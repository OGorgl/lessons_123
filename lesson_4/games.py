import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(data):
   average_sales_by_genre = data.groupby('Genre')['Sales'].mean()
   most_popular_game = data.loc[data['Sales'].idxmax()]
   highest_rated_game = data.loc[data['Rating'].idxmax()]


   return average_sales_by_genre, most_popular_game, highest_rated_game

def visualize_data(average_sales_by_genre, data):
   plt.figure(figsize=(10, 5))
   average_sales_by_genre.plot(kind='bar', color='skyblue')
   plt.title('Средние продажи по жанрам')
   plt.xlabel('Жанр')
   plt.ylabel('Средние продажи (млн)')
   plt.xticks(rotation=45)
   plt.grid(True)
   plt.show()

   plt.figure(figsize=(8, 5))
   data['Rating'].plot(kind='hist', bins=20, color='lightgreen', edgecolor='black')
   plt.title('Распределение рейтингов игр')
   plt.xlabel('Рейтинг')
   plt.ylabel('Количество игр')
   plt.grid(True)
   plt.show()

def main():
   file_path = input('Введите путь к файлу с данными - ')
   data = pd.read_excel(file_path)

   average_sales, popular, rated = analyze_data(data)

   print('Средние продажи по жанрам:\n', average_sales)
   print('Самая популярная игра:\n', popular)
   print('Самая высоко оцененная игра:\n', rated)

   visualize_data(average_sales, data)

if __name__ == '__main__':
   main()