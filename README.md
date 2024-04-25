# Capacitive-Touch-and-Pressure-Sensing

Welcome to the GitHub repository for our innovative capacitive touch/tactile sensor project. This report introduces a capacitive touch/tactile sensor designed to enhance robotic manipulators, significantly improving their interaction capabilities within dynamic environments. The novel application of capacitive sensing technology equips robots with the ability to detect and evaluate the pressure and orientation of objects, a critical requirement for precise and gentle handling tasks in industries such as manufacturing, healthcare, and logistics.

Through the development and experimental validation of a prototype, this project demonstrates the potential of integrating enhanced touch sensitivity into robotic systems. The sensor's design, incorporating a neoprene overlay and utilizing the MPR121 chip for data processing, illustrates an innovative approach to tactile feedback. This advancement not only improves the functionality and adaptability of robots but also sets the foundation for further research and development in robotic tactile sensing across various applications.

![image](https://github.com/bajajaryaman/Capacitive-Touch-and-Pressure-Sensing/assets/128712444/fa1ab5dd-b95b-49f3-85e3-bbeb8432a54a)
Fig.1. Image of the sensor system

The image showcases the assembled sensor system, comprising an Arduino connected to a capacitive touch sensor array via multiple wires. This setup forms the core of the touch-sensing capability, allowing the system to detect and interpret tactile interactions for robotic applications.

## User Installation Instructions

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
1. Click the "Verify" button (checkmark icon) to compile the code.
2. Click the "Upload" button (arrow icon) to upload the code to your Arduino device.

**Running the Python Script**
1. Ensure the Arduino is still connected via USB after uploading the code.
2. Modify the serialPort variable in the Python script to match the port your Arduino is connected to (you can find this in the Arduino IDE under Tools > Port).
3. Save the Python script.
4. Run the Python script in your terminal or command prompt with:

 _python Touch_Test_.py

**Interacting with the Program**
- Once the Arduino code is uploaded and the Python script is running, you can interact with the program according to the project's specifications.
- The Python script will visualize the data from the Arduino device in real-time.

## Known Issues and Future Improvements

While the current implementation of the project provides the basic functionalities, there are several known issues and areas for future improvements:

### Known Issues

- **False Positives:** Occasionally, the system may register a touch even when there is none, commonly referred to as a false positive.
- **Sensitivity Fluctuations:** Some users might experience fluctuations in sensor sensitivity, potentially due to environmental factors such as temperature and humidity.

### Future Improvements

- **Machine Learning for False Positives:** Implement a machine learning algorithm to analyze the touch patterns and learn to distinguish between intentional touches and false positives.
- **Environmental Compensation:** Develop a compensation algorithm to adjust sensitivity based on environmental changes, ensuring consistent performance.
- **Enhanced Pressure Sensitivity:** Refine the pressure sensitivity algorithm to capture a wider range of touch pressures, from very light to very heavy.
- **Energy Efficiency:** Optimize the code to reduce power consumption for battery-powered implementations.
- **User Interface Improvements:** Develop a more intuitive and feature-rich user interface for better interaction with the system.

If you would like to suggest a new feature or report a bug, please open an issue on the project repository.

