# Library Refresher
# This script must be run as an administrator. It will update all
# system packages and install to the latest version. It will also
# recover from catastrophic python failure. 

dpkg --configure -a
apt update
apt upgrade
apt autoremove
