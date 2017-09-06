sudo mkdir /home/pi/Desktop/Imagenes
sudo mkdir /home/pi/Desktop/Grabaciones
sudo mkdir /home/pi/Desktop/Capturas
sudo cp -r Interfaz /home/pi/Desktop
sudo cp -r Diccionario /home/pi
sudo mkdir /home/pi/pocketsphinx
cd /home/pi/pocketsphinx

sudo apt-get update -y
sudo apt-get upgrade -y

sudo echo "@xset s off" >> /home/pi/.config/lxsession/LXDE-pi/autostart
sudo echo "@xset -dpms" >> /home/pi/.config/lxsession/LXDE-pi/autostart
sudo echo "@xset s noblank" >> /home/pi/.config/lxsession/LXDE-pi/autostart
sudo echo "sleep(5)" >> /home/pi/.config/lxsession/LXDE-pi/autostart
sudo echo "sudo python /home/pi/Desktop/Interfaz/lanzar.py &" >> /home/pi/.config/lxsession/LXDE-pi/autostart

sudo apt-get install ppp wvdial -y
sudo apt-get install hostapd isc-dhcp-server -y
sudo apt-get install python-serial -y

sudo apt-get install mplayer -y

sudo apt-get install python-pygame -y

sudo apt-get install python-picamera python3-picamera -y
sudo apt-get install python-picamera -y
sudo apt-get install python-opencv -y
sudo apt-get install python-scipy -y
sudo apt-get install ipython -y
sudo apt-get install qrencode -y
sudo apt-get install python-zbar -y

sudo apt-get install alsa-utils -y
sudo apt-get install mpg321 -y
sudo apt-get install lame -y
sudo apt-get install festival -y
sudo apt-get install espeak -y

sudo wget https://sourceforge.net/projects/cmusphinx/files/sphinxbase/5prealpha/sphinxbase-5prealpha.tar.gz/download -O sphinxbase.tar.gz
sudo wget https://sourceforge.net/projects/cmusphinx/files/pocketsphinx/5prealpha/pocketsphinx-5prealpha.tar.gz/download -O pocketsphinx.tar.gz

sudo tar -xzvf sphinxbase.tar.gz
sudo tar -xzvf pocketsphinx.tar.gz

cd sphinxbase-5prealpha
sudo ./configure --enable-fixed
sudo make
sudo make install
cd ../pocketsphinx-5prealpha
sudo ./configure
sudo make
sudo make install

sudo ldconfig