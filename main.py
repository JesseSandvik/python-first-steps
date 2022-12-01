from user import User

username = "ghostiefloof123"
password = "floofB00f@11"
new_user = User(username, password)

new_user.greet()


class Admin(User):
    def greet(self):
        print("Hello Admin " + self.username + "!")

    def doSomethingBossy(self):
        answer = input(f"Hey, {username}, do you wanna get schwifty? ")
        print("You answered:" + "\n" + answer)

        print("Yeeeeeah, let's get schwifty!")

bossman = Admin("Bossman", "bossmanPasswordStuff")
bossman.greet()

bossman.doSomethingBossy()
