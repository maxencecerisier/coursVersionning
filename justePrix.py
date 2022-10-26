import random

price = random.randint(0,100)
print("debut") #affiche debut dans le terminal
find = False # déclare et mets find à flase
tries = 0 # déclare et mets find à flase
while(find == False and tries < 5): # tant que tries < 5
    print("en cours") # print en cours
    input_number = int(input("donnez un nombre : ")) # recupere le nombre saisie
    tries+=1 # augmente tries
    if input_number < price:
        print("c'est plus")
    elif input_number > price:
        print("c'est moins")
    elif input_number == price:
        find = True
        print("bravooooo")

if find:
    print("fin") #print fin
else:
    print("t'es nul, c'était : "+str(price))