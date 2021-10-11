import random

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
symbols=["!","#","$","%","&","(",")","=","~","-","^","?","_"]

potential_final=""

alph_count = int(input("How many alphabet characters? "))
number_count =int(input("How many numberical characters? "))
symbol_count = int(input("How many symbol characters? "))

for alp in range (0,(alph_count)):
    potential_final += alphabet[random.randint(0,len(alphabet)-1)]

for num in range (0,(number_count)):
    potential_final += numbers[random.randint(0,len(numbers)-1)]

for sym in range (0,(symbol_count)):
    potential_final += symbols[random.randint(0,len(symbols)-1)]

#print(potential_final)
print("".join(random.sample(potential_final,len(potential_final))))
