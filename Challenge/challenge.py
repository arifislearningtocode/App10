class User:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        print(self.name.upper())
        return self.name.upper()

    def age(self, current_year):
        x = current_year - self.birthyear
        print(x)
        return x


John = User("John", 1999)
John.age(2023)
John.get_name()

