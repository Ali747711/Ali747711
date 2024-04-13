# ip = input('what is your target ip: ')
# ipChosen = int(ip)
 
#  if ipChosen >= 168 :
#     print('Attention!! Your IP has been hacked')
# elif ipChosen >= 192:
#     print('Attention! Your IP is being hacked now')
# elif ipChosen < 168 :
#     print('Relax! Everything is fine')
# else:
#     print('Change your IP address')


# # FirstName = input('What the fuck is your name? ')
# # LastName = input('What the fuck is your last name? ')
# # print(F" Your name is {FirstName} {LastName}")

# # fnum = input("what is the first number? ")
# # snum = input("what is the second number? ")

# # if fnum > snum:
# #         print("The fisrt number is greater")
# # elif snum > fnum:
# #         print("The second number is greater")
# # else:
# #         print("The numbers are same")
# # greeting = input('Hi there ')
# # fname = input('What is your name? ')

# # If statements
# # grade = int(input('What is your grade from final exam? '))
# grade = input('What is your grade from final exam? ')
# grade = int(grade)

# if grade >= 92:
#     age = input('How old are you? ')
#     age = int(age)
#     if age <= 10:
#         print("You did really good job and recieved A+ ")
#     else:
#         print('You did really good job and recieved A ')
# elif grade >= 85:
#     age = input('How old are you? ')
#     age = int(age)
#     if age <= 10:
#         print("You did really good job and recieved B+ ")
#     else:
#         print('You did really good job and recieved B ')
# elif grade >= 75:
#     age = input('How old are you? ')
#     age = int(age)
#     if age <= 10:
#         print("You did really good job and recieved C+ ")
#     else:
#         print('You did really good job and recieved C ')
# else:
#     print("You got a really low score and you failed. See you next time loser!! ")

#FIZZ-BUZZ( LOOPS )

# for num in range(1,100):
#     if num % 3 == 0 and num % 5 == 0:
#         print('fizzbuzz')
#     elif num % 3 == 0:
#         print("fizz")
#     elif num % 5 == 0:
#         print('buzz')
#     else:
#         print(num)

# fruits = ['apple', 'peach', 'banana', 'orange']

# for fruit in fruits:
#     print(fruit + ' pia')

# for num in range(5,30, 5):
#     print(num)

# FUNCTIONS
# def ali():
#     print('Nabiev Azamat')

# ali()
# import time
# random = int(input("Just choose one number from 1 to 20: "))

# def divider(random):
#     for num in range(1,random):
#         if num % 3 == 0 and num % 5 == 0:
#             print("fizzbuzz")
#         elif num % 3 == 0:
#             print("fizz")
#         elif num % 5 == 0:
#             print('buzz')
#         else:
#             print(num)

# print('The function is in process! Please wait !!')
# time.sleep(5)
# divider(random)

#EXAMPLE-2
# import time
# uname = str(input("what is your name dear? "))

# def askingName(uname):
#     print(f"Hello {uname}. How are you ? ")

# print('The function is in process! Please wait !!')
# time.sleep(2)
# askingName(uname)

#EXAMPLE-2 HANGMAN GAME
# import random

# print('Welcome to Hangman ! ')

# words = ['bitch','pork','university','apple']
# secretWord = random.choice(words)

# guess = input('Guess any letter ').lower()
# print(guess)
# for letter in secretWord:
#     if letter == guess:
#         print('Right')
#     else:
#         print('Wrong')

# name = 'azamat'.upper()
# university = 'Dong-A University'

# message = input('Hi %s, what about your university: ' %s(name))

#///////////////////////////////////

# age =input('How old are you?')
# age2 =int(age)

# if age2 >= 14:
#     print('You are adult!!')
# elif age2 >= 10 :
#     print('You are child')
# else:
#     print('You are so young')

# number = input('Please choose any number: ')
# number1 = int(number)

# if number1 >= 0:
#     if number1 % 2 ==0:
#         print(f'{number} is positive even number')
#     else:
#         print(f'{number} is positive odd number')
# else:
#     if number1 % 2 ==0:
#         print(f'{number} is negative even number')
#     else:
#         print(f'{number} is negative odd number')


