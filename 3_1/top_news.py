#-*- coding: utf-8 -*-

import json
from collections import Counter

#Открываем JSON-файл с указанным именем и кодировкой, возвращаем словарь 
def open_file_with_coding(file_name, coding):
   with open(file_name, 'r', encoding = coding) as news_file:
      return json.load(news_file)

#Обрабатываем словарь и создаем список самых часто встречающихся слов больше заданной длины   
def top_words(news, min_word_len, len_top):
   len_list = len(news['rss']['channel']['item'])
   big_list = []
   for i in range(len_list):
     if ('__cdata' in news['rss']['channel']['item'][i]['description']):  
        news_topic = sorted(news['rss']['channel']['item'][i]['description']['__cdata'].split())
     else:
        news_topic = sorted(news['rss']['channel']['item'][i]['description'].split())
     for word in news_topic:       
        if word.isalpha() and len(word) > min_word_len:
           big_list.append(word)
   return Counter(big_list).most_common(len_top) 

#Печать списка слов и частоты их появления
def print_top(list_words):
   for i in range(len(list_words)):
      print(list_words[i][0], list_words[i][1])

#Обработка всех файлов, переданных в виде списка с указанием кодировки
def analyse_files(list_files_and_codes, min_word_len, len_top):
   for i in range(len(list_files_and_codes)):
      news_dict = open_file_with_coding(list_files_and_codes[i][0], list_files_and_codes[i][1])  
      top_list = top_words(news_dict, min_word_len, len_top)
      print('Обработка файла ' + list_files_and_codes[i][0] + ' с кодировкой ' + list_files_and_codes[i][1])
      print_top(top_list)
      print()    
      
#Задание списка файлов и вызов основной функции
list_files = [['newsafr.json', 'utf-8'], ['newscy.json', 'koi8-r'],  ['newsfr.json', 'iso8859-5'], ['newsit.json', 'cp1251']]

analyse_files(list_files, 6, 10) #передаем список файлов, мин. длину слова, длину top-листа

