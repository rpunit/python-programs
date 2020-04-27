import time
def prime_exponents(n,primes):
    exponents = []
    x = n
    p = 2
    while x != 1:
        if primes[p]:
            tally = 0
            while x%p ==0:
                x = x//p
                tally += 1
            exponents += [tally]
        p+=1
    while len(exponents) < len(primes):
        exponents += [0]
    return exponents

def eratosthenes (limit):
    primes = (limit+1)*[True]
    primes[0] = primes[1] = False
    primelist = []
    p = 2
    while p <= limit:
        if primes[p]:
            primelist += [p]
            q = p
            while p*q <= limit:
                primes[p*q] = False
                q += 1
        p+=1
    return primes,primelist

def C(n):
    import math
    primes, primelist= eratosthenes(n)
    prevcalls = {}
    exponents = prime_exponents(math.factorial(n),primes)
    print (recurse(primes,primelist,1,1,0,exponents,prevcalls)//2)

def gcd(a,b):
    while b != 0:
        t = a%b
        a = b
        b = t
    return a

def recurse (primes,primelist,adivs,bdivs,prime_index,exponents,prevcalls):
    if (adivs,bdivs,prime_index) in prevcalls:
        return prevcalls[(adivs,bdivs,prime_index)]
    if prime_index == len(exponents) and adivs == bdivs:
        prevcalls [(adivs,bdivs,prime_index)] = 1
        return 1
    elif prime_index == len(exponents):
        prevcalls [(adivs,bdivs,prime_index)] = 0
        return 0
    aexps = prime_exponents(adivs,primes)
    bexps = prime_exponents(bdivs,primes)
    for i in range (len(aexps)):
        if bexps[i] != 0:
            candidate = primelist[i]
            if candidate > exponents[prime_index]+1:
                prevcalls [(adivs,bdivs,prime_index)] = 0
                return 0
        if aexps[i] != 0:
            candidate = primelist[i]
            if candidate > exponents[prime_index]+1:
                prevcalls [(adivs,bdivs,prime_index)] = 0
                return 0
    tally = 0
    for j in range (exponents[prime_index]+1):
        next_adivs = adivs*(j+1)
        next_bdivs = bdivs*(exponents[prime_index]-j+1)
        g = gcd(next_adivs,next_bdivs)
        tally += recurse(primes,primelist,next_adivs//g,
                         next_bdivs//g,prime_index+1,exponents,prevcalls)
    prevcalls [(adivs,bdivs,prime_index)] = tally
    return tally

start_time = time.clock()
C(100)
finish_time = time.clock()
print (finish_time - start_time)
