class NameXPattern(MagicalPrime):
    def __init__(self, name):
        self.name = name
    
    def display_x_pattern(self):
        length = len(self.name)
        for i in range(length):
            for j in range(length):
                if i == j or j == length - i - 1:
                    print(self.name[j], end='')
                else:
                    print(' ', end='')
            print()

name = input("Enter your name: ")
name_x_pattern = NameXPattern(name)
name_x_pattern.display_x_pattern()
