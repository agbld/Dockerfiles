FROM ghcr.io/cirruslabs/flutter:latest

# 設定環境變數以避免在安裝過程中出現交互式提示
ENV DEBIAN_FRONTEND=noninteractive

# 更新APT套件列表並安裝SSH服務、screen和htop
RUN apt-get update && apt-get install -y openssh-server wget screen htop

# 設定SSH服務
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd  # 請將root:root替換成更安全的密碼
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH登錄時需要的環境變數修正
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# 清理APT緩存以減少映像大小
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# 開放22端口以使用SSH
EXPOSE 22

# 啟動SSH服務
CMD ["/usr/sbin/sshd", "-D"]