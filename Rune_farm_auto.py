import keyboard
import time
import logging
import pyautogui
import mouse
import pydirectinput




# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("elden_ring_automation.log"),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger(__name__)


def move_forward(duration):
    logger.info('Attempting to move forward for %s seconds', duration)
    
    keyboard.press('w') # Press the 'W' key to move forward
    time.sleep(0.1)
    keyboard.press('shift')
    time.sleep(duration)
     # Duration to move forward
    keyboard.release('w')
    keyboard.release('shift')
    logger.info('Movement completed')

def mount_horse():
    keyboard.press('e')
    pyautogui.scroll(-100)  # Negative value scrolls down
    keyboard.release('e')

def demount_horse():
    keyboard.press('c')
    time.sleep(0.5)
    keyboard.release('c')

def sharp_turn(x_offset, duration):
    start_x, start_y = pydirectinput.position()
    num_steps = int(duration / 0.005)  # Number of steps based on desired duration
    step_x = x_offset / num_steps

    for _ in range(num_steps):
        start_x += step_x
        pydirectinput.moveTo(int(start_x), int(start_y))
        time.sleep(0.005)  # Small sleep time for sharper movement

def rotate_180_sharp(duration):
    # Press shift + w to move forward
    keyboard.press('w')
    keyboard.press('shift')
    
    # Rotate the camera sharply to the right for 180 degrees
    sharp_turn(125, 0.2)  # Adjust the x_offset and duration as needed for a 180-degree turn
    
    # Release keys after rotation
    keyboard.release('w')
    keyboard.release('shift')

def starter_after_grace():
    keyboard.press('s')
    time.sleep(1.42)
    keyboard.release('s')
    keyboard.press('q')
    time.sleep(0.1)
    keyboard.release('q')

def look_left(i):
    keyboard.press('shift + w + a')
    # time.sleep(0.6849+(((0.001)*i)%4))
    time.sleep(0.6848)
    keyboard.release('shift + w + a')
    time.sleep(0.7)

def go_right_sharp():
    keyboard.press('shift + d')
    time.sleep(1.05)
    keyboard.press('shift + w')
    keyboard.release('shift + d')
    time.sleep(0.19 )
    keyboard.release('shift + w')

    keyboard.press('shift + d')
    time.sleep(1 )
    keyboard.press('space')
    time.sleep(0.1)
    keyboard.release('space')
    keyboard.release('shift + d')

    print("Dodged")

def look_right(step_size=5, total_distance=10):
    start_x, start_y = pydirectinput.position()
    steps = total_distance // step_size
    for _ in range(steps):
        pydirectinput.moveTo(start_x + step_size, start_y)
        start_x += step_size
        time.sleep(0.01)  # Adjust delay if necessary
    print("Looked right")

def q_button():
    keyboard.press('q')
    time.sleep(0.1)
    keyboard.release('q')

def dodge_ball_from_grace(i):
    time.sleep(1.2)
    starter_after_grace()
    time.sleep(1)
    mount_horse()
    time.sleep(3)
    look_left(i)
    time.sleep(0.5)

    move_forward(4.274)
    keyboard.press('e')
    time.sleep(0.03)
    keyboard.release('e')
    move_forward(3.8)

    go_right_sharp()
    time.sleep(0.5)

def open_map():
    time.sleep(0.2)
    keyboard.press('g')
    time.sleep(0.2)
    keyboard.release('g')
    
def go_to_grace():
    keyboard.press('d')
    time.sleep(0.43)
    keyboard.release('d')
    keyboard.press('s')
    time.sleep(0.17)
    keyboard.release('s')
    time.sleep(0.1)

    keyboard.press('e')
    time.sleep(0.1)
    keyboard.release('e')
    time.sleep(0.1)
    keyboard.press('e')
    time.sleep(0.1)
    keyboard.release('e')
    time.sleep(7.2)

#### TESTING AREA

# Give yourself a few seconds to switch to the game window
logger.info('Switch to the game window within the next 5 seconds')
time.sleep(5)  

for i in range (175):
    print(f"Round {i+1} completed!")
    dodge_ball_from_grace(i)
    time.sleep(4)
    open_map()
    time.sleep(0.1)
    go_to_grace()



# time.sleep(3)
# demount_horse()



