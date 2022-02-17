import random
print("Here is you're map:")
map = [[11, 12, 13, 14,], [15,16,17,18], [19,20,21,22], [23, 24, 25, 26]]
print(map[0])
print(map[1])
print(map[2])
print(map[3])
treasure = random.randint(11, 26)

guess = int(input("Guess the location of the treasure:"))
for x in range(16):
    if guess > treasure:
        guess = int(input("That's too high! Guess again:"))
    elif guess < treasure:
        guess = int(input("That's too low! Guess again:"))

print('Correct you found the treasure! Well Done! Restart to play again.')