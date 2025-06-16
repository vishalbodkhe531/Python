def evenNo(no):
    for idx in range(2,no+1,2):
        yield idx
    

for no in evenNo(10):
    print(no)