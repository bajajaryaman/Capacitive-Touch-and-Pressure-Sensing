#include <Wire.h>   // Library for I2C Communication
#include "Adafruit_MPR121.h"    // Library for MPR121

Adafruit_MPR121 cap_sense = Adafruit_MPR121(); // Create object to use functions on board

#define MPR121_ADDR 0x5B    // I2C Address of MPR121 Board
#define PRINT_DELAY 200     

// Define the dimensions of the virtual grid
const int GRID_COLS = 5;
const int GRID_ROWS = 7;
bool virtualGrid[GRID_ROWS][GRID_COLS] = {false}; // Initialize all cells to false (untouched)

void setup() {
  Serial.begin(115200);
  while (!Serial);     // Wait for Serial to be ready
  if (!cap_sense.begin(MPR121_ADDR)) {
    Serial.println("Error setting up MPR121");
    while (1);        // If error in setting up then Infinite loop to stop execution
  }

  // Recalibrate the sensor by setting touch and release thresholds
  recalibrateSensor();
  
  Serial.println("MPR121 setup complete.");
}

void loop() {
  updateVirtualGrid();    // Get values from the electrodes 
  printVirtualGrid();     // Print those values in the grid format 
  delay(PRINT_DELAY);
}

void recalibrateSensor() {
  // Values adjusted based on testing with the specific overlay  
    cap_sense.setThresholds( 0.687, 0.371); 
}

void updateVirtualGrid() {
  uint16_t touchStatus = cap_sense.touched();   // Get touch status about sensor
  
  // Reset the virtual grid
  memset(virtualGrid, 0, sizeof(virtualGrid));

  // Check the touch status of column electrodes (0-4) and store them 
  bool colStatus[GRID_COLS];
  for (int i = 0; i < GRID_COLS; i++) {
    colStatus[i] = touchStatus & _BV(i);
  }
  
  // Check the touch status of row electrodes (5-11) and store them 
  bool rowStatus[GRID_ROWS];
  for (int i = 0; i < GRID_ROWS; i++) {
    rowStatus[i] = touchStatus & _BV(i + GRID_COLS);
  }
  
  // Set the virtual grid cells based on touch status
  for (int row = 0; row < GRID_ROWS; row++) {
    for (int col = 0; col < GRID_COLS; col++) {
      virtualGrid[row][col] = colStatus[col] && rowStatus[row];
    }
  }
}

void printVirtualGrid() {
  Serial.println("VIRTUAL GRID");
  for (int row = 0; row < GRID_ROWS; row++) {
    for (int col = 0; col < GRID_COLS; col++) {
      Serial.print(virtualGrid[row][col] ? "1" : "0");  // Print '1' if the cell is touched, otherwise '0'
      if (col < GRID_COLS - 1) {
        Serial.print(" | ");  // Add after putting value 
      } else {
        Serial.println();     // Add when you reach the end of the row
      }
    }
    if (row < GRID_ROWS - 1) {
      Serial.println("-------------------------------");
    }
  }
  Serial.println("END OF GRID");
}
