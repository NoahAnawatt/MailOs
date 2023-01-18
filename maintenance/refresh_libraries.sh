# Library Refresher
# Version 1.0
# This script must be run as an administrator. It will update all
# system packages and install to the latest version. It will also
# recover from catastrophic python failure. 

apt update
apt upgrade
apt autoremove