# name = int(input('Введите размер списка '))
# list = []
# for i in range(name):
#     a = int(input('Введите число '))
#     list.append(a)
# print(list)
# print(max(list))

# result = 0
# a = int(input('Введите число'))
# for i in range(1,a+1):
#     result +=i
# print(result)

# month = int(input('Жыл айын енгізіңіз '))
# if month >= 1 and month <= 2 or month ==12:
#    print("Ай мезгілі Қыс.")
# elif month >= 3 and month <= 5:
#    print("Ай мезгілі Көктем.")
# elif month >= 6 and month <= 8:
#    print("Ай мезгілі Жаз.")
# elif month >=9 and month <=11:
#     print("Ай мезгілі Күз")


# < = Кіші
# > = Көп

# milk = not False  # Сүт "бар ЕМЕС".
# cereals = True   # Хлопья бар.
# eggs = False    # Жұмыртқа жоқ.
# if milk and cereals or eggs:
#     if eggs:
#         if milk:
#             breakfast = "- омлет"
#         else:
#             breakfast = "- яичница"
#     else:
#         breakfast = "- хлопья с молоком"
# else:
#     if milk:
#         breakfast = "- стакан молока"
#     elif cereals:
#         breakfast = "можно погрызть сухих хлопьев"
#     else:
#         breakfast = "ничего не будет: разгрузочный день"
# print("Сегодня на завтрак", breakfast)

# list = ["Windows", "Macos", "ios", "android", "linux"]
# user_input = input("Введите слов ")
# for i in range(len(list)):
#      if list[i] == user_input:
#         print('Слово найдено')
#      else:
#         print('Слово не найдено')

# list = "Windows", "Macos", "ios", "android", "ada"]
# user_input = input("Введите слов ")
# for i in range(0,4):
#     if list[0] == user_input or list[1] == user_input or list[2] == user_input or list[3] == user_input:
#         print('Слово найдено')
#     else:
#         print('Слово не найдено')

# temperature = int(input('Бүгін дала қанша градус ? '))
# temperature2 = 26
# sun = True
# if sun and temperature > 25:
#      print('Ауа райы жақсы, серуендеуге болады')
# else:
#      print('Ауа рай бүгіндікке жаман, үйде кітап оқып отырамыз')

# age = int(input('Жасыңызды енгізіңіз: '))
# if age >= 1 and age <= 12:
#         print('Балалық шақ')
# elif age >=13 and age <= 19:
#     print('Мүшел жас, Жастық шақ')
# elif age >=20 and age <= 50:
#     print('Егде жас')
# elif age >= 50 and age <= 60:
#     print('Кәрілік')
# else:
#     print('Зейнеталық жас')

# print('Добро пожаловать в наш магазин одежды')
# order_price = int(input('Введите сумму заказа '))
# if order_price > 9999:
#      print('Цена с учетом скидки',int(order_price-(order_price/10)))
# else:
#      print('Скидка не доступна')

# print('Добро пожаловать в наш магазин одежды')
# order_price = int(input('Введите сумму заказ '))
# if order_price > 9999:
#  sales_percent = int(input('Введите процент скидки '))
#  order_price = order_price -int(order_price * sales_percent/100)
#  print('Цена с учетом скидки', order_price)
# else:
#  print('Скидка не доступна')

# order_price = int(input('Заказ бағасын енгізіңіз '))
# country = input('Сізге қай елге жеткізіп беру керек? ')
# if order_price > 10000 and country == 'Canada' or country == 'USA' and  order_price > 10000:
#     print('Доставка бесплатная')
# elif order_price > 7000 and country == 'Canada' or country == 'USA' and order_price > 7000:
#     print('Доставка 10$')
# else:
#     print('Доставка 20$')
#
# order_price = int(input('Введите сумму заказа '))
# country = input('Введите страну доставки: ')
# if order_price > 1000 and (country == 'Canada' or country == 'USA')

# result = 0
# a = int(input('Введите число'))
# for i in range(1,a+1):
#     result +=i
# print(result)

# list = [-3, 20, 0, -9, 100]
# result = 0
# for i in list:
#     if i > 0:
#      result +=i
# print(result)

# Тапсырма 1
# list = [100, 90, 80, 70, 60, 50,55,75,66]
# number_input = int(input('Введите цифра '))
# result = 'Цифра не найдено'
# for i in range(len(list)):
#     if number_input == list[i]:
#         result = 'Цифра найдено'
# print(result)

# Тапсырма 2
# List_number = [1, 2, 2, 3, 4, 5, 2]
# unique_list = list(set(List_number))
# print(unique_list)

# # Тапсырма 3
# list = [-3, 20, 0, -9, 100, -9]
# for i in list:
#     if i < 0:
#      index = list.index(i)
#      list[index] = 0
#  print()

