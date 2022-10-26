import random

price = random.randint(0,100)
print("debut")
find = False
tries = 0
while(find == False and tries < 5):
    print("en cours")
    input_number = int(input("donnez un nombre : "))
    tries+=1
    if input_number < price:
        print("c'est plus")
    elif input_number > price:
        print("c'est moins")
    elif input_number == price:
        find = True
        print("bravooooo")

if find:
    print("fin")
else:
    print("t'es nul, c'était : "+str(price))