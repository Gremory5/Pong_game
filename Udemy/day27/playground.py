
#unlimited positional arguments it collects them in a tuple

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return(sum)

print(add(1000,2,3))

def calculate(n, **kwargs):    #keyword arguments 
    print(kwargs)
#    for key,value in kwargs.items():
#        print(key)
#        print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(2, add=3,multiply=5)