# counter = 9
# while counter > 0:
#      print(counter)
#      counter = counter -2


# parol = (input('Введите пароль '))
# while parol != 'admin':
#      print('Неверный пароль, попробуйте ище раз!')
#      parol = (input('Введите пароль '))
# if parol == 'admin':
#      print('Доступ Разрешен')

# list = ["Windows", "Macos", "ios", "android", "linux"]
# user_input = input("Введите слов ")
# while user_input not in list:
#      print('Слово не найдено')
#      user_input = input("Введите слов ")
# if user_input in list:
#      print('Слово найдено')


# print('1. Пистолет')
# print('2. Автомат')
# print('3. РПГ')
# print('0. Выйти')
# weapon =int(input('Выберите оружие: '))
# while weapon!=0:
#     if weapon == 1:
#         print('пиу пиу')
#     elif weapon == 2:
#         print('дрт дрт')
#     elif weapon == 3:
#         print('Boom Boom!')
#     print('1. Пистолет')
#     print('2. Автомат')
#     print('3. РПГ')
#     print('0. Выйти')
#     weapon = int(input('Выберите оружие: '))
#
# print('Вы Вышли')




# list=[]
# while True:
#     print('Выберите действие:')
#     print('1.Добавить задачу')
#     print('2.Ввести список задач')
#     print('3.Удалить задачу')
#     print('0.Выйти')
#     admin = int(input())
#     if admin==1:
#         print('Введите задачу для планирования')
#         ad0_list=input()
#         list.append(ad0_list)
#     elif admin==2:
#         counter = 0
#         for ad1_list in list:
#             counter = counter +1
#             print(counter, ad1_list)
#     elif admin==3:
#         counter = 0
#         for ad_list in list:
#             counter = counter +1
#             print(counter, ad_list)
#         print('Выберите план')
#         ad2_list = int(input())
#         list.remove(list[ad2_list-1])
#     else:
#         print('Вы вышли')
#         break

# list=[7, -3,9, -11,18,99,2,11]
# a = 0
# b = 0
# for i in list:
#     if i > a:
#         a = i
#
#     if i < b:
#         b = i
# print(a)
# print(b)

# list=[7, -3,9, -11,18,99,2,11]
# list1=[]
# list2=[]
# a=len(list)
# for i in range(0,a):
#     if list[i]>0:
#         list1.append(list[i])
# print('Оң сандар: ',len(list1))
# for i in range(0,a):
#     if list[i]<0:
#         list2.append(list[i])
# print('Теріс сандар: ',len(list2))
#
# list=[7, -3,9, -11,18,99,2,11]
# for i in range(1,len(list), 2):
#     print(i)

# def say_about():
#     print('Привет, я Томирис!')
#     print('Я персональный помощник.')
#     print('Я ещё маленькая,')
#     print('но постоянно расту и умнею:')
#     print('ведь мой код каждый день дописывают!')
# say_about()

# def print_friends_count(friends_count):
#     if friends_count == 0:
#         print('У тебя нет друзей')
#     elif friends_count == 1:
#         print('У тебя', friends_count, 'друг')
#     elif friends_count >= 2 and friends_count <= 4:
#         print('У тебя', friends_count, 'друга')
#     elif friends_count >= 5 and friends_count < 20:
#         print('У тебя', friends_count, 'друзей')
#     else:
#         print('Ого, сколько у тебя друзей! Целых', friends_count)
#
# for i in range(0,21):
#     print_friends_count(i)

# def lets_go(name='Айбек', target='учить Python'):
#     print(name + ', пойдем ' + target)
# lets_go()

# def lets_go(name='Друг', target='Учить Python'):
#     print(name + ', пойдём ' +target)
# lets_go(target='читать следующий урок!')

# def add_task():
#     print('Введите задачу для планирования')
#     ad0_list = input()
#     list.append(ad0_list)
# def print_tasks():
#     counter = 0
#     for ad1_list in list:
#         counter = counter + 1
#         print(counter, ad1_list)
# def delete_task():
#     print('Выберите план')
#     ad2_list = int(input())
#     list.remove(list[ad2_list - 1])
#
# list=[]
# while True:
#     print('Выберите действие:')
#     print('1.Добавить задачу')
#     print('2.Вывести список задач')
#     print('3.Удалить задачу')
#     print('0.Выйти')
#     admin = int(input())
#     if admin==1:
#         add_task()
#     elif admin==2:
#         print_tasks()
#     elif admin==3:
#         print_tasks()
#         delete_task()
#     else:
#         print('Вы вышли')
#         break

# def multiply(a, b):
#     print(a*b)
# multiply(2, 3)