# age = 25
# is_student = False
# has_job = True

# if age >= 18 and (is_student or has_job):
#     print("You are eligible for a loan.")
# else:
#     print("You are not eligible for a loan.")

# fruits = ['apple', 'banana', 'orange', 'mango', 'pineapple']
# choice = input('Write any name of fruit you like: ')

# if choice in fruits:
#     print(f'We sell {choice} in our store')
# else:
#     print(f'Please visit any other stores, we do not sell {choice} in our store')

# person = {"name": "Alice", "age": 25, "city": "New York"}
# print(type(person))

# num =int(input("Plese enter any positive integer: "))

# if num <= 0:
#     print('Invalid input, Please enter positive integer: ')

# else:
#     for i in range(1, num + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()

#     for i in range(num -1, 0, -1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()

# 

# cob = fruits[3].title() + fruits[0]
# fruits[2] = cob
# fruits.append('watermelon-1')
# print(fruits)

# vegetables = []
# vegetables.append('melon')
# vegetables.append('watermelon')
# vegetables.append('potato')
# vegetables.append('tomato')
# vegetables.insert(2, 'pumkin')
# # del vegetables[2]
# vegetables.remove('potato')
# my_favourite = vegetables.pop(2)
# print(f"Mening eng yaxshi ko'rgan sabzavotim bu {my_favourite} " )

# vegetables.sort()
# print(vegetables)
# fruits = ["apple", "banana", "orange", "pine", "pineapple", "strawberry", "kiwi", "blueberry", "lemon", "grapefruit", "peach", "watermelon"]
# print(sorted(fruits, reverse=True))

# for n in range(1,11):
#     print(f'{n} ning kvadrati bu {n**2} ga teng')

# sonlar = list(range(1,11))
# sonklar_kvadrati = []

# for son in sonlar:
#     sonklar_kvadrati.append(son**2)
# print(sonlar)
# print(sonklar_kvadrati)

# dostlar = []
# print('5 ta eng yaqin do\'stingizni ismini kiriting: ')

# for name in range(5):
#     dostlar.append(input(f'{name+1} - eng yaqin do\'stingizni ismi nima? \n>>>').capitalize())

# print(dostlar)

# friends = dostlar[0:2]
# print(friends)

# ism = input('ismingizni kiriting: \n>>>')
# if ism.lower() != 'ali':
#     print(f'Uzur, {ism.title()} biz Alini kutyabmiz')
# else:
#     print('Salom Ali, Xush kelibsiz !!')

# yosh = int(input('Yoshingizni kiriting: \n>>>'))

# if yosh <= 4:
#     narx = 0
# elif yosh <= 10:
#     narx = 5000
# elif yosh <= 15:
#     narx = 10000
# else:
#     narx = 18000

# print(f'Siz kirish uchun {narx} so\'m to\'lashingiz kerak')

# kun = input('Bugun haftaning qaysi kuni? \n>>>')

# if kun.lower() == 'yakshanba' or kun.lower() == 'shanba':
#     print(f'Bugun haftaning {kun.lower()} kuni bo\'lganligi uchun dam olamiz')
# else:
#     print(f'Bugun haftaning {kun.lower()} kuni bo\'lganligi uchun ishlaymiz')
    
# kun = input('Bugun haftaning qaysi kuni? \n>>>')
# harorat = float(input('Havo harorati qanday: \n>>>'))

# if (kun.lower() == 'yakshanba'or kun.lower() =='shanba') and harorat >= 30:
#     print(f'Bugun haftaning {kun} kuni bo\'lganligi uchun cho\'milgani boramiz')
# elif (kun.lower() == 'yakshanba'or kun.lower() =='shanba') and harorat < 30:
#     print(f'Bugun haftaning {kun} kuni bo\'lganligi ammo harorat {harorat} bo\'lganligi uchun cho\'milgani boramaymiz, judayam sovuq!')


# num =int(input("Plese enter any positive integer: "))

# if num <= 0:
#     print('Invalid input, Please enter positive integer: ')

# else:
#     for i in range(1, num + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()

#     for i in range(num -1, 0, -1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()

