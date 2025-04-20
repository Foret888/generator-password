# from setting import *
# print(token,password)

# print(locals())
# # print(dir(s))
# from setting import password, card
# a = input('Введие номер карты: ')
# if a == card:
#     b = input('Введите пароль: ')
#     if b == password:
#         print('Успешный вход')
# else:
#     print('Не верный номер карты!')



# from setting import *

# a = House(1200, 'Haiteck')
# b = a.result('123 * 50')
# # print(b)

# a = '10 * 5'
# print(eval('2983749837 +832746873276487'))


# import time
# t = time.time()
# print(time.strftime('Год: %Y Месяц: %m День: %d Час: %H Минута: %M '))
# local = time.localtime(t)
# print(f'Год: {local.tm_year}, Месяц: {local.tm_mon}, День: {local.tm_mday}, Часы: {local.tm_hour}, Минута: {local.tm_min}, Секунда: {local.tm_sec}')

# print(time.asctime())
# p = time.ctime().split()
# print(f'Год: {p[-1]}, Месяц: {p[1]}, День: {p[0]}, Часы: {p[3]}')


# import random

# # a = random.uniform(1,100)
# # a = random.randint(1,100)
# lst = ['first', 'Second', 'Third', 12,13,65,7]
# random.seed()
# a = random.shuffle(lst)


# print(lst)


# import random
# c = ['Давуд', 'Тынчтык', 'Саян', 'Халид', 'Имрон']
# a = input('Введите слово: ')
# b = random.choice(c)
# if a == b:
#     print('Вы выиграли!')
# else:
#     print(f'Вы проиграли!! На самом деле я выбрал: {b}')


# import random
# a1 = ['abadqw', 'cdqwd', 'eoqwdqw', 'fnwfq', 'mzwef', 'xvewr', 'pyjrw', 'rqrt', 'sgtyu', 'hjnh', 'lkqwd', 'hfruhfr', 'jkeew', 'whfw', 'wehfyew', 'qsqfrw', 'qgywddwdrfg', 'bvbvvc', 'cdcxx', 'bnbnep', 'hwq', 'eue', 'owie', 'qwuisygwt', 'tswrs']
# b1 = ['12678', '2356', '3189', '445678', '55232', '67453', '7435', '8845','99675', '32435', '23467', '245879', '11107897', '65756', '567', '4654', '4564345', '4353', '9797', '7897', '1223', '3232', '4545', '212344', '745']
# c1 = ['*$', '^|', '#.', '@%', '!"', '?;', '<!', '()>', '/\\', '`~']


# ru = print('Выберите язык на котором вы хотите продолжить! Напишите 1 что бы продолжить на русском')
# en = print('Please select the language you wish to continue in! Write 2 to continue in English')
# wri = int(input())
# if wri == 1:
#     print('Генератор паролей')
#     a = input('Добавить ли в пароль буквы?: ')
#     b = input('Добавить ли цифры в пароль?: ')
#     c = input('Добавить ли специальные знаки в пароль?: ')
#     num3 = random.choice(a1)
#     num1 = random.choice(b1)
#     num4 = random.choice(c1)




#     if a == 'да' and b == 'да' and c == 'да':
#                 print('Результат: ', num3 + num1 + num4)
#     elif a == 'нет' and b == 'нет' and c == 'нет':
#                 print('Ошибка, невозможно сгенерировать пароль без букв и без цифр а также без специальных знаков!')


#     if a == 'да' and b == 'да' and c == 'нет':
#                 print('Результат: ', num3 + num1)

                

#     if a == 'да' and b == 'нет' and c == 'да':
#                 print('Результат: ', num3 + num4)



#     if a == 'да' and b == 'нет' and c == 'нет':
#                 print('Результат: ', num3)



#     if a == 'нет' and b == 'да' and c == 'да':
#                 print('Результат: ', num1 + num4)



#     if a == 'нет' and  b == 'нет' and c == 'да':
#                 print('Результат: ', num4)



#     if a == 'нет' and b == 'да' and c == 'нет':
#                 print('Результат: ', num1)





# if wri == 2:
#         print('Password generator')
#         a = input('Should I add letters to my password?: ')
#         b = input('Should I add numbers to my password?: ')
#         c = input('Should I add special characters to my password?: ')
#         num3 = random.choice(a1)
#         num1 = random.choice(b1)
#         num4 = random.choice(c1)






# if a == 'yes' and b == 'yes' and c == 'yes':
#             print('Results: ', num3 + num1 + num4)
# elif a == 'no' and b == 'no' and c == 'no':
#             print('Error, it is impossible to generate a password without letters and numbers and without special characters!')


# if a == 'yes' and b == 'yes' and c == 'no':
#             print('Result:', num3 + num1)

            

# if a == 'yes' and b == 'no' and c == 'yes':
#             print('Result:', num3 + num4)



# if a == 'yes' and b == 'no' and c == 'no':
#             print('Result:', num3)



# if a == 'no' and b == 'yes' and c == 'yes':
#             print('Result:', num1 + num4)



# if a == 'no' and  b == 'no' and c == 'yes':
#             print('Result:', num4)



# if a == 'no' and b == 'yes' and c == 'no':
#             print('Result:', num1)


# import requests

# req = requests.get('https://skillbox.ru/')
# # print(req.content)
# # print(req.text)
# with open('index.html', 'w', encoding='utf-8') as ind:
#         ind.write(req.text)
# with open('style.css', 'w', encoding='utf-8') as ind:
#         ind.write(req.text)
# with open('main.js', 'w', encoding='utf-8') as ind:
#         ind.write(req.text)



# import time
# for i in range(1, 10):
#         print(i)
#         time.sleep(1)

# import threading


# def numbers():
# 	for i in range(100):
# 		print(i)

# a = int(input('Введите количество потоков: '))

# lst = []
# for i in range(a):
# 	a = threading.Thread(target=numbers)
# 	lst.append(a)

# for i in range(a):
# 	lst[i].start()
# # 	print(lst)
# # print(a)


# a = int(input('Введите число: '))
# for i in range(0, a, 2):
# 	print(i)

# import requests
# import threading
# a = int(input())

# def ddos(b):
#     req = requests.get('https://kalys.bolotbekov.kg/')
#     print(req)
# lst = [ threading.Thread(target=ddos, args=(i,)) for i in range(a)]
    
# for i in range(a):
#     lst[i].start()

# def read_text(b):
#     a = open('dataBases/notebook.txt', 'w')
#     text = a.write()
#     print('rfggrtgr')
#     a.close()
# read_text()



# b = open('dataBases/notebook.txt', 'a')
# a = (input('Введите отзыв от 1 до 5: '))

# if a > '5':
#     print('Отзыв только до 5')
# else:
#     b.append(a)

# b.close()




# def write_text(t):
#     a = open('dataBases/notebook.txt', 'r')

#     b = a.read()
#     print(b)

    
#     a.close()
    



