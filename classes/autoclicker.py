import pyautogui
import random
import numpy as np
import time

class AutoClicker:
    def __init__(self, run_type = "wiggle" ,run_time = 50, right_skew=2, mean=0.5, std=0.35, min_value=0.3):
        self.run_type = run_type
        self.run_time = run_time * 60 # Convert minutes to seconds
        self.right_skew = right_skew
        self.mean = mean
        self.std = std
        self.min_value = min_value

    def set_position(self):
        self.x, self.y = pyautogui.position()  # get current mouse position

    def get_position(self):
        return pyautogui.position()
        
    def click(self):
        pyautogui.click()

    def move(self, x_offset, y_offset):
        pyautogui.moveRel(x_offset, y_offset)

    def take_break(self, break_interval):
        # pause for a random amount of time within the range of break_interval
        break_time = random.uniform(break_interval[0], break_interval[1])
        print("Taking a break for {} seconds".format(break_time))
        time.sleep(break_time)


    def pause_skewed(self, right_skew=2, mean=5, std=1, min_value=0.5):
        """Pause for a random amount of time based on a right-skewed distribution.

        Parameters:
        right_skew (float): Skewness of the distribution, where a higher value corresponds to a more right-skewed distribution. Default is 2.
        mean (float): Mean value of the distribution. Default is 5.
        std (float): Standard deviation of the distribution. Default is 1.
        min_value (float): Minimum value of the pause duration. Default is 0.5.

        Returns:
        None
        """
        # Generate a random value from a right-skewed distribution
        value = np.random.normal(loc=mean, scale=std) ** right_skew
        value = max(value, min_value)  # enforce minimum value
        # Pause the program for the random duration
        print("Pausing for {} seconds".format(value))
        time.sleep(value)

    def mouse_wiggle(self, x_offset, y_offset):
        """Wiggle the mouse cursor.

        Parameters:
        x_offset (int): Maximum x offset from the current position.
        y_offset (int): Maximum y offset from the current position.

        Returns:
        None
        """
        # Generate random offsets
        x = random.randint(-x_offset, x_offset)
        y = random.randint(-y_offset, y_offset)
        # Move the mouse cursor
        self.move(x, y)

    def run(self):
        start_time = time.time()
        self.take_break([10,12])
        self.set_position()
        while time.time() - start_time < self.run_time:

            if self.run_type == "wiggle":
                self.mouse_wiggle(250, 250)
                self.take_break([30, 300])
            elif self.run_type == "click":
                rnd = random.randint(0, 100)
                print(rnd)
            
                if rnd < 3:
                    self.mouse_wiggle(5,5)
                    self.pause_skewed(self.right_skew, self.mean, self.std, self.min_value)
                elif rnd == 3:
                    self.pause_skewed(6, 5, self.std, self.min_value)
                elif rnd < 25:
                    self.take_break([0.5, 2])
                else:
                    self.pause_skewed(self.right_skew, self.mean, self.std, self.min_value)

                self.click()
                    


                

