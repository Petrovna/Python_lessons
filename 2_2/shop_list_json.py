#-*- coding: utf-8 -*-

import json
from pprint import pprint

with open('cook_book.json', 'r', encoding='utf-8') as cook_book_file:
   cook_book = json.load(cook_book_file)
   
def get_shop_list_by_dishes(dishes, people_count):
   shop_list = {}
   for dish in dishes:
      for ingridient in dish['ingridients']:
            new_shop_item = dict(ingridient)
            # пересчитали ингрединты по количеству людей
            new_shop_item['quantity'] = new_shop_item['quantity'] * people_count
            if new_shop_item['product'] not in shop_list:
               shop_list[new_shop_item['product']] = new_shop_item
            else:
               shop_list[new_shop_item['product']]['quantity'] += new_shop_item['quantity']
   return shop_list

def print_shop_list(shop_list):
   for key, shop_list_item in shop_list.items():
     print("{product} {quantity} {unit}".format(**shop_list_item))

def create_shop_list(people_count, first_dish, second_dish, third_dish):
   # получить блюда из кулинарной книги
   dish1 = cook_book[first_dish]
   dish2 = cook_book[second_dish]
   dish3 = cook_book[third_dish]
   dishes = [dish1, dish2, dish3]
    #заполнили список покупок
   shop_list = get_shop_list_by_dishes(dishes, people_count)
    # Вывести список покупок
   print_shop_list(shop_list)

print('Выберите первое блюдо: ')
first_dish = input().upper().strip()
print('Выберите второе блюдо: ')
second_dish =  input().upper().strip()
print('Выберите третье блюдо: ')
third_dish =  input().upper().strip()
print('На сколько человек?')
people_count = int(input())

print('Список покупок: ')
create_shop_list(people_count, first_dish, second_dish, third_dish)

