# Namespaces: Local vs. Global Scope

#Scope 
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

"""
Output will be:
enemies inside function: 2
enemies outside function: 1
"""

#Local Scope - Exists within the game
def drink():
    name = "akhil"
    print(name)

drink()
#print(name) #Shows Error (Can't access it outside the scope of the function)

#Global Scope
player_health = 10

def portion():
    name2 = "aa"
    print(player_health)

portion()
# Global scope dont show any error

#Namespace

# There is no Block Scope in Python