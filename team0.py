####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Mr. B' # Only 10 chars displayed.
strategy_name = 'Rubber Chicken'
strategy_description = 'Can\'t tell you yet'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    import random
    if (random.randint(0,100) < 50):
        return 'b'
    else:
        return 'c'
'''