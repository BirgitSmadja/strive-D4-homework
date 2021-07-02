def strive_school():
    x = input('Are you a Strive School student?\n').lower()
    if x == 'yes':
        print('Your are not getting enough sleep!')
    elif x == 'no':
        print("You're getting plenty of sleep!")

strive_school()