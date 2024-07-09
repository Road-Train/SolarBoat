# SolarBoat
Knowledge Management Repository

Requirements:
Python 3.
## Installing:
pip install -r requirements.txt should get you all the requirements that you'll need for this project.
## Running the various programs in here:
### For the object recognition/disparity map:
Run Server.py, wait until it is started.
Follow instructions in BoatSim\simulation\templates\Simulation, version 2\README.md to run the front-end, it should automatically work.
### For webcam object recognition:
Run OldObjectRecognition.py, make sure it is set up to actually use the webcam.
### For the controller input reader:
Run InputReader.py

Note: The docker containers DO NOT work unless used via the NUC.

To run Code within Docker: 
docker run --privileged --cap-add=ALL --device=/dev/input/js0:/dev/input/js0 -e XDG_RUNTIME_DIR=/tmp/runtime-dir -v /home/solarboat/Downloads/SolarBoat-main:/app -w /app -it --user root solarboatmain:latest /bin/bash
python3 "the code file you want to run.py" (without the ") for example : python3 InputReader.py
