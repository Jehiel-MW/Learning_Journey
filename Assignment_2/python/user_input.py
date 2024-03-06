name = input("What is your name: ")
age = int(input("How old are you: "))
location = input("Where are you from: ")   
print("""\nHello {}, welcome to the league
Your age next year is {} and you are from {}""".format(name, age + 1, location))
