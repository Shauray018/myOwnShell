import sys


def main():
    # Uncomment this block to pass the first stage
    
    knownUserCommands = ["exit", "echo"]

    # Wait for user input
    

    def iknow():  
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        commandcheck  = command.split(" ")[1:]
        thing = " ".join(commandcheck)
        if command.split(" ")[0] not in knownUserCommands: 
            sys.stdout.write(f"{command}: command not found\n")
            iknow() 
        elif command.split(" ")[0] == "echo": 
            sys.stdout.write(f"{thing} \n")
            iknow()
        elif command.split(" ")[0] == "exit":
            if commandcheck == ["0"] : 
                sys.stdout.write("thanks for checking out")
            else :
                iknow()
        else :
            iknow()
    iknow()
if __name__ == "__main__":
    main()
