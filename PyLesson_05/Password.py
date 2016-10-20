usernamec = "Hello"
passwordc = "123456"
def passCheck():
    username = input("Please Enter your username: ")
    password = input("Please Enter your password: ")

    if username == usernamec and password == passwordc:
        print("Your are granted access!")
    else:
        if password == passwordc and username != usernamec:
            print("Your username is incorrect!")
            passCheck()
        elif username == usernamec and password != passwordc:
            print("Your password is incorrect!")
            passCheck()
        else:
            print("Your username and password are incorrect!")
            passCheck()
passCheck()



