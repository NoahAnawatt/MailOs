import os
import subprocess

# Install GStreamer development packages
subprocess.call(['sudo', 'apt-get', 'install', 'libgstreamer1.0-dev', 'libgstreamer-plugins-base1.0-dev'])

# Install OpenCV dependencies
subprocess.call(['sudo', 'apt-get', 'install', 'build-essential', 'cmake', 'git', 'libgtk2.0-dev', 'pkg-config', 'libavcodec-dev', 'libavformat-dev', 'libswscale-dev'])

# Clone the OpenCV source code repository
subprocess.call(['git', 'clone', 'https://github.com/opencv/opencv.git'])

# Create a build directory and navigate into it
os.chdir('opencv')
os.mkdir('build')
os.chdir('build')

# Configure the build with CMake, enabling GStreamer support
subprocess.call(['cmake', '-D', 'CMAKE_BUILD_TYPE=RELEASE', '-D', 'CMAKE_INSTALL_PREFIX=/usr/local', '-D', 'WITH_GSTREAMER=ON', '..'])

# Build and install OpenCV
subprocess.call(['make', '-j4'])
subprocess.call(['sudo', 'make', 'install'])

# Verify that OpenCV was installed with GStreamer support
import cv2
print(cv2.getBuildInformation())

