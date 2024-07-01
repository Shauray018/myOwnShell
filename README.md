# Simple Shell Emulator

This is a simple shell emulator implemented in Python. It supports a few basic shell commands including `exit`, `echo`, `type`, `pwd`, and `cd`.

## Features

- **exit**: Exit the shell. The command `exit 0` will successfully exit the shell.
- **echo**: Print the provided arguments to the standard output.
- **type**: Determine if a command is a shell builtin or an external command.
- **pwd**: Print the current working directory.
- **cd**: Change the current working directory. Supports the `~` symbol to navigate to the home directory.

## Requirements

- Python 3.x
- An operating system that supports the standard Unix-like shell commands.

## Usage

1. Clone the repository or download the script file.
2. Ensure you have Python 3.x installed on your system.
3. Run the script using the following command:

    ```bash
    python3 shell_emulator.py
    ```

4. You will see a prompt that looks like this:

    ```bash
    $
    ```

5. Enter your commands after the prompt.

### Example Commands

- **exit**:
    ```bash
    $ exit 0
    ```

- **echo**:
    ```bash
    $ echo Hello, World!
    Hello, World!
    ```

- **type**:
    ```bash
    $ type cd
    cd is a shell builtin
    ```

- **pwd**:
    ```bash
    $ pwd
    /current/working/directory
    ```

- **cd**:
    ```bash
    $ cd /path/to/directory
    ```

    ```bash
    $ cd ~
    ```

## Code Explanation

The main function initializes the known shell commands and sets up the environment path. It defines a helper function `iknow` which is responsible for handling the user input and executing the corresponding commands.

### Known Commands

- **exit**: Exits the shell if the provided argument is `0`.
- **echo**: Prints the arguments to the standard output.
- **type**: Checks if the command is a shell builtin or an external command and prints the appropriate message.
- **pwd**: Prints the current working directory.
- **cd**: Changes the directory to the specified path. Supports `~` for navigating to the home directory.

### Handling Unknown Commands

If a command is not recognized as a known shell command, it checks if it is an executable in the system's PATH and executes it. If the command is not found, it prints an error message.

### Handling `cd` with `~`

The `cd` command supports changing to the home directory by recognizing the `~` symbol and translating it to the home directory path using `os.path.expanduser("~")`.

## Contributing

Feel free to fork this repository, create issues, or submit pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License.
