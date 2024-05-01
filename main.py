weather = input("Is it a snowy day? (yes/no) ")
if weather == "yes":
    print("You change into warm clothes but you arrive late.")
else:
    print('''
You walk to school and arrive a few minutes early.
''')

print('''
You walk into class.
''')
seat = input("Do you want to sit next to your friend? (yes/no) ")
if seat == "yes":
    print("You two sit next to eachother and get some work done.")
else:
    print("Your friend is upset you don't want to sit together but you finish all your work.")

help = input('''
Your friend approaches you for help, do you help?
(yes/no) ''')
if help == "yes":
    print('"thanks!" your friend says.')
else:
    print("Your friend is upset and walks away.")
    
print('''
The next bell rings and you go to lunch.
''')
if seat == "yes" and help == "yes":
    print("Your friend sits with you at lunch.")
else:
    print("You sit by yourself since your friend was upset.")

print('''
The bell rings for the next period.
''')
cheat = input("Oh no, there's a pop quiz! Are you planning to cheat? (yes/no) ")
if cheat == "yes":
    print("Your teaches catches you and gives you a zero.")
else:
    print("Good choice, you got 100%!")

print('''
The final bell rings and school is over.''')
call = input("Will you call your mom for a ride? (yes/no) ")
if call == "yes":
    print("Your mom picks you up but is a bit irritated.")
else:
    print("You walk home.")

