StinkLog = 'Log'

print("Welcome")
welcome = input("Do you have an acount? y/n: ")
if welcome == "n":
    while True:
        username  = input("Enter a username:")
        password  = input("Enter a password:")
        password1 = input("Confirm password:")
        if password == password1:
            file = open(StinkLog+".txt", "w")
            file.write(username+":"+password)
            file.close()
            welcome = "y"
            break
        print("Passwords do not match!")
if welcome == "y":
    while True:
        login1 = input("Login:")
        login2 = input("Password:")
        file = open(StinkLog+".txt", "r")
        data   = file.readline()
        file.close()
        if data == login1+":"+login2:
            print("Welcome")
            exec(open("Stink\Main.py").read())
        print('Incorrect username or password.')