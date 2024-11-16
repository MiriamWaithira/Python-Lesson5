# Encapsulation is the practice of keeping attributes and methods private to prevent unwanted interference from outside the class

class SecretStash:
    def __init__(self):
        self.__chocolates = 10   #Private attribute

    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("One chocolate taken!")   #Output: One chocolate taken
        else:
            print("No chocolates left")

stash = SecretStash()
stash.take_chocolate()


    # def take_chocolate(self):
    #     if self.__chocolates > 10:
    #         self.__chocolates -= 10
    #         print("One chocolate taken!")
    #     else:
    #         print("No chocolates left") Output: No chocolates left