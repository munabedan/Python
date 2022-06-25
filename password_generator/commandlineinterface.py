# Reset
#Color_Off='\033[0m'       # Text Reset

# Regular Colors
#Black='\033[0;30m'        # Black
#Red='\033[0;31m'          # Red
#Green='\033[0;32m'        # Green
#Yellow='\033[0;33m'       # Yellow
#Blue='\033[0;34m'         # Blue
#Purple='\033[0;35m'       # Purple
#Cyan='\033[0;36m'         # Cyan
#White='\033[0;37m'        # White  



class Commandlineinterface:

    def __init__(self) -> None:

        pass

    def read_command():
        pass

    def invoke_action():
        pass

    
import sys
from datetime import datetime
import time
import password as p


class Commandlineinterface(Commandlineinterface):

    def __init__(self) -> None:
        pass


    def read_command(self):

        cli_arguments = sys.argv

        self.__interpret_command(cli_arguments)



    def __interpret_command(self,cli_arguments):

        match cli_arguments:
            case ["main.py"]:
                print("matched main.py")

            case ["main.py","generate"]:

                print(datetime.now().strftime("\033[0;35m[%H:%M:%S]\033[0m"), f"Generating password ...")
                start_time = time.perf_counter_ns()
                duration_time = time.perf_counter_ns() - start_time

                self.__invoke_action(["generate"])
                print(datetime.now().strftime("\033[0;35m[%H:%M:%S]\033[0m"), f"Finished generating after {duration_time // 1000000} ms ")
                
            

    def __invoke_action(self,action):
        match action:
            case ["generate"]:
                
                p.initialise_password()
                output=p.password.generate_password()
                self.__print_output(output)

    def __print_output(self,output):
        print("")
        print("\033[0;33m",output,"\033[0m")
        print("")
        pass

   


