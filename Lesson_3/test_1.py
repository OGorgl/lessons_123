import pandas as pd

# if __name__ == '__main__':
#    super_heroes = pd.DataFrame({
#       'Super Hero': ['Spider Man', 'Iron Man', 'Capitan America', 'Thor'],
#       'Debut': [1962, 1962, 1941, 1962],
#       'Real name': ['Peter Parker', 'Tony Stark', 'Steve Rogers', 'Thor Odinson']
#    })

#    print(super_heroes)



if __name__ == '__main__':
   super_heroes = pd.read_csv('Lesson_3\super heroes.csv') # создаем переменную super_heroes, в которую помещаем содержимое файла super heroes.csv

   print(super_heroes)