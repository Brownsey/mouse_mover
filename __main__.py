from classes.autoclicker import AutoClicker
import sys

def main():
    # runs the parameters for the data challenge when this .py is called
    #run_type = sys.argv[1]
    #run_time = int(sys.argv[2])
    #right_skew = int(sys.argv[3])
    #mean = int(sys.argv[4])
    #std = int(sys.argv[5])
    #min_value = int(sys.argv[6])
    # create an instance of the autoclicker class
    autoclicker = AutoClicker(run_type="click")
    # start the autoclicker
    autoclicker.run()




if __name__ == "__main__":
    # runs the parameters for the data challenge when this .py is called
    print("running main")
    main()
