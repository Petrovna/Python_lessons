#-*- coding: utf-8 -*-

cook_book= {}
with open('cook_book.txt', 'r', encoding='utf-8') as cook_book_file:
    for line in cook_book_file:
        dish_name=line.strip().upper()
        ingridients_count = int(cook_book_file.readline())
        ingridients = []
       # print (dish_name, '\n', ingridients_count)
        for i in range(ingridients_count):
            ingridients_name, ingridients_quantity, ingridients_unit = cook_book_file.readline().split('|') 
            ingridients_quantity_int = int(ingridients_quantity)
            ingridients.append ( {'product' :  ingridients_name, 'quantity': ingridients_quantity_int, 'unit':  ingridients_unit})
        
            #print (ingridients_name, '\n', ingridients_quantity_int, '\n', ingridients_unit)
           # print(ingridients[i])
        dish = {'name': dish_name, 'ingridients': ingridients} 
       # print(dish)
        cook_book_file.readline() 
        cook_book.update({dish_name: dish})
print (cook_book)
    
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
first_dish = input().upper()
print('Выберите второе блюдо: ')
second_dish =  input().upper()
print('Выберите третье блюдо: ')
third_dish =  input().upper()
print('На сколько человек?')
people_count = int(input())

print('Список покупок: ')
create_shop_list(people_count, first_dish, second_dish, third_dish)
