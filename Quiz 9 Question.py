import random

# sayings must be a list of sayings
sayings = ['Today will be a wonderful day!',
    'You are going to realize your dreams!',
    'Soon your ideas will be appreciated by others!',
    'Doors are opening because of your hard work!',
    'Your dreams are about to come true.']

count_sayings = len(sayings) - 1

get_saying = True

# enter into a loop while the user wants to continue to play
while get_saying:
    saying_index = random.randint(0, count_sayings)  # get a random index value
    print('\n')
    print('----- Your Saying for Today -----')
    print(sayings[saying_index])  # print the random saying

    print('\n')    
    user_response = input('Would you like another inspirational saying? (y/n) ')

    if user_response == 'n':
        get_saying = False

# print final message as the game play ends.
    print('Thank you for playing, please come again.')