# num = int(input('Write any non-negative:- \n>>>'))
# total_sum = 0
# while num >= 0:
#     total_sum = total_sum + num
#     num = int(input('Write any non-negative:- \n>>>'))

# print(f'The sum of all numbers entered: {total_sum}')

# menu = ['osh', 'qozonkabob', 'shashlik', 'manti', 'mastava', 'asarti']
# buyurtmalar = []
# for n in range(4):
#     buyurtmalar.append(input('Nima yeyishni hohlaysiz?\n:'))

# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f'{taom} bizning menuda mavjud!')
#         else:
#             print(f'{taom} bizning menuda mavjud emas!, boshqa taomlarni tanlashingiz mumkin')
# else:
#     print('Hech narsa tanlamadingiz!')

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:

# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul

# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm

# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# age = int(input('How old are you?\n :'))

# if age <= 4 or age >= 60:
#     print('Sizga kirish bepul')
# elif age <= 18:
#     print('Sizga kirish narxi 10000 so\'m ')
# else:
#     print('Sizga kirish narxi 20000 so\'m ')

# mahsulotlar = ['olma', 'uzum', 'shaftoli', 'nok', 'smartphone', 'planshet', 'muzlatgich', 'kalbasa', 'non', 'tarvuz']
# plan = []

# for n in range(5):
#     plan.append(input('Qanday mahsulot sotib olishni istaysiz? \n :'))

# if plan:
#     for tavor in plan:
#         if tavor in mahsulotlar:
#             print(f'{tavor} bizning do\'konda mavjud')
#         else:
#             print(f'Afsuski {tavor} bizning do\'konda mavjud emas')
# else:
#     print('Sizning savatingiz bo\'sh !')

# LUG'ATLAR
# family = {'dadam': 'lazizjon', 'onam':'yulduzxon', 'opam': 'feruza', 'opam2': 'dilafruz', 'men':'Azamat' }
# print(family)
# print(f'Mening onamning ismi {family["onam"].title()}')

# otam = {'ism':'lazizjon', 'job':'dehqon', 'yosh':'50'}
# onam = {'ism':'yulduzoxn', 'job':'manager', 'yosh':'47'}
# opam = {'ism':'feruzaxon', 'job':'enaga', 'yosh':'24'}

# print(f"Dadaming ism {otam['ism'].title()}, ular {otam['yosh']} yoshdalar")
# print(otam)

# del otam['yosh']
# print(otam)

# otam['job'] = 'engineer'
# print(otam)

# print(otam.items())
# for kalit, qiymat in otam.items():
#     print(f"Kalit : {kalit}")
#     print(f"Qiymat: {qiymat}\n")

# data_types = {'boolean': 'true or false', 'string': 'harfli qiymat', 'interger': 'raqamlar', 'set': 'o\'zgarmas qiyamtlar', 'float': 'o\'nlik sonlar'}

# for k, v in sorted(data_types.items()):
#     print(f'{k} - {v}\n'.capitalize())
    

# for data in sorted(data_types):
#     print(data)

# countries = {'canada': 'ottava', 'malasia': 'kuala lumpur', 'USA': 'washington', 'uzbekistan': 'tashkent', 'korea': 'seoul'}

# print('Davalatlar:\n')
# for k in countries:
#     print(f'{k.title()}\n')

# print('Poytaxtlar:\n'.capitalize())
# for v in countries.values():
#     print(f"{v.title()}\n")

# visited = input('Tashrif buyurgan davlatingizni kiriting: \n>>>').lower()
# capital =countries.get(visited)

# if capital == None:
#     print(f'Kechirasiz bizda {visited.capitalize()} haqida malumot yo\'q ')
# else:
    # print(f'{visited.capitalize()} juda chiroyli davlat va uning poytaxti {capital.capitalize()} shahri.')

# menu = {'manti': '15000',
#         'osh': '12000',
#         'shashlik': '14000', 
#         'burger': '7400', 
#         'asarti': '18000', 
#         'salat': '5000', 
#         'kabob': '7000'
#         }

# buyurtmalar = []

