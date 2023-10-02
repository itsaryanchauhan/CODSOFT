import random

length = int(input("Enter the desired length for password: "))
password = ""
i =0

list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
        "1","2","3","4","5","6","7","8","9","0","!","@","#","$","&"]
while i != length:
    random_element = random.choice(list)
    password = password + random_element
    i+=1

print(password)