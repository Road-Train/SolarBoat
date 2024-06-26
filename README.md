# SolarBoat
Knowledge Management Repository

Requirements:
Python 3.

Installation:
Run setup.bat
Running the program:
For Front-end, run main.py
For Back-end, run ReadControllerInputs.py


To run Code within Docker: 
docker run --privileged --cap-add=ALL --device=/dev/input/js0:/dev/input/js0 -e XDG_RUNTIME_DIR=/tmp/runtime-dir -v /home/solarboat/Downloads/SolarBoat-main:/app -w /app -it --user root solarboatmain:latest /bin/bash
python3 "the code file you want to run.py" (without the ") for example : python3 InputReader.py
