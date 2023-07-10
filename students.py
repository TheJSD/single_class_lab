class Student:

    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort

    def talk(self):
        print(self.name + ": I can talk!")

    def say_favourite_language(self, favourite_language):
        print(self.name + ": I love " + favourite_language + "!")

