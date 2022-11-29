from user import User

username: str = "ghostiefloor123"
password: str = "floofB00f@11"
new_user = User(username, password)

new_user.greet()


class Admin(User):
    pass


bossman = Admin("Bossman", "bossmanPasswordStuff")
bossman.greet()
