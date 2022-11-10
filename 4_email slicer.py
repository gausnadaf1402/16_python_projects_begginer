def main():
    print("Welcome to email slicer")
    print("")

    email_input=input("input your email: ")

    (username,domain)=email_input.split("@")
    (domain,extension)=domain.split(".")

    print("username : ", username)
    print("domain : ", domain)
    print("extension : ", extension)

while True:
   main()