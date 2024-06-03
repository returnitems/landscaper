import random

current_cash = 0
day_count = 0

print('Welcome to Landscaper two point oh!')
user_name = input('Please enter your name: ')
print('Hello ' + user_name + '! Shall we get started?')
start_input = input('Type 1 for yes, 2 for no: ')
start_input = int(start_input)

# Game function
def gameStart():

    def day_start():
        while True:
            day_input = input('Type 1 to work the day, 2 to call out, 3 to quit: ')
            day_input = int(day_input)

            if day_input == 1:
                random_int = random.randint(1, 10)
                current_cash += random_int
                day_count += 1

                print('Congratulations on completing a day of hard labor! Today you made $' + random_int)
                print('Current cash: $' + str(current_cash))
                print('Day: ' + str(day_count))
            elif day_input == 2:
                day_count += 1
                print('You called out today and make no money. Better get to work tomorrow!')
                print('Current cash: $' + str(current_cash))
                print('Day: ' + str(day_count))
            else:
                print('Goodbye!')
    day_start()

if start_input == 2:
    print("That's sad but understandable. Have a good day!")
else:
    print('Great! We will now begin our landscaping journey. Unfortunately, for now we only have our teeth to work with.')
    gameStart()