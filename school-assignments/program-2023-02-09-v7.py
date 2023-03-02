g=float(input("How many grades? "))
s=0
for i in range (n+1):
   grades=float(input("How much did you get? "))
   s=s+grades
if s<=10 :
  print("Your average is (s/n) try harder next time!")
elif s>=15:
  print("Your average is (s/n) your getting better!)
else:
  print("Your average is (s/n) good job")

