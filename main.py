import mouse
import time

# Global variable to control the loop
running = True

def click_mouse(delay):
    while running:
        time.sleep(delay)
        #mouse.click()
        print("Clicking...") # For testing purposes

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
            delay = float(input("Enter time delay in seconds: "))
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
        running = True
        mouse.on_click(stop_clicking)
        click_mouse(delay)

main()