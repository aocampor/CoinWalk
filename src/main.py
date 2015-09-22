import random
from datetime import datetime

def TossCoin():
    num = random.uniform(0,1)
    if num > 0.5:
        return True
    else:
        return False

def CombCoeff(trials, tims):
    #n!/k!(n-k)!
    if(tims > trials):
        return 0
    elif( trials == 0 ):
        return 1
    mi = tims
    ma = trials - tims
    if (trials -tims < tims):
        mi = trials -tims
        ma = tims
    num = 1
    den = 1    
    for i in range(ma+1, trials + 1):
        num = num * i
    for i in range(1, mi + 1):
        den = den * i
    return num/den            

def distance(decision, toss):
    if( decision == False and toss == False):
        return 2
    elif( decision == False and toss == True):
        return 3.4142
    elif( decision == True and toss == False):
        return 2.114
    elif(decision == True and toss == True):
        return 3.121

if __name__ == "__main__":
    startTime = datetime.now()
    mean = 0
    for i in range(0,10000):
        tosses = {1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False, 9:False, 10:False}
        totaldis = 0
        prev = False
        for it in range(1,11):
            dec = True
            if(it > 4):
                if(tosses[it - 2] == tosses[it - 1] and tosses[it-3] == tosses[it-1] and tosses[it-4] == tosses[it-1]):
                    dec = not tosses[it - 1]
                
            tosses[it] = TossCoin()
            totaldis = totaldis + distance(dec, tosses[it])
        mean = mean + totaldis
        print totaldis
        
    endTime = datetime.now()
    print mean/10000
    print 'It took ' + str(endTime - startTime)    
        
    
    