import sys


def main():
    # Uncomment this block to pass the first stage
    
    knownUserCommands = []

    # Wait for user input
    

    def iknow():  
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        if command not in knownUserCommands: 
            sys.stdout.write(f"{command}: command not found\n")
            iknow() 

    iknow()

        
    

if __name__ == "__main__":
    main()
