import threading
import mouse
import keyboard
import time

# Global variable to control the loop
running = True

def click_mouse(delay):
    while running:
        time.sleep(delay)
        mouse.click()
        print("Clicking...") # For testing purposes
        keyboard.on_press_key("space", lambda _: stop_clicking())

def stop_clicking():
    global running
    running = False

def get_user_confirmation():
    while True:
        input_to_run = input("Do you want to run the program? (y/n): ")
        if input_to_run in ['y', 'n']:
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    return input_to_run

def get_user_delay():
    while True:
        try:
            delay = 1 / float(input("Enter keypresses per second: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    return delay

def main():
    global running
    while True:
        user_confirmation = get_user_confirmation()
        if user_confirmation == 'n':
            break
        
        delay = get_user_delay()
        print("Press space to start clicking. Press space again to stop.")
        keyboard.wait("space")
        click_mouse(delay)
        keyboard.unhook_all()
        running = True

main()