class myclass:
    __privatevar=27

    def print(self):
        print("I am in this class")

    def hello(self):
        print("private variable is:",myclass.__privatevar)

vish=myclass()
vish.print()
vish.hello()
