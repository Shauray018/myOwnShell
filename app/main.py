import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    def commandTaker(): 
        command = input()
        sys.stdout.write(f"{command}: command not found\n")
        commandTaker()
    commandTaker()

if __name__ == "__main__":
    main()
