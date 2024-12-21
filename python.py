import random
#1
rand = random.randint(1,10)
attempt = 0

print("Угадай число")
while True:
  n = int(input("Число: "))
  if (rand == n):
    attempt +=1;
    print("Вы выйграли за", attempt, "попыток")
    break
  else:
    print("Не угадали")
    attempt += 1;
    if (n > rand): 
      print("Заданное число меньше")
    else: 
      print("Заданное число больше")
    
#2 
mass = input("Буквы: ").lower().split(' ')
result = []
temp = []

for i in range(len(mass)):
    if len(temp) == 0 or mass[i] == temp[0]:
        temp.append(mass[i])  
    else:
        result.append(temp)  
        temp = [mass[i]]

if len(temp) > 0:
    result.append(temp)  

final = []  
seen = []  

for item in mass:
    if item not in seen:  
        seen.append(item)  
        gruppa = []
        for i in mass:
            if i == item:
                gruppa.append(i)
        final.append(gruppa)

print(final)

#3
mast = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 2, 'Q': 3, 'K': 4, 'A': 11}
random.shuffle(mast)
point = 0
while True:
    answer = input("v - Взять карту\nz - Закончить игру\n")
    
    if answer == 'z':
        print("У вас", point, "очков.")
        break
    elif answer == 'v':
        card = mast.pop()
        point += values[card]  
        
        print("Ваши карты:", card)
        print("Ваши очки:", point)
        
        if point > 21:
            print("Вы проиграли")
            break
        elif point == 21:
            print("Вы выиграли")
            break
    else:
        print("Есть только 2 варианта")
