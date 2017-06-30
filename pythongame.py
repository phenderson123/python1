
import sys
import random

ans = True

while ans:
    question = raw_input("Ask 8 ball a question: (press enter to stop) ")
    
    answers = random.randint(1,8)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print "It is going to happen"
    
    elif answers == 2:
        print "Looking good dude"
    
    elif answers == 3:
        print "Yeah bro"
    
    elif answers == 4:
        print "Later dude"
    
    elif answers == 5:
        print "No, it cloudy"
    
    elif answers == 6:
        print "Really man"
    
    elif answers == 7:
        print "Naw, aint happining"
    
    elif answers == 8:
        print "hell no bro"