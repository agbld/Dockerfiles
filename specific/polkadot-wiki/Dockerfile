# 使用 Node.js 18 的官方 Docker 映像
FROM node:18-bullseye

# 安裝必要的系統工具
RUN apt-get update && apt-get install -y openssh-server wget screen htop build-essential libssl-dev git

# 設定 SSH 服務
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd  # 請將root:root替換成更安全的密碼
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH 登錄時需要的環境變數修正
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# # Clone Polkadot Wiki repository
# WORKDIR /github
# RUN git clone https://github.com/agbld/polkadot-wiki.git
# WORKDIR /github/polkadot-wiki
# RUN git checkout dune-analytics

# # Build and start Polkadot Wiki web server
# WORKDIR /github/polkadot-wiki
# RUN yarn install

# 將 start.sh 腳本添加到容器
COPY start.sh /start.sh
RUN chmod +x /start.sh

# 清理 APT 緩存以減少映像大小
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# 開放 22 端口以使用 SSH 和 3000 端口給 Polkadot Wiki 網站伺服器
EXPOSE 22
EXPOSE 3000

# 啟動 SSH 服務和應用程序
CMD ["/start.sh"]
