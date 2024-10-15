import mouse
import keyboard
import time

# Global variable to control the loop
running = True
quit = False

def click_mouse(delay):
    while running:
        if quit:
            break
        time.sleep(delay)
        mouse.click()
        # print("Clicking...") # For testing purposes
        keyboard.on_press_key("g", lambda _: stop_clicking())

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

def leave():
    global quit
    quit = True

def main():
    global running
    global quit
    while True:
        user_confirmation = get_user_confirmation()
        if user_confirmation == 'n':
            break
        
        delay = get_user_delay()
        print("Press 'g' to start clicking. Press 'g' again to stop.\nPress 'ctrl+q' to quit.")
        while not quit:
            keyboard.add_hotkey("ctrl+q", lambda: leave())
            keyboard.wait("g")
            click_mouse(delay)
            keyboard.unhook_all()
            running = True
        quit = False

main()