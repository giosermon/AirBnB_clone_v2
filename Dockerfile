FROM ubuntu:bionic

# install previous packages
RUN apt-get update
RUN apt-get install software-properties-common git vim neovim --force-yes -y

# install python 3.4
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update
RUN apt-get install python3.4 python3-dev python3-pip -y --force-yes

# install python mysqlDb
RUN apt-get install libmysqlclient-dev -y --force-yes
RUN apt-get install zlib1g-dev -y --force-yes
RUN pip3 install mysqlclient==1.3.10
RUN pip3 install SQLAlchemy==1.2.5


# Custom config
RUN git clone https://github.com/williamzborja/linux-env.git
RUN cd linux-env && ./install.sh

# Install mysql

RUN echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | tee -a /etc/apt/sources.list
RUN apt-get install mysql-server-5.7 -y --force-yes
RUN apt-get autoremove -y


ENTRYPOINT [ "/bin/bash" ]
