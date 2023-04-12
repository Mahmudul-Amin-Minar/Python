import os
import time
from cryptography.fernet import Fernet


# class CredentialDetails:
#     def __init__(self, *args, **kwargs):
#         self.username = kwargs['username']
#         self.password = kwargs['password']
#         self.url = kwargs['url']

#     def __repr__(self) -> str:
#         return f"Username: {self.username}\nPassword: {self.password}\nURL: {self.url}\n----------\n"

def clear_screen():
    os.system('cls')

def encrypt_password(password):
    secret_key = b"9W0oIzqUc46l5G9IQlBlWk0dGrvPt6yGbLzAn-zcu2o="
    f = Fernet(secret_key)
    # convert byte string to encrypted password 
    enc_password = f.encrypt(password.encode())
    # return encrypted password and convert it from byte to normal string 
    return enc_password.decode()

def decrypt_password(password):
    secret_key = b"9W0oIzqUc46l5G9IQlBlWk0dGrvPt6yGbLzAn-zcu2o="
    f = Fernet(secret_key)
    dec_password = f.decrypt(password.encode())
    return dec_password.decode()


def add_credentials():
    clear_screen()
    print("""
            (1) Add credentials and related resources (username, password and URL/resource).\n
    """)
    username = input("username: ")
    password = input("password: ")
    url = input("URL: ")
    password = encrypt_password(password)

    with open('information.txt', 'a', encoding = 'utf-8') as file:
        file.write('username: ' + username + '\n')
        file.write('password: ' + password + '\n')
        file.write('URL: ' + url + '\n')
        file.write('----------\n')
    clear_screen()
    time.sleep(2.0)
    print("record saved successfully...")
    time.sleep(2.0)

def view_credentials():
    clear_screen()
    print("""
            (2) View stored credentials.\n
    """)
    with open('information.txt', 'r', encoding = 'utf-8') as file:
        file_str = file.read()

    list_ = file_str.split('----------')
    
    for i in list_:
        credential = i.split('\n')
        credential = [x for x in credential if x]
        if len(credential) > 1:
            username = credential[0][10:]
            password = credential[1][10:]
            url = credential[2][5:]

            print("Username: ", username)
            print("Password: ", decrypt_password(password))
            print("URL: ", url)
            print("----------")
            
    input("Press ENTER to return to main menu")


def help():
    clear_screen()
    print("""
            (3) How to Use it.\n
            To use it users have to choose one option from the menu by pressing the\n
            1,2,3,4 keys in the keyboard. Depending on the choice users can perform
            different task.\n If user select 1 then in next step user have to enter their\n
            username, password and url in the command prompt. Upon successful operation a success message will be shown.
    """)
    input("Press ENTER to return to main menu")

def main_menu():
    while(True):
        clear_screen()
        print("""\n\n\n =====Please Select your choice. Enter corresponding number.=====\n
                (1) Add credentials and related resources (username, password and URL/resource).\n
                (2) View stored credentials.\n
                (3) How to Use it.\n
                (4) Exit.
        """)
        choice = int(input())

        if choice is 1:
            add_credentials()
        elif choice is 2:
            view_credentials()
        elif choice is 3:
            help()
        elif choice is 4:
            clear_screen()
            # time.sleep(2)
            print("Thanks")
            # time.sleep(2)
            break


if __name__ == "__main__":
    main_menu()
