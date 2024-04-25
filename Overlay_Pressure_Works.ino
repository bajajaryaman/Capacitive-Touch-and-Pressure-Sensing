#include <Wire.h>
#include "Adafruit_MPR121.h"

Adafruit_MPR121 cap_sense = Adafruit_MPR121();    // Object of class MPR121

#define MPR121_ADDR 0x5B
#define PRINT_DELAY 200 // Milliseconds between updates

// Manually define FLT_MAX and FLT_MIN
#define FLT_MAX  3.4028235E+38
#define FLT_MIN -3.4028235E+38

// Initialize min and max observed values arrays with placeholders
float minValues[7][5];
float maxValues[7][5];
bool isFirstRun = true; // Flag to initialize min/max arrays

void setup() {
  Serial.begin(115200);
  while (!Serial); // Wait for Serial to be ready
  if (!cap_sense.begin(MPR121_ADDR)) {
    Serial.println("MPR121 not found, check wiring?");
    while (1);    // If error , then infinite loop is run
  }
  Serial.println("MPR121 setup complete.");
  recalibrateSensor();
}

void recalibrateSensor() {
  for (int i = 0; i < 12; i++) {
    cap_sense.setThresholds(0.687, 0.366); // Threshold values onbtained by testing
  }
}

void loop() {
  if (isFirstRun) {
    initializeMinMaxValues();
    isFirstRun = false;         // Done so that the grid elements are only intialised once intially 
  }

  Serial.println("VIRTUAL GRID CAPACITANCE DELTAS:");
  for (int row = 0; row < 7; row++) {
    for (int col = 0; col < 5; col++) {
      int rowElectrode = row + 5; // electrodes 5-11 are rows
      int colElectrode = col;     // electrodes 0-4 are columns

      float deltaCap = calculateDelta(rowElectrode, colElectrode);
      updateMinMaxValues(deltaCap, row, col);                       // Done to dynamically change the range of min and max values 

      float normalizedDelta = normalizeDelta(deltaCap, row, col);   // Done to normalise the values

      Serial.print(normalizedDelta, 4);   // Prints till 4 decimal places 
      if (col < 4) Serial.print(", ");
    }
    Serial.println();
  }
  Serial.println("-----END OF GRID-----");
  delay(PRINT_DELAY);
}

void initializeMinMaxValues() {             //Initialises sensor grid element with predefined min and max values 
  for (int row = 0; row < 7; row++) {
    for (int col = 0; col < 5; col++) {
      minValues[row][col] = FLT_MAX;
      maxValues[row][col] = FLT_MIN;
    }
  }
}

float calculateDelta(int rowElectrode, int colElectrode) {      // Calculated average delta for grid element 
  float deltaRow = getCapacitanceDelta(rowElectrode);
  float deltaCol = getCapacitanceDelta(colElectrode);
  
  return (deltaRow + deltaCol) / 2.0;
}

float getCapacitanceDelta(int electrode) {        
  uint16_t filteredData = cap_sense.filteredData(electrode);
  uint16_t baselineData = cap_sense.baselineData(electrode);
  
  return ((8.0 * 1024) / (5.0 * filteredData)) - ((8.0 * 1024) / (5.0 * baselineData));
}

float normalizeDelta(float delta, int row, int col) {
  float range = maxValues[row][col] - minValues[row][col];
  if (range == 0) return 0; // Avoid division by zero
  return (delta - minValues[row][col]) / range;
}

void updateMinMaxValues(float delta, int row, int col) {                // Updates min and max values 
  if (delta < minValues[row][col]) minValues[row][col] = delta;         // If value is lower than the min value, then it becomes the new min value
  if (delta > maxValues[row][col]) maxValues[row][col] = delta;         // If value is greater than the max value, then it becomes the new max value
}