# asdsad = [10, 20, 30, 40, 50]
# def calculate_sum(list_numbers):
#     print(sum(list_numbers))
#
# calculate_sum(asdsad)
#
# numbers1 = [30,40,50,20,90]
# calculate_sum(numbers1)


# def print_multyply_table(a):
#     for i in range(1,11):
#         print(a,'*',i,'=',a*i)
# print_multyply_table(333)

# def number_of_occurences(word, letter):
#     result = 0
#     for i in word:
#         if i == letter:
#             result = result + 1
#     print(result)
# number_of_occurences('Hello World', 'p')



# def lets_go(name='Друг', target='Учить Python'):
#     print(name + ', пойдём ' +target)
# lets_go(target='читать следующий урок!')
# lets_go(target='питон')

# def multiply_sum(numbers):
#     result = 1
#     for i in numbers:
#         result = result *i
#     print(result

# def snow_date(date,month,year):
#     print('Дата:',str(date)+'.'+str(month)+ '.'+str(year))
# snow_date(6,7,2023)



# def rooms_equal(room_size,room_list):
#     count = 0
#     for room in room_list:
#         if room == room_size:
#             count = count + 1
#     print('Комнат площадью', room_size, 'кв.м:', count)
# flat = [
#     5.55, 22.19, 7.78, 26.86, 5.55,
#     29.84, 22.19, 5.55, 16.85, 4.52
# ]
# hut = [9.2, 3.5, 8.1, 2.3, 9.2, 4.2, 6.9]
# rooms_equal(9.2, hut)
# rooms_equal(5.55, flat)

# def number_of_occurrences(char, string):
#     count = 0
#     for letter in string:
#         if letter == char:
#             count = count + 1
#     print('Исходная строка:', string)
#     print('Количество вхождений символа', char, 'составляет:', count)
# phrase = 'Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили.'
# number_of_occurrences('е', phrase)

# def count_vowels(string):
#     letters = ['a','e','i','o','u','y']
#     count = 0
#     for letter in string:
#         if letter in letters:
#             count = count + 1
#     print(count)
# text = input('Текст: ')
# count_vowels(text)


# def comfort_count(temperatures):
#     count = 0
#     for comfort in temperatures:
#         if comfort == temperatures:
#             count = count + 1
#     print(count)
# may_2022 = [26, 19, 13, 17, 20, 24, 12, 17, 21, 19, 20, 23, 26, 25, 24,
# 27, 26, 18, 20, 25, 31, 20, 22, 28, 30, 34, 31, 16, 27, 30, 24]
# may_2023 = [12, 12, 15, 17, 22, 25, 27, 29, 21, 24, 27, 21, 25, 13, 20,
# 23, 24, 12, 19, 23, 24, 26, 24, 25, 27, 22, 23, 23, 29, 33, 33]
# comfort_count(26,may_2022)
# comfort_count(27,may_2023)


# may_2022 = [26,19,13,17,20,24,12,17,21,19,20,23,26,25,24,27,26,18,20,25,31,20,22,28,30,34,31,16,27,30,24]
# # Осы функцияны толтырыңыз
# def comfort_count(temperatures):
#     count = 0
#     for temp in temperatures:
#         if 22 <= temp <= 26:
#             count += 1
#     return count
# nice_days = comfort_count(may_2022)
# print('Количество тёплых дней в этом месяце',nice_days)


# def is_even():
#     number = int(input('Введите число: '))
#     result = number
#     print(result)
#     if (number % 2==0):
#         print("Число чётное")
#     else:
#         print("Число не чётное")
# is_even()
#
# def calculate_average():
#     number = [150, 27, 123, 12, 23]
#     print(sum(number) // 2)
# calculate_average()

# cities = [
#     'Алматы',
#     'Астана',
#     'Шымкент',
#     'Актобе',
#     'Караганда',
#     'Тараз',
#     'Павлодар',
#     'Семей',
#     'Астана',
#     'Кызылорда',
#     'Шымкент',
#     'Актау',
#     'Астана',
#     'Петропавловск',
#     'Алматы',
# ]
#
# unique_cities = set(cities)
# for i in unique_cities:
#     print('У меня есть друг в городе',i)

