
def sumAll(*args):    # for multiple string we can also use **args
    print(sum(args))
    return sum(args)

sumAll(1,2,3)
sumAll(1,2,3,4,5)