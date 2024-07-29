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

# LLM_API_URL = f"http://{args.host}:{args.port}/api/generate"
LLM_API_URL = f"http://{args.host}:{args.port}/api/chat"
MODEL = args.model

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json

    source_lang = data.get('source_lang')
    target_lang = data.get('target_lang')
    if target_lang == 'zh-TW':
        target_lang = 'Traditional Chinese'
    text_list = data.get('text_list')

    translations = []

    for text in text_list:
#         prompt = """Translate the following source text to {target_lang}, Output translation directly without any additional text.
# Source Text: {text}

# Translated Text:"""
#         response = requests.post(LLM_API_URL, json={
#             "model": MODEL,
#             "prompt": prompt,
#             "stream": False,
#             "system": "You are a professional, authentic translator.",
#         })
#         translation_result = response.json()
#         translated_text = translation_result.get('response', '')

        prompt = f"Translate the following source text to {target_lang}. Output translation directly without any additional text, note, and explanations.\n\n{text}\n\n{args.post_prompts}"
        response = requests.post(LLM_API_URL, json={
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False,
            "system": "You are a effiecient machine translation engine. You will provide the translation WITHOUT any additional text, note, and explanations.",
        })
        translation_result = response.json()
        translated_text = translation_result.get('message', {}).get('content', '')

        translations.append({
            "detected_source_lang": source_lang,
            "text": translated_text
        })

    return jsonify({"translations": translations})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
