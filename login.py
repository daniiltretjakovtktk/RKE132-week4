username = input("Sisesta kasutajanimi: ")
password = input("Sisesta parool: ")

#if username == "user":
#    print("Welcome!")
#else:
#    print("Invalid username.")

# if username == "user" and password == "1234":
#     print("Welcome!")
# else:
#     print("Access denied.")

if username != "user" and password != "1234":
    print("Access denied.")
else:
    print("Welcome!")