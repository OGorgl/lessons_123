import pandas as pd


# if __name__ == '__main__': # точка входа
#    series_numbers = pd.Series([32, 12.4, -46, 2]) # создаем переменную, которая содержит объект класса Series

#    print(series_numbers) # выводим содержимое переменной series_numbers

if __name__ == '__main__':
   series_numbers = pd.Series([32, 12.4, -46, 2], ['elem_1', 'elem_2', 'elem_3', 'elem_4'])

   print(series_numbers['elem_3'])
   print(series_numbers.iloc[2])

# if __name__ == '__main__':
#    series_numbers = pd.Series({
#       'elem_1': 32,
#       'elem_2': 12.4,
#       'elem_3': -46,
#       'elem_4': 2
#    })
#    print(series_numbers)
#    print(series_numbers['elem_3'])
#    print(series_numbers.iloc[2])


