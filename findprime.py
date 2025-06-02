def findprime(n):
    for i in range(2,n):
        if(n%i==0):
            n1="n is prime number"
        elif(n<=1):
            return "invalid"
        else:
            return "n isnot prime"
        return n
