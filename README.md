# LINUX-PS3-ISO-TOOLS

![image](https://i.imgur.com/XmEYZ1w.png)

A GUI for use the ps3 iso tools on Linux

## Using the release version:
For use the release version you will need ( for now ) be in a 64bit machine with the python version: Python 3.8.3
If you don't have a 64bit machine or you're on another version of Python 3, you need to execute the .py file, read below for more information

## Dependencies needed:
python3, python3-setuptools, python3-pip, python3-pyqt5, git

## Setup
This will clone the repository, and execute a script for copy the binary iso tools into `/usr/bin/` so the files can be executed from anywhere, and also will install the dependencies for python3, also it will install QtWaitingSpinner
```
git clone https://github.com/Klairm/LINUX-PS3-ISO-TOOLS

cd LINUX-PS3-ISO-TOOLS

./setup.sh

```
## Usage
You could either double click on `PS3_ISO_Tools.py` (which depending on your distro can be executed) or run via terminal using `python3 PS3_ISO_Tools.py`


## TODO:
- Add error handler ( right now if something goes wrong the GUI won't tell)
- Provide a installer for different package managers to install the dependencies python3, python3-pip and python3-pyqt5
- Make a greater GUI


This it's just a python GUI made with pythonQT created by Klairm for the ps3iso utilites programs created by Estwald/Hermes
That's why there's 2 binaries included in a folder, those were created  by Estwald/Hermes.

![image](https://i.imgur.com/cTZlvDO.png)
