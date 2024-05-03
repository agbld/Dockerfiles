#!/bin/bash
# 設置環境變數
export app_id="xxxxxx"
export api_key="xxxxxxx"

# 運行 yarn 命令來啟動應用
yarn polkadot:start

# 啟動 SSH 服務
/usr/sbin/sshd -D
