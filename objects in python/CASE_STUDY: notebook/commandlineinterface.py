class Commandlineinterface:

    def __init__(self) -> None:

        pass

    def read_command():
        pass

    def invoke_action():
        pass

    
import sys

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

            case ["main.py","list"]:
                print("list all notes")
            
            case ["main.py","create",file]:
                print("create a new note",file)

            case ["main.py","edit",file]:
                print("edit note",file)

            case ["main.py","tag",file]:
                print("create tag",file)
            
        




    def invoke_action(self):
        pass
