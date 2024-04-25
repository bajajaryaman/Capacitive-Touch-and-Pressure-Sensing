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

# Setup the serial connection to the Arduino
serialPort = "COM11"  
ser = Serial(serialPort, baudrate=115200, timeout=1)  # Adjusted to match the Arduino's baud rate

# Setup the Pygame screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('5x7 Grid Heatmap Visualization')

# Function to convert normalized delta to color intensity
def delta_to_color(delta):
    if delta != delta:  # Check for NaN
        print("Received NaN value")
        return (255, 255, 255)  # Return white color for NaN values
    # Ensure delta is within the 0-1 range
    # Amplify the delta values for visualization purposes
    amplified_delta = min(max(delta ** 2, 0), 1)  # Squaring the delta to amplify changes
    color_val = int((1.0 - amplified_delta) * 255)  # Convert the amplified delta to a color value
    return color_val, color_val, color_val  # Returning a shade of blue

def main_loop():
    while True:
        # Check for Pygame events (window close)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                ser.close()  # Close serial port
                pygame.quit()  # Quit Pygame
                sys.exit()  # Exit the script

        # Read serial data if available
        if ser.in_waiting > 0:
            line = ser.readline().decode("utf-8").strip()  # Read a line of text from the serial port
            if "VIRTUAL GRID" in line:  # Check if the line indicates the start of grid data
                # Clear screen with white at the start of each grid read
                screen.fill((255, 255, 255))
                for row in range(GRID_ROWS):
                    line = ser.readline().decode("utf-8").strip()  # Read the next line for row data
                    if "END OF GRID" in line:
                        break
                    cells = line.split(', ')  # Split the line into individual cell values
                    for col, cell in enumerate(cells):
                        try:
                            delta = float(cell)
                            color_val = delta_to_color(delta)  # Get the color based on the delta
                        except ValueError:
                            # Handle any potential conversion error
                            print(f"Error parsing value: {cell}")
                            color_val = (255, 255, 255)  # Default to white

                        # Draw the cell on the screen
                        rect = pygame.Rect(col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
                        pygame.draw.rect(screen, color_val, rect)
                # Update the display with the new grid
                pygame.display.flip()

if __name__ == "__main__":
    main_loop()
