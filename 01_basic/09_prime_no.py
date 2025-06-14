# 1,2,3,5,7

inputNo = int(input("Enter a no. : "))
count = 2
isPrime = True

while count < inputNo:
    if inputNo % count == 0 :
        isPrime = False
        break
    count +=1

print(f"{input} is a prime number" if isPrime else f"{input} is a non-prime number")
