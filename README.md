To install please use pip install git+https://github.com/beling86/b86_utils#egg=b86_utils

installing code-server on..

#Update termux and install debian

termux-setup-storage && pkg update -y && pkg install proot-distro -y && proot-distro install debian && proot-distro login debian

#Update debian
pkg update -y && pkg upgrade -y
#Install nodejs v16
curl -fsSL https://deb.nodesource.com/setup_16.x | bash 
apt install nodejs

#Install code-server
curl -fsSL https://code-server.dev/install.sh | sh

#Install python requirements
pkg install make build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
  libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git vim -y
  
#install Pyenv
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

#Everything is set.. now time to set up environment
run code server and then kill it
code-server
ctrl+c

nano /etc/profile 
add:
start-stop-daemon --start --exec /usr/bin/code-server -b
export PYENV_ROOT="/root/.pyenv"
export PATH="/root/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"

nano ~/.config/code-server/config.yaml
auth = none

#Exit debian, take opportunity to automate debian startup.. 
exit
nano /data/data/com.termux/files/usr/etc/profile
proot-distro login debian --bind /data/data/com.termux/files/home/storage:/storage

#now everything is set, finally install python


#Finally, install python
pyenv install 3.10.6
touch /root/.pyenv/version && echo 3.10.6 > /root/.pyenv/version
