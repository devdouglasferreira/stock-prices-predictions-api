sudo apt-get update
sudo apt-get install software-properties-common -y
sudo apt-get install gnupg2 -y
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 3B4FE6ACC0B21F32
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 871920D1991BC93C
sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu/ focal main restricted"
sudo apt-get update
sudo apt-get install wget -y
sudo apt-get install firefox -y
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/