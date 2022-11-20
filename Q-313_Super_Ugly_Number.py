primes = [2,3,5]
step = 0
uglyNumber = 1
n = 327

def isUgly(n, primes):
    if n == 1:
        return True
    
    for i in primes:
        if n % i == 0:
            while n % i == 0:
                n /= i
                #print(n)
            if n == 1:
                return True
        
    
while True:
    
    if isUgly(uglyNumber, primes):
        step += 1
        print(f"Step is {step}")
        if step == n:
            print(f"Result is: {uglyNumber}")
            break
    
    uglyNumber += 1

            