# for k in range(3):
#     buyurtmalar.append(input(f'{k+1}-ga nima yeyishni hohlaysiz?\n >>> '))

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f'{buyurtma}ning narxi {menu[buyurtma]} so\'m\n'.capitalize())
#     else:
#         print(f'Kechirasiz bizda {buyurtma} mavjud emas.')

# gm_cars = []

# for i in range(10):
#     car = {
#         'rang': 'qora\n',
#         'model': 'gentra\n',
#         'yil': '2024\n',
#         'karobka': 'auto\n',
#         'country': 'uzbekistan\n',
#         'narxi': '12000\n'
#     }
#     gm_cars.append(car)

# for car in gm_cars[:3]:
#     car['rang'] = 'qizil'


# for car in gm_cars[3:6]:
#     car['karobka'] = 'mehanika'
#     car['rang'] = 'matvi'

# for car in gm_cars:
#     if car['karobka'] == 'auto':
#         car['narxi'] = '12000'
#     else:
#         car['narxi'] = '10000'
# for v in gm_cars:
#     print(v)
# print(gm_cars)


# WHILE LOOPS
# count = int(input('Insert any even number: \n >> '))
# while count <= 10:
#     print(count)
#     count =count + 1

# num = 1
# total = 0

# while num <= 200:
#     total += num
#     num += 1

# print(f"The sum of numbers from 1 to 200 is: {total}")

# num = 0

# password = ''

# while password != 'secret':
#     password = input('Input the password: \n >>>')
#     print("Wrong password !!")

# print('Access granted ')

# num = 1
# sum = 0

# while num <= 10:
#     sum = sum + num
#     num = num + 1
#     print(sum, num)

# num = 5
# factorial = 1

# while num > 0:
#     factorial *= num
#     num -= 1
#     print(factorial, num )
# print(f"The factorial of 5 is: {factorial}")

# num = int(input("Enter any number"))
# is_prime = True

# if num < 2:
#     is_prime = False
# else:
#     i = 2
#     while i * i <= num:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1

# if is_prime:
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

# def name(x):
#     num = 1
#     while num < x:
#         num += 1
#         print(num)
#     return x

# num = name(int(input('Enter any numer: \n >>')))
# print(num)

# ism = input('What is your name?\n >>>')
# savol = f'Hi {ism.title()}, how old are you? \n >>>'
# age = input(savol)

# num = 1

# while num < 6:
#     print(num, end=' ')
#     num += 1
# print('Finished')

# print('Kiritilgan sonni kvadratni topuvchi dastur')

# savol = 'Istalgan sonni kiriting: \n'
# savol += '(dasturni to\'xtatish uchun "exit" deb yozing)'

# value = ''
# while value != 'exit':
#     value = input(savol)
#     if value != 'exit':
#         print(int(value) ** 2)
# print('Dastur tugati')

# print('Kiritilgan sonni kvadratni topuvchi dastur')

# savol = 'Istalgan sonni kiriting: \n'
# savol += '(dasturni to\'xtatish uchun "exit" deb yozing\n)'

# sign = True
# while sign:
#     value = input(savol)
#     if value == 'exit':
#         sign = False
#     else:
#         print(float(value )** 2)
# print('Dastur tugati')

# while True:
#     value = input(savol)
#     if value == 'exit':
#         break
#     else:
#         print(float(value )** 2)
# print('Dastur tugati')

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     else:
#         print(f'Kiritilgan {son} ning kvadrati {son**2} ga teng')
# print('Dastur tugati')

# num = 0
# while num <=10:
#     num += 1
#     if num % 2 != 0:
#         continue
#     else:
#         print(num)

# print('Kutubxona dasturi')
# savol = 'Yaxshi ko\'rgan kitobingizni kiriting'
# savol += '(dasturni tugatish uchun "stop" deb yozing)\n'

# sign = True
# while sign:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         sign = False
#     else:
#         print(f'{qiymat.title()} is one of the most existing book')
# print('Dastur tugadi')

# value = ''
# while value != 'stop':
#     value = input(savol)
#     if value != 'stop':
#         print(f'{value.title()} is one of the most existing book')
# print('Dastur tugadi')

# while True:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#         break
#     else:
#         print(f'{qiymat.title()} is one of the most existing book')
# print('Dastur tugadi')

