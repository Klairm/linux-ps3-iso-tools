# LINUX-PS3-ISO-TOOLS
A GUI for use the iso tools created by Hermes

You will need python3 for use this.

## Setup
This will clone the repository, and execute a script for copy the binary iso tools into `/usr/bin/` so the files can be executed from anywhere
```
git clone https://github.com/Klairm/LINUX-PS3-ISO-TOOLS

cd LINUX-PS3-ISO-TOOLS

./setup.sh

```
## Usage
You could either double click on `PS3_ISO_Tools.py` (which depending on your distro can be executed) or run via terminal using `python3 PS3_ISO_Tools.py`
## TODO:
- Add error handler ( right now if something goes wrong the GUI won't tell)
- Optimize the progress bar
- Provide as single executable file

This it's just a python GUI made with pythonQT for the ps3iso utilites programs created by Estwald/Hermes
