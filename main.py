import mouse
import keyboard
import time
import threading

class AutoClicker:
    def __init__(self):
        self.delay = 1.0
        self.running = False
        self.quit = False
    
    def start_clicking(self):
        self.running = True
        threading.Thread(target=self.click_mouse).start()
        keyboard.on_press_key("g", lambda _: self.stop_clicking())

    def click_mouse(self):
        while self.running:
            if self.quit:
                break
            time.sleep(self.delay)
            mouse.click()
            #print("Clicking...") # For testing purposes
            

    def stop_clicking(self):
        self.running = False

    def get_user_confirmation(self):
        while True:
            input_to_run = input("Do you want to run the program? (y/n): ")
            if input_to_run in ['y', 'n']:
                return input_to_run
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def get_user_delay(self):
        while True:
            try:
                delay = 1 / float(input("Enter keypresses per second: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        return delay

    def leave(self):
        self.quit = True

    def main(self):
        while True:
            user_confirmation = self.get_user_confirmation()
            if user_confirmation == 'n':
                break
            self.delay = self.get_user_delay()
            print("Press 'g' to start clicking. Press 'g' again to stop.\nPress 'ctrl+q' to quit.")
            while not self.quit:
                keyboard.add_hotkey("ctrl+q", lambda: self.leave())
                if not self.quit:
                    keyboard.wait("g")
                self.start_clicking()
                if not self.quit:
                    keyboard.wait("g")
                self.stop_clicking()
                keyboard.unhook_all()
            self.quit = False

if __name__ == "__main__":
    clicker = AutoClicker()
    clicker.main()