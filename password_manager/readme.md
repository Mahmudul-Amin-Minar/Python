# Credential Manager

This is a simple credential manager that allows users to store and retrieve their login credentials. The program uses the `cryptography` module to encrypt and decrypt user passwords before storing them in a local file.

## How to Use

To use the program, simply run the `main.py` file in your preferred Python environment. The program will display a main menu with the following options:

1. Add credentials and related resources (username, password and URL/resource)
2. View stored credentials
3. How to use it
4. Exit

Select the corresponding number to perform the desired action.

### Add Credentials

Selecting option 1 will allow you to add your username, password, and URL/resource to the program. The password will be encrypted before being stored. Upon successful completion, the program will display a success message.

### View Stored Credentials

Selecting option 2 will display all stored credentials in the format of username, password, and URL/resource.

### How to Use

Selecting option 3 will provide information on how to use the program.

### Exit

Selecting option 4 will exit the program.

## Code Overview

The main file `main.py` contains the following functions:

- `clear_screen()`: Clears the console screen
- `encrypt_password(password)`: Encrypts the user password using `cryptography` module
- `decrypt_password(password)`: Decrypts the user password using `cryptography` module
- `add_credentials()`: Adds user credentials to the program by accepting input for username, password, and URL/resource
- `view_credentials()`: Displays all stored credentials in the console
- `help()`: Provides information on how to use the program
- `main_menu()`: Displays the main menu and allows users to select an option

The program uses the `Fernet` class from `cryptography.fernet` module to generate the encryption key used for password encryption and decryption.

The user credentials are stored in a local file called `information.txt` in the format of username, password, and URL/resource.

## Dependencies

The program requires the following dependencies:

- `cryptography`

You can install the dependencies using the following command:

`pip install -r requirements.txt`
