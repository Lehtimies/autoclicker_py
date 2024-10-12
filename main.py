import mouse
import time

running = True

def click_mouse(delay):
    while running:
        time.sleep(delay)
        #mouse.click()
        print("Clicking...") # For testing purposes

def stop_clicking():
    global running
    running = False

while True:
    while True:
        input_to_run = input("Do you want to run the program? (y/n): ")
        if input_to_run == 'y' or input_to_run =='n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
   
    if input_to_run == 'n':
        break
    
    while True:
        try:
            delay = float(input("Enter time delay in seconds: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        break

    mouse.on_click(stop_clicking)

    click_mouse(delay)
