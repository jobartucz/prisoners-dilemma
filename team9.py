####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Keegan' # Only 10 chars displayed.
strategy_name = 'Tit for Tat Method, kinda'
strategy_description = "It starts off with colluding until the opponent betrays,then it betrays because it will continue to read the opponent's history and repeat whatever the last move was that the opponent made"
    
def move(my_history, their_history, my_score, their_score):

    if len(my_history) == 0:
        return "c"

    if their_history[-1] == "b":
        return "b"
    else:
        return "c"
    if not their_history:
        return "c"
    else:
        return "c"
    if my_score > their_score:
        return "b"
    else:
        return "c"
    if my_score < (-100):
        return "b"
    else:
        return "c"
    if "b" in their_history[-5]:
        return "b"
    else:
        return "c"

    if len(their_history) < 180:
        if len(their_history) > 6:
            if "b" not in their_history[:7]:
                 return "c"

    if opponent.defections > 3:
        return "b"
    else:
        return "c"


    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return "c"

    
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
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print ('Test passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             

####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Keegan' # Only 10 chars displayed.
strategy_name = 'Tit for Tat Method'
strategy_description = "It starts off with colluding until the opponent betrays,then it betrays because it will continue to read the opponent's history and repeat whatever the last move was that the opponent made"
    
def move(my_history, their_history, my_score, their_score):

    if len(my_history) == 0:
        return "c"

    if their_history[-1] == "b":
        return "b"
    return "b"
    if not their_history:
        return "c"


    if len(their_history) > (self.tournament_attributes['length'] - 3):
        return "b"

    if len(their_history) < 180:
        if len(their_history) > 6:
            if "b" not in their_history[:7]:
                 return "b"

    if opponent.defections > 3:
        return "b"


    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return "c"

    
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
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print ('Test passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             

