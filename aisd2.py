# Натуральные числа, в которых строго чередуются четные и нечетные цифры. Список используемых в числах четных цифр выводить отдельно прописью.

import re               
def number_to_words(n): #все цифры и их пропись
    f = {0 : 'ноль', 1 : 'один', 2 : 'два', 3 : 'три', 4 : 'четыре', 5 : 'пять',
    6 : 'шесть', 7 : 'семь', 8 : 'восемь', 9 : 'девять'}
    return f.get(n)
a = []
k = False
file = open("text2.txt", "r") #открываем файл
while True:
    buffer = file.readline().split()
    if not buffer: #если файл пустой
        if not k:
            print("Файл пустой")
        break
    k = True
    for j in buffer:
        res = re.findall(r'\b[^13579][^02468]\w*', j) #составляем регулярное выражение
        if len(res) != 0:
            a.append(res)
            a.sort() #сортируем список по неубыванию
if len(a) == 0:
    print('В файле нет подходящих чисел')
print('Список чисел, подходящих под условие: ', a)
for i in a:
    for g in i:
        print(g)
        for t in g:
            if int(t) % 2 == 0:
                evenNumber = number_to_words(int(t)) #четные цифры выводим словами
                print(evenNumber + ' - четная цифра')
    
