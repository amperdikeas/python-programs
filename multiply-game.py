from random import *
score=0
N=4
for i in range(N):
   n1= randint(2,10)
   n2= randint(2,10)
   print(n1,n2)
   ans=int(input("How much is their product? "+ str(n1)+'*'+str(n2) + " = "))
   if (ans==n1*n2):
      print("Correct")
      score=score+1
   else:
      print("Try again")
print("score= "+ str(score) +" / "+str(N))
