import random
#The lowercase has 26
lowercase_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

#The uppercase has 26
uppercase_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
#The number has 10
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#The amount of special character number is 28 
special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', 
    ',', '.', '<', '>', '/', '?', '|', '~'
]

l_let=int(input("Enter the amount of lowercase letter: "))
u_let=int(input("Enter the amount of uppercase letter: "))
num=int(input("Enter the amount of number: "))
spec_char=int(input("Enter the amount of special characters: "))
l_let_list=[]
u_let_list=[]
num_list=[]
special_list=[]

#use random.choice() method instead of randint()
for i in range(0,l_let):
    r_num=random.choice(lowercase_letters)
    l_let_list.append(r_num)

for j in range(0,u_let):
    r_num=random.choice(uppercase_letters)
    u_let_list.append(r_num)

for j in range(0,num):
    r_num=random.choice(numbers)
    num_list.append(r_num)
    
for j in range(0,spec_char):
    r_num=random.choice(special_characters)
    special_list.append(r_num)
    
l_let_list.extend(u_let_list)
num_list.extend(special_list)
l_let_list.extend(num_list)

random.shuffle(l_let_list)

text="".join(l_let_list)
print(f"The final password is : {text}")




