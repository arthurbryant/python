#!/usr/bin/env python

def rsp(player1, player2):
    choices = ('paper', 'rock', 'scissors')
    if(player1 not in choices or player2 not in choices):
        return ""
    if(player1 == 'rock'):
        if(player2 == 'scissors'):
            return "player1 wins"
        elif(player2 == 'paper'):
            return "player2 wins"
    elif(player1 == 'paper'):
        if(player2 == 'scissors'):
            return "player2 wins"
        elif(player2 == 'rock'):
            return "player1 wins"
    else:
        if(player2 == 'rock'):
            return "player2 wins"
        elif(player2 == 'paper'):
            return "player1 wins"
    return "equal";
    '''
while(True):
    print "Player 1?"
    player1 = raw_input()
    if(player1 not in choices):
        print "This is not a valid object section"
        continue
    else:
        break
while(True):
    print "Player 2?"
    player2 = raw_input()
    if(player2 not in choices):
        print "This is not a valid object section"
        continue
    else:
        break
        '''
print rsp('abc', 'rock');
print rsp('paper', 'rock');
print rsp('rock', 'scissors');
print rsp('paper', 'scissors');
print rsp('scissors', 'scissors');

