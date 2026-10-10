import pandas as pd
from tabulate import tabulate

import pandas as pd
from tabulate import tabulate

def table_head():
   head = []
   column_number = 1
   while True:
       if column_number > 2:
           answer = input('Хотите больше колонок? (д/н) - ')
           if answer.lower() == 'н':
               break
           elif answer.lower() != 'д':
               continue
       head.append(input(f'Введите название колонки {column_number} - '))
       column_number += 1
   return head

def table_body(head_length):
   body = []
   rows_number = 1
   while True:
       if rows_number > 2:
           answer = input('Хотите больше строк? (д/н) - ')
           if answer.lower() == 'н':
               break
           elif answer.lower() != 'д':
               continue
       row = []
       print(f'Row {rows_number}:')
       for i in range(head_length):
           row.append(input(f'Введите значение ячейки {i + 1} - '))
       body.append(row)
       rows_number += 1
   return body

def main():
   head = table_head()
   body = table_body(len(head))

   table = pd.DataFrame(body, columns=head)
   table.to_csv(input('Введите название таблицы - ') + '.csv', index=False)
   print(tabulate(table, showindex=False, headers=head))

if __name__ == '__main__':
   main()