# Capacitive-Touch-and-Pressure-Sensing

Welcome to the GitHub repository for an innovative capacitive touch/tactile sensor project, designed to enhance robotic manipulators with advanced touch and pressure sensing capabilities. This project integrates a novel application of capacitive sensing technology to provide robotic systems with detailed tactile feedback, crucial for handling delicate objects and performing precise tasks.

**User Installation Instructions**
Follow these step-by-step instructions to get started with the software for this project.

**Prerequisites**
Before you begin, ensure you have met the following requirements:

- You have installed the latest version of [Arduino IDE](https://www.arduino.cc/en/software) for the Arduino code.
- You have installed Python 3. You can download it from [python.org](https://www.python.org/downloads/).
- You have a basic understanding of Python programming and the Arduino platform.

**Installing Python Dependencies**
1. Open your terminal or command prompt.
2. Install the required Python libraries by running:

_pip install pyserial pygame_

**Setting up the Arduino Environment**
1. Connect your Arduino device to your computer via USB.
2. Open the Arduino IDE.
3. Under the Tools menu, select the Board that matches your Arduino device.
4. Under the Tools menu, select the Port that your Arduino is connected to.
5. Open the Arduino code .ino file from the repository.
   
**Uploading the Arduino Code**
Click the "Verify" button (checkmark icon) to compile the code.
Click the "Upload" button (arrow icon) to upload the code to your Arduino device.
Running the Python Script
Ensure the Arduino is still connected via USB after uploading the code.
Modify the serialPort variable in the Python script to match the port your Arduino is connected to (you can find this in the Arduino IDE under Tools > Port).
Save the Python script.
Run the Python script in your terminal or command prompt with:
Copy code
python your_script_name.py
Interacting with the Program
Once the Arduino code is uploaded and the Python script is running, you can interact with the program according to the project's specifications.
The Python script will visualize the data from the Arduino device in real-time.
