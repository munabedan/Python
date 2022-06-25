from passwordgenerator import pwgenerator

class Password():


    def __init__(self):
        pass


class Password(Password):

    def __init__(self):
        super().__init__()
        pass

    def generate_password(self):
        return pwgenerator.generate()

password = None

def initialise_password():
    global password
    password = Password()

        
        

