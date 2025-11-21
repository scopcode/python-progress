from random import randint

class Dice():
    def __init__(self , sides = 6):
        self.sides = sides
        
    
    def roll_dice(self):
        print(randint(1,self.sides))
        

print("For six sided dice")
six_sided = Dice()
for value in range(1,11):
    six_sided.roll_dice()

print("For 10 sided dice")
ten_sided = Dice(10)
for value in range(1,11):
    ten_sided.roll_dice()

print("For 20 sided dice")
twenty_sided = Dice(20)
for value in range(1,11):
    twenty_sided.roll_dice()