# def print_valid_cities(barlyk_qalalar,atalgan_qalalar):
#     oynda_atalmagan_qalalar = barlyk_qalalar.difference(atalgan_qalalar)
#     for i in oynda_atalmagan_qalalar:
#         print(i)
# all_cities = {
#     'Алматы',
#     'Астана',
#     'Шымкент',
#     'Актобе',
#     'Караганда',
#     'Тараз',
#     'Павлодар',
#     'Семей'
# }
# used_cities = {'Алматы', 'Семей', 'Караганда'}
#
#
# def add_cities(all_cities,new_cities):
#     for city in new_cities:
#         all_cities.add(city)
# all_cities = {
#     'Алматы',
#     'Астана',
#     'Шымкент',
#     'Актобе',
#     'Караганда',
#     'Тараз',
#     'Павлодар',
#     'Семей'
# }
# new_cities = [
#     'Атырау',
#     'Кызылорда',
#     'Костанай',
#     'Актау',
#     'Уральск',
#     'Петропавловск',
#     'Кокшетау'
# ]
# add_cities(all_cities, new_cities)
# print_valid_cities(all_cities, used_cities)

# def get_together_games(playgame_1,playgame_2):
#     return set(playgame_1).intersection(set(playgame_2))
# tomiris_games = [
#     'Online-chess',
#     'Города',
#     'Doom',
#     'Крестики-нолики'
# ]
# set(tomiris_games).intersection()
# alexa_games = [
#     'Doom',
#     'Online-chess',
#     'Города',
#     'GTA',
#     'World of tanks'
# ]
# together_games = get_together_games(tomiris_games, alexa_games)
# for i in together_games:
#     print(i)


# friends = {
#     'Сергей': 'Павлодар',
#     'Айбек': 'Атырау',
#     'Дамир': 'Астана'
# }
# friends['Сергей'] = 'Астана'
# print(friends['Сергей'])

# friends = {
#     'Сергей': 'Павлодар',
#     'Айбек': 'Атырау',
#     'Дамир': 'Астана',
#     'Рустем': 'Алматы',
#     'Максим': 'Кокшетау',
#     'Амир': 'Алматы',
#     'Азат': 'Уральск',
#     'Руслан': 'Астана'
# }
# for i in set(friends.values()):
#     print(i)


# dictionary = {
#     'a': 50,
#     'b': 20,
#     'c': 13.2,
#     'd': 70
# }
# dictionary = dictionary +str
# print(a)
# print(dictionary)
# sozder = dictionary.values()
# print(sum(sozder))

# friends = {
#     'Сергей': 'Павлодар',
#     'Айбек': 'Атырау',
#     'Дамир': 'Астана',
#     'Асылбек': 'Шымкент',
#     'Самат': 'Ташкент'
# }
# print(friends)


# friends = {
#     'Сергей': 'Павлодар',
#     'Айбек': 'Атырау',
#     'Дамир': 'Астана',
#     'Асылбек': 'Шымкент',
#     'Самат': 'Ташкент'
# }
# new_friends = {
#     'Амир': 'Алматы',
#     'Азат': 'Уральск',
#     'Руслан': 'Астана'
# }
#
# friends.update(new_friends)
# print(friends)

# friends_names = ['Сергей', 'Айбек', 'Дамир', 'Рустем', 'Максим']
# friends_cities = ['Павлодар', 'Атырау', 'Астана', 'Алматы', 'Кокшетау']
#
# friends = {}
#
# for i in range(len(friends_names)):
#     name = friends_names[i]
#     city = friends_cities[i]
#     friends[name] = city
# print(friends)

# Үй тапсырмасы

# friends = {
#     'Сергей': 'Павлодар',
#     'Айбек': 'Атырау',
#     'Дамир': 'Астана',
#     'Рустем': 'Алматы',
#     'Максим': 'Кокшетау',
#     'Амир': 'Алматы',
#     'Азат': 'Уральск',
#     'Руслан': 'Астана'
# }
# for name,gorod in zip(friends, friends.values()):
#     print(name,'живёт в городе',gorod)
#
#
# favorite_songs = {
#     'Сергей': ['Karma Police', 'Reptilia', 'No Surprises'],
#     'Дамир': ['Shake it out', 'The Show Must Go On', 'Наше лето'],
#     'Рустем': ['Владимирский централ', 'Той жыры', 'Аяулым']
# }
#
# print('Дамирдың сүйікті әндерінің саны',len(favorite_songs))
# favorite_songs.pop('Сергей')
# favorite_songs.pop('Дамир')
# for music in favorite_songs.values():
#     print('Рүстемнің сүйікті әндері',music)

# def is_anyone_in(collection, city):
#     for friend in city:
#         if collection > friend:
#             print('в городе',city,'меня есть друг, но мне туда не надо')
#         else:
#             print('в городе живет',collection,'Обизательно зайду в гость!')
#
# is_anyone_in(friends, 'Алматы')


# playlist = {
#     'Venus As a Boy',
#     'Yesterday',
#     'Comfortably Numb',
#     'Time After Time',
# }
# new_music = [
#     'Stairway to Heaven',
#     'Wish You Were Here',
#     'Bohemian Rhapsody',
#     'Let It Be',
# ]
#
# playlist.update(new_music)
# print(playlist)