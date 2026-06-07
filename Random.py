import random # imports the random module, which provides functions for generating random numbers and making random choices. 

# print(help(random))

low = 1
high = 50
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low, high)
# number = random.random()
# option = random.choice(options)
random.shuffle(cards)

print(cards)