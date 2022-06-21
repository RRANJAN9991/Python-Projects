#This program determines whether a number is prime, the factors of a number, and the prime factorization of a number.
def isprime(n):#This is the first function which determines if a number if prime or not prime. 
    if (n <= 1):#Checks to see if the number is less than or equal to 1. If it is, then the function will return false.
        return False
    for i in range(2,n):#This loop will check the numbers in the range specified by dividing them with the number given. As long as this yields a remainder, the loop will continue to run.
        if (n % i == 0):#Once the divsion yields no remainder, the function will return false since the given number is divisible by a number other then 1 and itself.
            return False
    return True#If the loop ends without entering the if countion, the number given is a prime number. (The function returns true)
print(isprime(2))#These are test runs.
print(isprime(10))
print(isprime(17))

def factorize(n):#This is the second function which returns all the factors of a given number.
    answer = []#The factors will be stored in this list.
    for i in range(1,n+1):#This loop will append a number to the list as long as this number yields no remainder when divided with the given number. 
        if (n % i == 0):
            answer.append(i)
    return answer
print(factorize(2))#These are test runs.
print(factorize(72))
print(factorize(196))

def prime_factorize(n):#This is the third function which returns the prime factorization of a given number.
    answer = []#The prime factors from the prime factorization will be stored in this list.
    counter = 2;
    while (counter <= n):#This loop which starts at 2 (Since we do not care about dividing by 1 when constructing a prime factorization tree) will continue to look for numbers to divide with the
        #given number until the given number cannot be divided further wilthout becoming a decimal. (Having a remainder) For each number in the range that can be divided with the given number, it will be
        #appended to the list.
        if (n % counter == 0):
            answer.append(counter)
            n = n/counter
        else:#If the if condition is not satisfied, we just simply increment the counter by 1.
            counter = counter + 1
    return answer
print(prime_factorize(2))#These are test runs.
print(prime_factorize(72))
print(prime_factorize(196))
