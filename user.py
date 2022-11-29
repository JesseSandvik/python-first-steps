class User:
    def __int__(self, username, password):
        self.username = username
        self.password = password

    def greet(self):
        print("Hello, " + self.username + "!")
