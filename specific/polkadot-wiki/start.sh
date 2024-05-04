#!/bin/bash
# 設置環境變數
export app_id="xxxxxx"
export api_key="xxxxxxx"

# Clone Polkadot Wiki repository
mkdir /github
cd /github
git clone https://github.com/agbld/polkadot-wiki.git
cd /github/polkadot-wiki
git checkout dune-analytics

# 安裝依賴
yarn install

# 啟動 Polkadot Wiki
yarn polkadot:build
yarn polkadot:start

# 啟動 SSH 服務
/usr/sbin/sshd -D
