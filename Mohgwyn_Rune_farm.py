import keyboard
import time
import logging
import pyautogui
import pydirectinput


# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("elden_ring_automation.log"),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger(__name__)

def q_button():
    keyboard.press('q')
    time.sleep(0.1)
    keyboard.release('q')

def open_map():
    time.sleep(0.2)
    keyboard.press('g')
    time.sleep(0.2)
    keyboard.release('g')

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

def move_diag_left(duration):
    keyboard.press('w+a') 
    time.sleep(0.1)
    keyboard.press('shift')
    time.sleep(duration)
    keyboard.release('w+a')
    keyboard.release('shift')
    logger.info('Movement diag_left completed')

def move_diag_right(duration):
    keyboard.press('w+d') 
    time.sleep(0.1)
    keyboard.press('shift')
    time.sleep(duration)
    keyboard.release('w+d')
    keyboard.release('shift')
    logger.info('Movement diag_right completed')

def perfect_loc_move():
    move_forward(3.5)
    move_diag_left(1.4)
    move_diag_right(0.8)
    move_diag_left(0.2)

def drink_flask():
    time.sleep(0.1)
    keyboard.press('r')
    time.sleep(0.1)
    keyboard.release('r')
    wait_time(2.5)

def wait_time(duration):
    time.sleep(duration)

def attack(duration):
    pydirectinput.mouseDown()
    time.sleep(duration)
    pydirectinput.mouseUp()
    
def move_to_grace():
    keyboard.press('s')
    time.sleep(0.1)
    keyboard.release('s')
    time.sleep(0.1)

    keyboard.press('e')
    time.sleep(0.1)
    keyboard.release('e')
    time.sleep(0.5)
    keyboard.press('e')
    time.sleep(0.1)
    keyboard.release('e')
    time.sleep(7.2)

# Give yourself a few seconds to switch to the game window
logger.info('Switch to the game window within the next 5 seconds')
time.sleep(5)  


for i in range (2000):
    print(f"Round {i+1} completed!")
    perfect_loc_move()
    q_button()
    drink_flask()
    attack(17)
    open_map()
    move_to_grace()