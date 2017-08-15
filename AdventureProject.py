
# A life or Death decision
def man1():
    man = raw_input('>')
    if man == "1":
        print 'you failed to sneak up on him' 
        print 'what do you do now'
        print '4 do you tackle him'
        print '5 do you run away'
        man2()
    if man == "2": 
        print 'you successfully fled without him noticing you'
    if man == "3": 
        print 'you go back in the house'
        print 'do you escape through the window on the right or the door on the left?'
   
        
def man2():
    man = raw_input('>')
    if man == "4":
        print 'you tackle the man and run away'
        print 'you escape safely'
    if man == "5":
        print 'you run away'
        print 'you run faster than him and escape safely'
  

person = raw_input('Enter name?')
print 'welcome', person,'!'
print 'You wake up in an empty room, do you want to escape through the window on the right or the door on the left?'

direction = raw_input('left or right>')

if direction == "left":
    print 'You leave through the house through the door and see a man outside looking away from you.'
    print 'make a decision'
    print '1 do you want to sneak up and knock him out'
    print '2 do you want to sneak past him'
    print '3 do you want to go back in the house and leave through the window'
    man1()


if direction == "right":
    print 'you escaped through the window and see a bear eating and a weapon leaning on a tree'
    print '8 do you grab the gun and shoot the bear'
    print '9 do you climb the tree and hide until the bear leaves'

    bear = raw_input('>')
    if bear == "8":
        print 'you grab the gun and kill the bear'
        print 'you escape safely' 
    if bear == "9":
        print 'you climb the tree without the bear noticing '
        print 'you fall asleep in the tree'
        print 'you wake up and the bear is gone'
        print 'you jump down the tree and escape safely'
    man2()    
        
        
        
        
        
        
        
        
        
        
        



















    
    
    
    
    