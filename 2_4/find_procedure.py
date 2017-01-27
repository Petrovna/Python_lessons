import glob
import os.path

migrations = 'Migrations'
adv = 'Advanced Migrations'

files_1 = glob.glob(os.path.join(migrations, "*.sql"))
files_2 = glob.glob(os.path.join(adv, "*.sql"))
files = files_1 + files_2

for file in files:
   print(file)
print(len(files))
            
while len(files) > 0:
   search_string =  input('Введите строку для поиска: ').upper()
   files_search =[]
   for file in files:
      with open(file) as file_sql:
         f  = file_sql.read().upper()        
         if (f.find(search_string) != -1):
            files_search.append(file)
            print(file)
   files = files_search		       
   print('Всего найдено файлов: ' + str(len(files_search)))
   print()
             