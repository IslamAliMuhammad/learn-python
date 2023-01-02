from cryptography.fernet import Fernet

# def store_key():
#     with open("key.key", "wb") as file:
#         key = Fernet.generate_key()
#         file.write(key)
    
# store_key()

def get_key():
    key_file = open("key.key", "rb")
    key = key_file.read()
    key_file.close()
    
    return key
    
def view():
    f = open("passwords.txt", "r")
       
    key = get_key()

    fer = Fernet(key)
    
    for line in f.readlines():
        data = line.rstrip()
        account, password = data.split("|")
        print("Account: ", account, "|", "Password: ", fer.decrypt(password).decode())
        
    f.close()
        
def add():
    account = input("Enter your account: ")
    password = input("Enter your password: ")
  
    key = get_key()
    
    f = Fernet(key)

    password_encrypted = f.encrypt(password.encode())
      
    f = open("passwords.txt", "a")
    f.write(account + "|" + password_encrypted.decode() + "\n")
    f.close()

while True:
    mode = input("Would you like to add a new passowrd or view existing ones (view, add), press q to quit? ").lower()
    
    if mode == "q":
        quit()
        
    elif mode == "view":
        view()
        continue
    
    elif mode == "add":
        add()
        
    else:
        print("Invalid mode.")

