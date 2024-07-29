from flask import Flask, request, jsonify
import requests
import argparse

# parse command line arguments: host, port, model, post-prompts
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--host', type=str)
arg_parser.add_argument('--port', type=int, default=11434)
arg_parser.add_argument('--model', type=str, default='llama3.1')
arg_parser.add_argument('--post-prompts', type=str, default='')
args = arg_parser.parse_args()

app = Flask(__name__)

LLM_API_URL = f"http://{args.host}:{args.port}/api/generate"
MODEL = args.model

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json

    source_lang = data.get('source_lang')
    target_lang = data.get('target_lang')
    text_list = data.get('text_list')

    translations = []

    for text in text_list:
        prompt = f"""Translate the following source text to {target_lang}, Output translation directly without any additional text.
Source Text: {text}

Translated Text:"""
        # prompt = f"Translate the following source text to {target_lang}. Output translation directly without any additional text.\n```\n{text}\n```\n{args.post_prompts}"
        response = requests.post(LLM_API_URL, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "system": "You are a professional, authentic machine translation engine.",
        })
        translation_result = response.json()
        translated_text = translation_result.get('response', '')  # assuming the response has a 'text' field

        translations.append({
            "detected_source_lang": source_lang,
            "text": translated_text
        })

    return jsonify({"translations": translations})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
