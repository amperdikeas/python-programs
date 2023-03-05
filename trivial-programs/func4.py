# global variable
a = 3
a = 4 
def fn():
    global a
    a = 5
    print(a) # prints 5

fn()
print(a) # prints 5
