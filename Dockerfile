FROM ubuntu:20.04

LABEL author="Maja Franz <maja.franz@st.othr.de>"

ENV DEBIAN_FRONTEND noninteractive
ENV LANG="C.UTF-8"
ENV LC_ALL="C.UTF-8"

# Install required packages
RUN apt-get update && apt-get install -y \
        python3 \
        python3-pip \
        git \
        unzip

# Add user
RUN useradd -m -G sudo -s /bin/bash pix && echo "pix:pix" | chpasswd
RUN usermod -a -G staff pix
USER pix

WORKDIR /home/pix/

RUN git clone https://github.com/majafranz/pix2pix_mri_ce
WORKDIR /home/pix/pix2pix_mri_ce

# process dataset
ADD --chown=pix:pix archive.zip /home/pix/pix2pix_mri_ce
RUN unzip archive.zip -d archive
WORKDIR /home/pix/pix2pix_mri_ce/archive
RUN tar -xf BraTS2021_Training_Data.tar
WORKDIR /home/pix/pix2pix_mri_ce
RUN python3 data_processing.py

# install python packages
ENV PATH $PATH:/home/pix/.local/bin
RUN pip3 install -r requirements.txt

ENTRYPOINT ["./run.sh"]
CMD ["jupyter"]
