import pygame
import sys
from serial import Serial

# Initialize Pygame
pygame.init()

# Constants for the window size
GRID_COLS = 5
GRID_ROWS = 7
CELL_WIDTH = 100
CELL_HEIGHT = 100
WINDOW_WIDTH = GRID_COLS * CELL_WIDTH
WINDOW_HEIGHT = GRID_ROWS * CELL_HEIGHT

# Serial connection to the Arduino
serialPort = "COM11"  
ser = Serial(serialPort, baudrate=115200, timeout=1)        # Setup Serial

# Setup  Pygame screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('5x7 Grid Heatmap Visualization')            # Window Title

# Function to read and update the virtual grid
def update_virtual_grid():  
    grid_data = []      # Initialize the list that will hold grid data
    while len(grid_data) < GRID_ROWS:
        if ser.in_waiting > 0:          # If data is there 
            line = ser.readline().decode('utf-8').strip()       
            print(f"Received line: {line}")  # Debugging print
            if "VIRTUAL GRID" in line:          # Check if the line indicates the start of grid data
                grid_data = []  # Start a new grid
            elif line and line[0].isdigit():  # If the line starts with a digit
                grid_data.append([int(n) for n in line.split(' | ')])       # extract data from line and add to virtual grid
    return grid_data

# Function to draw the grid on the screen
def draw_grid(grid_data):
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            color_val = 255 * (1 - grid_data[row][col])  # 0 is touched, 1 is not touched
            rect = pygame.Rect(col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            pygame.draw.rect(screen, (color_val, color_val, color_val), rect)
    pygame.display.flip()       # update display

# Main loop
def main_loop():
    while True:
        grid_data = update_virtual_grid()
        draw_grid(grid_data)


        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                ser.close()     # Close the serial port
                pygame.quit()   # Quit Pygame
                sys.exit()      # Exit script

# Run the main loop if this script is executed
main_loop()

