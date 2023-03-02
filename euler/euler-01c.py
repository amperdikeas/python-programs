#   If we list all the natural numbers below 10
#   that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#   The sum of these multiples is 23.
#   Find the sum of all the multiples of 3 or 5 below 1000.""

def is_i_mul_of_3(n):
    if ( i%3 == 0 ):
        return True
    else:
        return False

def is_i_mul_of_5(n):
    if ( i%5 == 0 ):
        return True
    else:
        return False

def is_mul_of_3_or_5(n):
    if  is_i_mul_of_3(i) or is_i_mul_of_5(i):
        return True
    else:
        return False

sum=0
for i in range (1,1000):
    if is_mul_of_3_or_5(i):
        sum=sum+i
print('The answer is:'+str(sum))
