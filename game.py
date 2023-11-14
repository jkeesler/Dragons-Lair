import random

class Dragon:
    
    def __init__(self):
        self.rage_counters = 0
        self.life = 100
        self.whelps = 0
        self.kobolds = 0
        self.whelps_tapped = 0
        self.enraged = False
        
    def increase_rage(self, counter):
        self.rage_counters += counter
        
    def decrease_rage(self, counter):
        self.rage_counters -= counter
        
    def decrease_life(self, amount):
        self.life -= amount
        
    def gather(self):
        self.whelps += 1
        self.kobolds += 1
        
    def hatch(self):
        amount = self.roll()
        self.whelps += amount
        return amount
        
    def stats(self):
        print('Rage Counters: ', self.rage_counters)
        print('Life: ', self.life)
        print('Whelps: ', self.whelps)
        print('Tapped Whelps: ', self.whelps_tapped)
        print('Kobolds: ', self.kobolds)
        
    def roll(self):
        return random.randint(1,6)

    



dragon = Dragon()




#####
#
#
#   UNENRAGED
#
#
#####
while dragon.life > 0:
    if not dragon.enraged:
        #Step 1: Lash Out
        print("Lash Out")
        print("The lair deals ", dragon.rage_counters, "damage to you\n")
        
        #Step 2: Combat
        print('Combat')
        damage = 0
        if dragon.whelps >= 1:
            if dragon.kobolds == 0:
                damage = dragon.whelps
            else:
                damage = dragon.whelps * dragon.kobolds
            dragon.whelps_tapped = dragon.whelps
            dragon.whelps = 0
            
        print(dragon.whelps, "Dragon Whelps hit you for", damage, "Damage\n")
            
        #Step 3: Gather
        print("Gathering Forces\n")
        dragon.gather()
        
        #Step 4: Misfortune
        print('Misfortune Befalls You')
        r1 = dragon.roll()
        if r1 == 1:
            dragon.increase_rage(1)
            print("The lair deals ", dragon.rage_counters, "damage to you\n")
        elif r1 == 2:
            dragon.increase_rage(2)
            print("The lair deals ", dragon.rage_counters, "damage to you\n")
        elif r1 == 3:
            print("There is a cave in, sacrifice a creature\n")
        elif r1 == 4 or r1 == 5:
            hatch = dragon.hatch()
            print(hatch, "Whelps Hatch\n")
        else:
            print('You run into Magma, lose 5 life or sacrifice a creature\n')
            
        #Step 5: Enrage
        if dragon.roll()+dragon.roll() < dragon.rage_counters:
            print('RAGE')
            dragon.enraged = True
            break
    
        
        dragon.stats()
        decrease = int(input())
        dragon.decrease_life(decrease)
    if dragon.enraged:
        break