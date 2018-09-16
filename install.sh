sudo cp twelite-read.service /etc/systemd/system/
sudo cp shutdownbuttond.service /etc/systemd/system/
sudo systemctl start twelite-read.service
sudo systemctl enable twelite-read.service
sudo systemctl start shutdownbuttond.service
sudo systemctl enable shutdownbuttond.service
