#!/usr/bin/python
#title			:day21.py
#description		:Advent of code day 21
#author			:Mike Jarrett
#date			:20160109
#version		:1
#usage			:python day21.py
#notes			:
#python_version	:2.6.6
#==============================================================================
import itertools 



#cost, damage, armour
dagger = [8, 4, 0]
ssword = [10,5,0]
warhammer  =  [25,     6,       0]
lsword  =  [40,     7,       0]
greataxe   =  [74,     8,       0]
weapons = [dagger, ssword, warhammer, lsword, greataxe]

Leather     = [13,     0    ,   1]
Chainmail   = [31 ,    0   ,    2]
Splintmail  = [53  ,   0  ,     3]
Bandedmail  = [75   ,  0 ,      4]
Platemail  = [102    , 0,       5]
noarmour = [0, 0, 0]
armours = [Leather, Chainmail, Splintmail, Bandedmail, Platemail, noarmour]


Damage1 =[ 25,     1     ,  0]
Damage2 =[ 50 ,    2    ,   0]
Damage3 =[100  ,   3   ,    0]
Defense1 = [   20   ,  0  ,     1]
Defense2 =[  40    , 0 ,      2]
Defense3 =[   80    , 0,       3]
noring1 = [0,0,0]
noring2 = [0,0,0]
rings = [ Damage1, Damage2, Damage3, Defense1, Defense2, Defense3 ,noring1, noring2]
#ring_perms = ptns(rings, 2)
#print ring_perms
mystuffs = []
boss=[103,9,2]


#provide hitpoints, damage given and defense for each player
def fight(mystuff, bossstuff,t=False):
    bossdam = mystuff[1]-bossstuff[2]
    if bossdam < 1: bossdam = 1
    mydam = bossstuff[1]-mystuff[2]
    if mydam < 1: mydam = 1

    myturns = mystuff[0]/mydam
    if mystuff[0]%mydam != 0: myturns += 1
    bossturns = bossstuff[0]/bossdam
    if bossstuff[0]%bossdam != 0: bossturns += 1
    
    if t == True:
        print "me: hitpoints: %d damage: %d armour: %d" % (mystuff[0], mystuff[1], mystuff[2])
        print "bo: hitpoints: %d damage: %d armour: %d" % (bossstuff[0], bossstuff[1], bossstuff[2])
        print myturns, bossturns
    if myturns >= bossturns:
        print "win!"
        return True
    else: 
        return False

def simulate(php, pdmg, parmr):
    b = 103
    while True:
        b -= max(1, pdmg - 2)
        if b <= 0:
            return True
        php -= max(1, 9 - parmr)
        if php <= 0:
            return False



results = []
results2 = []
#choose exactly one weapon
for weapon in weapons:
    
    #choose zero or one armour
    for armour in armours:

        #choose zero, one or two rings
        for ring1,ring2 in itertools.combinations(rings,2):
            
            
            cost = weapon[0]+armour[0]+ring1[0]+ring2[0]
            damage = weapon[1]+armour[1]+ring1[1]+ring2[1]
            defense = weapon[2]+armour[2]+ring1[2]+ring2[2]

            print "-----"
            print "weapon: %d, %d, %d" % (weapon[0], weapon[1], weapon[2])
            print "armour: %d, %d, %d" % (armour[0], armour[1], armour[2])
            print "ring1: %d, %d, %d" % (ring1[0], ring1[1], ring1[2])
            print "ring1: %d, %d, %d" % (ring2[0], ring2[1], ring2[2])
            print cost, damage, defense

            #mystuffs.append((cost, damage, defense))
            #print fight([100,damage,defense],boss)
            
            if fight([100,damage,defense],boss):
            #if simulate(100,damage,defense):
                #print cost
                results.append(cost)
            else:
                results2.append(cost)

print min(results)
print max(results2)
#print 9/2, 13/3, 9%2, 13%3





#boss = [12,7,2]
#mystuffs = [[8,5,5]]
#results=[]
#for me in mystuffs:
#    if fight([100,me[1],me[2]],boss):
#        results.append(me[0])
#print results
#print min(results)

    
#test fight function
#me = [20,7,4]
#bo = boss
#print "me: %dhp, %ddam, %ddef" % (me[0],me[1],me[2])
#print "bo: %dhp, %ddam, %ddef" % (bo[0],bo[1],bo[2])
#print fight(me,bo,True)


