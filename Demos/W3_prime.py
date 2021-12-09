
def isPrime(n):
    for thing in range(2, n):
        if n % thing == 0:
            return False
    return True


#print(isPrime(88)) = example, when Run, it gives false because it's not prime number

def findPrime(s, e):
    for i in range(s, e):
        if isPrime(i):
            return i

#print(findPrime(1000, 2200))

def encrypt():
    x = int(input("Provide a starting point: "))
    y = int(input("Provide an end point: "))
    p1 = findPrime(x,y)
    x = int(input("Provide a starting point: "))
    y = int(input("Provide an end point: "))
    p2 = findPrime(x,y)
    return p1*p2

print(encrypt())