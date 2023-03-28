from classes.autoclicker import AutoClicker
import sys

def main():

    num_args = len(sys.argv)
    print("num_args: ", num_args)
    if num_args > 1:
        print("running with system args")
        if num_args == 2:
            autoclicker = AutoClicker(run_type=sys.argv[1])
        elif num_args == 3:
            autoclicker = AutoClicker(run_type=sys.argv[1], run_time=sys.argv[2] )
        elif num_args == 4:
            autoclicker = AutoClicker(run_type=sys.argv[1], run_time=sys.argv[2], right_skew=sys.argv[3])
        elif num_args == 5:
            autoclicker = AutoClicker(run_type=sys.argv[1], run_time=sys.argv[2], right_skew=sys.argv[3], mean=sys.argv[4])
        elif num_args == 6:
            autoclicker = AutoClicker(run_type=sys.argv[1], run_time=sys.argv[2], right_skew=sys.argv[3], mean=sys.argv[4], min_value=sys.argv[5])
        else:
            print("too many args")
    else:
        print("running with default parameters")
        autoclicker = AutoClicker()
    # start the autoclicker
    autoclicker.run()




if __name__ == "__main__":
    # runs the parameters for the data challenge when this .py is called
    print("running main")
    main()
