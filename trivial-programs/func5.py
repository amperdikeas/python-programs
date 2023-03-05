# global variable
a = 3
print(a)
a = 4
print(a)
def fn():
    global a
    a = 5
    print(a)

print(a)
fn()
print(a)
