import pyautogui
import random
import numpy as np
import time

class AutoClicker:
    def __init__(self, run_type ,run_time = 50, right_skew=2, mean=5, std=1, min_value=0.5):
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

    def start(self):
        while True:
            self.move(self.x, self.y)  # move to starting position
            self.click()  # click mouse
            time.sleep(self.interval)

    def repeat_click(self, repeat_interval, break_interval):
        while True:
            self.click()  # click mouse
            time.sleep(repeat_interval)
            self.take_break(break_interval)


    def take_break(self, break_interval):
        # pause for a random amount of time within the range of break_interval
        time.sleep(random.uniform(break_interval[0], break_interval[1]))


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
        time.sleep(value)

    def run(self):
        start_time = time.time()
        while time.time() - start_time < self.run_time:
            self.click()
            self.pause_skewed(self.right_skew, self.mean, self.std, self.min_value)