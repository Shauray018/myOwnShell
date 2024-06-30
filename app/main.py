import sys
import os
import shutil

def main():
    # Uncomment this block to pass the first stage
    
    knownUserCommands = ["exit", "echo", "type", "pwd", "cd"]
    PATH = os.environ.get("PATH")

    # Wait for user input
    # os.chdir(path)c
    def iknow():  
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        commandcheck  = command.split(" ")[1:]
        command_parts = command.split(" ")
        base_command = command_parts[0]
        thing = " ".join(commandcheck)
        if command.split(" ")[0] not in knownUserCommands: 
            command_path = shutil.which(base_command)
            if command_path:
                    os.system(command)
                    iknow()
            else:
                print(f"{command}: command not found") 
                iknow()
        elif base_command == "echo": 
            sys.stdout.write(f"{thing}\n")
            iknow()
        elif base_command == "exit":
            if commandcheck != ["0"] : 
                iknow()
        elif base_command == "type" and len(command.split(" ")) > 1: 
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
        elif command == "pwd": 
            sys.stdout.write(f"{os.getcwd()}\n")
            iknow()
        elif base_command == "cd":
            path = commandcheck[0]
            if commandcheck:
                if path == "~":
                        path = os.path.expanduser("~")
                try:
                    os.chdir(path)
                    iknow() 
                except FileNotFoundError:
                    sys.stdout.write(f"cd: {path}: No such file or directory\n")
                    iknow()
            else : 
                os.chdir(os.path.expanduser("~"))
                iknow()
        else :
            iknow()
    iknow()
if __name__ == "__main__":
    main()
