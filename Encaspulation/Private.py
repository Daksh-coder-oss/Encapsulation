#Write a program to create a class with following variables and methods - 
# 1. Private variable named privateVar that contains an integer value 
# 2. Create a private function privMeth that prints a message 
# 3. Create a function hello that prints the value of privateVar 
# 4. Create an object for the class and call all the functions.

class Priv:
    __privateVar=9
    def __privateMeth(self):
        print("This is a private message")
    def Hello(self):
        print(Priv.__privateVar)
obj=Priv()
obj.Hello()
obj.__privateMeth()


