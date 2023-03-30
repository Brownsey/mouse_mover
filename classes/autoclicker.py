import pyautogui
import random
import numpy as np
import time
from scipy.stats import skewnorm

class AutoClicker:
    def __init__(self, run_type = "wiggle",run_time = 50, right_skew = 2, mean=0.5,  min_value=0.3):
        self.run_type = run_type
        self.run_time = run_time * 60 # Convert minutes to seconds
        self.right_skew = right_skew
        self.mean = mean
        self.min_value = min_value

    def set_position(self):
        self.x, self.y = pyautogui.position()  # get current mouse position

    def get_position(self):
        return pyautogui.position()
        
    def click(self):
        pyautogui.click()

    def __get_resolution(self):
        return pyautogui.size()
    
    def set_resolution(self):
        self.res_x, self.res_y = self.__get_resolution()
    
    def move_to(self, x, y):
        #Moves to specific co-ords
        pyautogui.moveTo(x, y)

    def move(self, x_offset, y_offset):
        #Moves relative to currently set position
        pyautogui.moveRel(x_offset, y_offset)

    def take_break(self, break_interval):
        # pause for a random amount of time within the range of break_interval
        break_time = random.uniform(break_interval[0], break_interval[1])
        print("Taking a break for {} seconds".format(break_time))
        time.sleep(break_time)


    def pause_skewed(self, skew,mean, min_value=0.5):
        """Pause for a random amount of time based on a right-skewed distribution.

        Parameters:
        right_skew (float): Skewness of the distribution, where a higher value corresponds to a more right-skewed distribution. Default is 2.
        mean (float): Mean value of the distribution. Default is 5.
        std (float): Standard deviation of the distribution. Default is 1.
        min_value (float): Minimum value of the pause duration. Default is 0.5, 10% variation is added around this number.

        Returns:
        None
        """

        print("running right skewed waiting time")
        min_value = min_value + random.uniform(-0.1, 0.1) * min_value
        # Generate a random value from a right-skewed distribution
        value = abs(skewnorm.rvs(a = skew, scale = mean))
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
        print("Wiggling mouse")
        # Generate random offsets
        x = random.randint(-x_offset, x_offset)
        y = random.randint(-y_offset, y_offset)
        # Move the mouse cursor
        self.move(x, y)

    def random_move(self):
        """Move the mouse cursor to a random location on the screen.

        Parameters:
        None

        Returns:
        None
        """
        # Get the screen resolution
        
        # Generate random x and y coordinates - not including whole screen as there is a click
        # This click means that you could open a program on your taskbar if set to the whole screen
        x = random.randint(self.res_x/4, 5/6*self.res_y)
        y = random.randint(self.res_x/4, 5/6*self.res_y)
        # Move the mouse cursor
        print("Moving mouse to {}, {}".format(x, y))
        self.move_to(x, y)

    def run(self):
        start_time = time.time()
        self.set_resolution()
        self.set_position()
        self.take_break([10,12])
        while time.time() - start_time < self.run_time:

            if self.run_type == "wiggle":
                
                self.random_move()
                self.take_break([30, 300])
            elif self.run_type == "click":
                rnd = random.randint(0, 100)
                print(rnd)
            
                if rnd < 3:
                    self.mouse_wiggle(5,5)
                    self.pause_skewed(self.right_skew, self.mean, self.min_value)
                elif rnd == 3:
                    self.pause_skewed(10, 12, self.min_value)
                elif rnd < 30:
                    self.take_break([0.3, 1])
                else:
                    self.pause_skewed(self.right_skew, self.mean,  self.min_value)

                current_x, current_y = self.get_position()
                if abs(current_x - self.x) > 5 or abs(current_y - self.y) > 5:
                    self.move_to(self.x, self.y)
                    

            self.click() # Both methods need a click to work

        print("The Mouse Mover has finished running, thank you for using it!")
                    


                

