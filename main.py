#Write your code below this line ๐

def prime_checker(number):
  isPrime = True
  for i in range(2, number):
    isPrime = isPrime and (number % i != 0)

  prime = "is"
  if not isPrime:
    prime = "not"
    
  print(f"{number} {prime} a prime number.")


#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)