# print('Welcome to our muzey')

# savol = 'Yoshingizni kiriting: '
# savol += 'Dasturni to\'xtatish uchun "exit" yoki "stop" deb yozing''\n'
# value = True
# while value:
#     age = input(savol)
#     if age == 'exit' or age == 'stop':
#         value = False
#     elif int(age) < 7:
#         narh = 2000
#         print('Sizga kirish 2000 so\'m')
#     elif 7 <= int(age) < 18:
#         narh = 3000
#         print('Sizga kirish 3000 so\'m')
#     elif 18 <= int(age) < 65:
#         narh = 10000
#         print('Sizga kirish 10000 so\'m')
#     else:
#         narh = 0
# print('Dastur tugadi')

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat) < 0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
# print('Dastur yakunlandi')

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

# WHILE with Lists

# print("Counting friends")

# num = 1
# friends = []
# while True:
#     question = f'{num}-chi do\'stingizni ismini kiriting'
#     name = input(question)
#     friends.append(name.title())
#     takrorlash = input('Yana ism kiritishni hoglaysizmi? (ha/yo\'q)')
#     num += 1
#     if takrorlash != 'ha':
#         break
# print('Done!')
# print('Do\'stlar ro\'yxat: ')

# for name in friends:
#     print(name)

# print('\n')
# company = 'GM automobiles'.upper()
# print(f'{company:<^20}')

# cars = {}
# print()

# while True:
#     ques_1 = input('Qanday mashina sotasiz? \n >> ').title()
#     ques_2 = int(input(f'{ques_1}ning narxi qancha? \n >>'))
#     cars[ques_1] = ques_2

#     takrorlash = input('Yana kiritishni hohlaysizmi? (ha/yo\'q) \n >> ')
#     if takrorlash != 'ha':
#         break

# for name, price in cars.items():
#     print(f'{name} ning narxi {price} so\'m ')
#     print('\n\n')

# fruits = ["apple", "banana", "orange", "pine", "pineapple", "strawberry", "kiwi", "blueberry", "lemon",'apple', 'apple' "grapefruit", "peach", "watermelon",'apple']

# print(fruits)

# while 'apple' in fruits:
#     fruits.remove('apple')
#     print(fruits)

# tag = ('baholar tabeli')
# print(f'{tag.capitalize():.^30}')
# print('\n\n')
# talabalar = ['Ulugbek', 'sanjar','Ilyos', 'Umar']
# talabalar_baholari = {}

# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f'{talaba.title()} ga qanday baho qo\'yasiz  \n>>> ')
#     print(f'{talaba.title()} {baho} bilan baholandi !\n\n')
#     talabalar_baholari[talaba] = int(baho)

# for x, y in talabalar_baholari.items():
#     print(f'{x} ning bahosi {y} ga teng')
# print('\n\n')
# print(talabalar)

# for x in range(4):
#     talaba = talabalar.pop()
#     baho = input(f'{talaba.title()} ga qanday baho qo\'yasiz  \n>>> ')
#     print(f'{talaba.title()} {baho} bilan baholandi !\n\n')
#     talabalar_baholari[talaba] = int(baho)

# for x, y in talabalar_baholari.items():
#     print(f'{x} ning bahosi {y} ga teng')
# print('\n\n')

# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# orders = []

# while True:
#     savol = 'Nima sotib olmoqchisiz? (to\'xtatish uchun "exit") \n >>'.lower()
#     order = input(savol)
#     if order == 'exit':
#         break
#     if order in mahsulotlar:
#         print(f'{order} sizning savatchangizga qo\'shildi')
#         orders.append(order)
#     else:
#         print(f'Kechirasiz biz {order} sotmaymiz')

# print(f"\nYour orders: {', '.join(orders)}")

mahsulotlar = {}

value = True
while value:
    order = input('Nima sotib olasiz? \n >>')
    price = int(input(f'{order} ning narxini kiriting: \n >>'))
    mahsulotlar[order] = price
    if order != 'exit':
        mahsulotlar[order] = price
    else:
        value = False

print(f"\nYour orders: {', '.join(mahsulotlar)}")       


