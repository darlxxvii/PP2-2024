import random
def play(rnum, v):
    v+=1
    num=int(input())
    if num==rnum:
        print(f"Good job, ", name, "! You guessed my number in ", v," guesses!")
        return end=''
    elif num>rnum:
        print("\nYour guess is too high. \nTake a guess.")
        return play(rnum, v)
    elif num<rnum:
        print("\nYour guess is too low. \nTake a guess.")
        return play(rnum, v)

print("Hello! What is your name?")
name=input()
print(f"\nWell, ", name,", I am thinking of a number between 1 and 20.\nTake a guess.")
rnum=random.randint(1,20)
v=0
print(play(rnum, v))