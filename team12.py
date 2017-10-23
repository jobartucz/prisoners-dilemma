####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Silas' # Only 10 chars displayed.
strategy_name = 'Russian Relations'
strategy_description = 'Collude, but once betrayed, never collude again'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if 'b' in their_history:
        return 'b'
    else:
        return 'c'
    # Theoretically, as long as someone adopts a similar strategy, this should be a winning strategy.
    # I did not go through the thought process entirely by myself; I watched a video titled "Evolution of Trust"
    # quite a while ago, and managed to remember the (mostly) winning strategy. 


    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # my_history, my_score, their_score are all placeholders for arguments, my code doesn't actually look at them
    # Test 1: collude first turn
    if test_move(my_history='',
                 my_score=0,
                 their_score=0,
                 their_history='', 
                 result='c'):
         print ('Test 1 passed')
     # Test 2: Continue Colluding
    if test_move(my_history='',
                 my_score=0,
                 their_score=0,
                 their_history='c',
                 result='c'):
        print ('Test 2 passed')
    # Test 3: Betray after one betrayal
    if test_move(my_history='',
                 my_score=0,
                 their_score=0,
                 their_history='b',
                 result='b'):
        print ('Test 3 passed')
    # Test 4: Keep betraying
    if test_move(my_history='',
                 my_score=0,
                 their_score=0,
                 their_history='ccbcc',
                 result='b'):
        print('Test 4 passed')
    # Test 5: Make sure tests work
    if test_move(my_history='',
                 my_score=0,
                 their_score=0,
                 their_history='ccbcc',
                 result='c'):
        print("The tests don't work")
    else:
        print('Ignore that mumbo jumbo. Test 5 passed :)')