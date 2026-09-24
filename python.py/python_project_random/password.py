users = {
    "kundan": "kundan123@",
    "admin": "12345"

}
attempts = 3

while attempts > 0:

   username = input("enter username: ")
   password = input("enter password: ")

   if username in users and users[username] == password:

     print("\nlogin successful! ")
     print("welcome to the system", username)

     break

   else:

      attempts -= 1

      print("Invalid username or password !")

      print("Attempts remaining:",attempts)

      if attempts== 0:

        print("\n sorry Account temporarily locked!")
