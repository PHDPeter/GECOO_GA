#simple GA
#targent is to make a arry that is the same as the targgent, very simple!!
def simple_GA ():
    print "test"
# set starting conditions
#population size
    POPsize = 10
    mutRate = 0.1
    Gen = 100
    startPop = making_pop(POPsize)
#    for i in xrange(0,Gen):      

def making_pop(POPsize):
    import random
    for i in xrange(0,POPsize):
            #intlising the peramters
            pack = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
            T1=[0]*len(pack)
            T2=[0]*len(pack)
            t1=0
            t2=0
            #shuffle the cards
            random.shuffle(pack)
            #randomly sort cards in to to piles (T1 and T2)
            for e in xrange(0,(len(pack))):
                card = pack[e]
                R = random.random()
                if R > 0.5:
                        T1[t1+1] = card
                else:
                        T2[t2+1] = card
            #assinging themto the population
            print i
            Ind(i) = podInd(T1,T2,i,i)
            
            #to test
            popInd(i).displayPop()
            print "test"
            
#print pop[0]

class popInd:
    #should holed all detals on the indivdral in the population
    popCount = 0

    def __init__(self, pile1, pile2, ID, rank):
        self.pile1 = pile1
        self.pile2 = pile2
        self.ID = ID
        self.rank = rank
        popInd.popCount +=1
        
    def displayPop(self):
        print "pile 1:", self.pile1, ", pile 2:", self.pile2
        
        
#running the code from above? this makes no sanes to me?      
simple_GA()