"""
 ________  _______   _______  _________  ___       _______   ________      
|\   __  \|\  ___ \ |\  ___ \|\___   ___\\  \     |\  ___ \ |\   ____\     
\ \  \|\ /\ \   __/|\ \   __/\|___ \  \_\ \  \    \ \   __/|\ \  \___|_    
 \ \   __  \ \  \_|/_\ \  \_|/__  \ \  \ \ \  \    \ \  \_|/_\ \_____  \   
  \ \  \|\  \ \  \_|\ \ \  \_|\ \  \ \  \ \ \  \____\ \  \_|\ \|____|\  \  
   \ \_______\ \_______\ \_______\  \ \__\ \ \_______\ \_______\____\_\  \ 
    \|_______|\|_______|\|_______|   \|__|  \|_______|\|_______|\_________\
                                                                \|________|
"""

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def eggs(f,m):
    '''f is female bettles, m is male beetles. this function is to calculate how many eggs and pupae you will end up with
    '''
    msg=''

    if f<m:
        msg+='Release {} of the males.\n'.format(m-f)
    elif m<f:
        msg+='Keep the females and put an even amount with each male.\n'
    elif m==f:
        msg+='Pair up the beetles evenly within their own enclosure for a week with food and water.\n'
        
    msg+='There will be {} to {} amount of eggs, in total, in 1 to 5 days.\n'.format(f*5, f*10)
    msg+="There will be a loss of {} to {} larvae and eggs once they reach pupation.".format(f*5*.80, f*10*.96)

    return msg


for i in (50, 60, 70, 80, 90, 100)
    


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(eggs(60,70) == 'Release 10 of the males.\nThere will be 300 to 600 amount of eggs, in total, in 1 to 5 days.\nThere will be a loss of 240.0 to 576.0 larvae and eggs once they reach pupation.')
    test(eggs(60,80) == 'Release 20 of the males.\nThere will be 300 to 600 amount of eggs, in total, in 1 to 5 days.\nThere will be a loss of 240.0 to 576.0 larvae and eggs once they reach pupation.')
    test(eggs(70,70) == 'Pair up the beetles evenly within their own enclosure for a week with food and water.\nThere will be 350 to 700 amount of eggs, in total, in 1 to 5 days.\nThere will be a loss of 280.0 to 672.0 larvae and eggs once they reach pupation.')
    test(eggs(70,50) == 'Keep the females and put an even amount with each male.\nThere will be 350 to 700 amount of eggs, in total, in 1 to 5 days.\nThere will be a loss of 280.0 to 672.0 larvae and eggs once they reach pupation.')
    test(eggs(60,173) == 'Release 113 of the males.\nThere will be 300 to 600 amount of eggs, in total, in 1 to 5 days.\nThere will be a loss of 240.0 to 576.0 larvae and eggs once they reach pupation.')

test_suite()




f=int(input("How many were female?"))
m=int(input("How many were male?"))

print(eggs(f,m))

