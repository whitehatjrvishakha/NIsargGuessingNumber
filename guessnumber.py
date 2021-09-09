import random
chances=3
a=random.randint(1,9)
while chances>0:
    no=int(input('Enter Your number '))

    if no==a:
        print('You Win')

    elif no<a:
        print('Your geuss is too low')
        chances=chances-1
    else :
        print("Your geuss is too high")
        chances=chances-1
        
    
    
if chances==0:
    print('You lose')

    