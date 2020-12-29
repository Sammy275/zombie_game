import random
import time

class Character:
    health = 100
    def __init__(self, character_type):
        self.character_type = character_type

    def check(self):
        return self.health


    def heal(self):
        self.health += 10

    def attack(self, other):
        other.health -= 50

# Zombie Class
# class Zombie(Character):
#     def __init__(self):
#         super().__init__()

#     def attack(self, man):   # Attack method
#         man.health -= 50

# Player Class
# class Player(Character):
#     def __init__(self):
#         super().__init__()

#     def attack(self, zombie):
#         zombie.health -= 50



def zombie_turn(zombie, man):
    zom_decision = random.randint(1, 3) 
    if zom_decision == 1:
        print("Zombie attacked you, you loose some health")
        zombie.attack(man)
    elif zom_decision == 2:
        print("zombie healed itself")
        zombie.heal()
    else:
        print("You are lucky!!! zombie took too much time")
    time.sleep(2)

def player_turn(man, zombie):
    player_guess = random.randint(1, 3)
    player_decision = int(input("Enter your decision between 1 to 3: "))
    if player_decision == player_guess:
        print("You attacked the zombie!!!")
        man.attack(zombie)
    elif player_decision > player_guess:
        print("You drank potion and healed yourself")
        man.heal()
    else:
        print("You took too much time, your turn is skipped :(")
    time.sleep(2)


def health_check(man, zombie):
    if zombie.health <= 0:
        zombie.health = 0
        return 1
    elif man.health <= 0:
        man.health = 0
        return -1
    return 0



# Driver Code
zombie = Character("Zombie")
man = Character("Player")
gameover = False

print("Welcome to the game")
print("In this game you have to kill a zombie which have a health of 100 and you the player also have 100 health")
print("You can perform 3 actions\nAttack\nHeal\nSkip")
print("Enter a number between 1 to 3 and the computer will generate action for you")
print("Lets kill some zombies!!!")
input("Press any key to continue: ")
print("\n\n\n")

while not gameover:
    print(f"\nZombie health: {zombie.check()}\nYour health is: {man.check()}")
    player_turn(man, zombie)
    if health_check(man, zombie) > 0:
        print("\nZombie Died you win!!!")
        break
    zombie_turn(zombie, man)
    if health_check(man, zombie) < 0:
        print("\nYou died, Zombie wins :(")
        break
time.sleep(2)
print("\nMatch remnants")
print(f"Your health after the match: {man.check()}\nZombie health after the match: {zombie.check()}")
time.sleep(2)