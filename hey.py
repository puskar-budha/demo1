print("ram ram ram")
import numpy as np
from numpy import random
ran=random.randint(1,100,size=(3,5))
print(ran)
arr1=np.array([3,6,8,9])
arr2=np.array([4,9,2,3])
new=np.sum([arr1,arr2],axis=1)
p=np.prod([arr1,arr2],axis=1)
print(new)
print(p)
lcm=np.lcm.reduce(arr1)
print(lcm)
gcd=np.gcd.reduce(arr2)
print(gcd)
print("welcome to scissors,paper and rock game !")
print("take a guess.")
while True:
    choices=["scissors","paper","rock"]
    guess=input("enter scissors or paper or rock or(quit to exit game):").lower()
    if guess=="quit":
        break
    if guess not in choices:
        print("sorry it's not valid try again...")
        continue
    ai=random.choice(choices)
    print(f"ai choose {ai}")
    if(ai==guess):
        print("it's tie.Try again.")
    elif (ai=="scissors" and guess=="rock")or\
       (ai=="paper" and guess=="scissors")or\
       (ai=="rock" and guess=="paper"):
          print("congrats! you win")
    else:
        print("ai win.") 