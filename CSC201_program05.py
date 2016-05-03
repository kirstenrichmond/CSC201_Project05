#Kirsten Richmond
#April 18th, 2016
#Program 05

class Treasure(object):  #Parent class

    def __init__(self, name, description, type_of_treasure, value):
        #describing the type of object
        self.name = name #name of object
        self.description = description #description of object
        self.type_of_treasure = type_of_treasure #type of treasure
        self.value = value #value of treasure

   

class Armor(Treasure): #armor subclass of treasure class
    def __init__(self, type_of_armor, value, defense):
        self.type_of_treasure = "Armor"
        self.type_of_armor = type_of_armor
        self.value = value #price of armor in gold coin
        self.defense = defense #protects against 10 % damage

class Helmet(Armor): # Subclass of armor
    def __init__(self):
        self.value = 50 #price of the helmet
        self.name = "Helmet" #name of the helmet
        self.defense = 10 #will protect 10 percent of damage
        self.description = "A great way to protect your head from damage"

class Weapon(Treasure): #weapon subclass of treasure class
    def __init__(self, damage, attack_level, wielded):
        self.damage = amount of damage #how much damage the weapon does
   
        
class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist sized rock, suitable for bludgeoning"
        self.value = 0 #rock does not cost any money to own
        self.damage = 5 #does 10% damage on prey
            
class Dagger(Weapon)
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust. Useful at close range"
        self.value = 10 #A dagger is worth 10 gold
        self.damage = 10

     def use_weapon:
         choice = input("Which weapon would you like to use?")
         if choice = "Dagger":
             self.money -=10
             print ("You now have" self.money "gold left.") #Choosing to have this weapon
             #will take 10 of the player's gold
             self.experience +=5 #when a player chooses a weapon their experience goes up
         

    
class Food(Treasure): #food subclass of treasure class
    def __init__(self, nutrition):
        self.nutrition = nutrition #nutrition value of the object
    class Apple(Food): #type of food
        self.name = "Apple"
        self.description = "A healthy treat that will keep the doctor away"
        self.nutrition = 15
        input("Would you like to have an apple? Y/N"):
            if "Y":
                self.health += 15 #asks player if they want to eat an apple and adds to health
            if "N":
                return ("You are not very healthy")
    


class Gold(Treasure): #gold subclass of treasure class
    def __init__(self, amt):
        self.type_of_treasure = "Gold"
        self.amt = amt #amount that the gold is worth
        self.money +=amt 
        


class Player(object): #A player for the game
    def __init__(self, experience, health, money, position):
        self.name = "Player"
        self.experience = 0 #has 0 experience when first starting the game
        self.health = 100 #has full health when starting the game
        self.money = 100 #player starts the game with 100 gold coins
        self.position = position #where the player is in the game
    def eating(self): #eating food will give extra help to player
        self.health +=1 #health will go up 1 point if eating
        if eating =>5:
            self.health -= 1
            print ("I'm stuffed") #Player has eaten too much food and lost health
        if health == 100:
            self.health = 100 #Player's health cannot go above 100%
    if health == 0:
        print ("You are dead") #If player has no health they are dead
    
        
    def position(self):
        if self.experience = 0:
            self.position = "middle of map" #starting point of the player is
            #in the middle of the map
            print ("You have started the game in the middle of the map")
         if self.health <= 50:
             self.position = "under a tree" #the player is positioned under a tree
                # for protection
         if self.health <= 99 >= 51:
             self.position = behind a bush #the player will be behind a bush 
    

    def equip(self): #this wiil allow the player to use the weapon of choice
        input ("Which object would you like to carry"):
            if "Dagger":
                
        
    def drop(location)
    def wear()
    def remove()
