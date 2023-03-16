n = int(input("Check this number: "))

""" def prime_checker(number = n):
    a = []
    for i in range(1,n+1):
        if  n % i == 0:
            a.append(i)
    
    if len(a) >= 3:
        print("its not a prime number")
    else:
        print("its a prime number ")
     """



#method 2

def prime_checker(number = n):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
        
    if is_prime:
        print("it's a prime number.")
    else:
        print("its not a prime number")

prime_checker()