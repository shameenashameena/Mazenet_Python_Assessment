# EXERCISE 1: PRIME CHECK

num = int(input("Enter a number: "))

if num <= 1:
    print(False)
    
else: 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(False)
            break
    else:
        print(True)
       
           
           
    