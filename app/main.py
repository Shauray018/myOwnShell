import sys
import os

def main():
    # Uncomment this block to pass the first stage
    
    knownUserCommands = ["exit", "echo", "type"]
    PATH = os.environ.get("PATH")

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
            sys.stdout.write(f"{thing}\n")
            iknow()
        elif command.split(" ")[0] == "exit":
            if commandcheck != ["0"] : 
                iknow()
        elif command.split(" ")[0] == "type" and len(command.split(" ")) > 1: 
            cmd = command.split(" ")[1]
            cmd_path = None
            paths = PATH.split(":")
            for path in paths:
                if os.path.isfile(f"{path}/{cmd}"):
                    cmd_path = f"{path}/{cmd}"
            
            if cmd in knownUserCommands: 
                sys.stdout.write(f"{thing} is a shell builtin\n")
                iknow()
            elif cmd_path:
                sys.stdout.write(f"{cmd} is {cmd_path}\n")
                iknow()
            else : 
                sys.stdout.write(f"{thing}: not found\n")
                iknow()
        else :
            iknow()
    iknow()
if __name__ == "__main__":
    main()
