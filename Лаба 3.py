import math

number = math.sin(0.56) #Перший член послідовності
counter = 1 #Значення n
summ = 0    #Cума послідовності n-ї кількості number
while number > 0.000001:
    summ = summ + number #Доплюсовуємо до загальної суми
    print("Доданок %s: %8.6f" % (counter, number))
    counter = counter + 1  #Номер цикла
    number = 1 / (counter ** 2) * math.sin(0.56) #Розрахунок значення наступного члена суми
y = 1 / summ

print(input("Значення змінної y: ""{:.5f}".format(y)))
