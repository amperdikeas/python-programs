from random import randint
x=randint(0,10)
print('x='+str(x))
if (x<3):
  print("very small")
else:
  if (x>=3 and x<5):
    print("small")
  else:
    if (x>=5 and x<7):
      print("large")
    else:
      print("very great")
