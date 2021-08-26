FROM holbertonschool/ubuntu-1404-fabric3
# Custom config
RUN git clone https://github.com/williamzborja/linux-env.git
RUN cd linux-env && ./install.sh

ENTRYPOINT [ "/bin/bash" ]
