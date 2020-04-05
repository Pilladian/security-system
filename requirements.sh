# Requirements

# Installation of pip and cmake on Debian Linux based Systems
# sudo apt install python3-pip cmake

# Installation of openblas, pip and cmake on Arch Linux based Systems
# sudo pacman -Sy openblas python-pip cmake


# Installing actual python packages
pip3 install opencv-python numpy scipy face_recognition pathlib dlib==19.15.0


#### Troubleshooting ####

# unable to locate package python3-pip (Ubuntu)
	# https://askubuntu.com/questions/1061486/unable-to-locate-package-python-pip-when-trying-to-install-from-fresh-18-04-in

# ImportError: /home/manjaro/.local/lib/python3.8/site-packages/dlib.cpython-38-x86_64-linux-gnu.so: undefined symbol: cblas_dtrsm (Manjaro)
	# https://github.com/ageitgey/face_recognition/issues/731
