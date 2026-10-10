import matplotlib.pyplot as plt  # импортируем модуль Pyplot
import pandas as pd  # импортируем модуль Pandas

def main():  # объявляем функцию для запуска основной программы
    weather_changes = pd.DataFrame({  # создаем DataFrame с информацией о погоде
    'Дата': ['14 мая', '15 мая', '16 мая', '17 мая', '18 мая', '19 мая', '20 мая'],
    'День': [22, 22, 24, 25, 25, 26, 27],
    'Ночь': [11, 10, 13, 16, 14, 16, 10]
    })
    print(weather_changes)  # выводим данные DataFrame

    # plt.plot(weather_changes['Дата'], weather_changes['Ночь'], label='Ночь', color='blue', marker='o', markersize=4)  # создаем график погоды ночью
    # plt.plot(weather_changes['Дата'], weather_changes['День'], label='День', color='green', marker='o', markersize=4)  # создаем график погоды днем
    # plt.xlabel('Дата')  # задаем название нижней части графика
    # plt.ylabel(u'Температура, C\N{DEGREE SIGN}')  # задаем название вертикальной части графика
    # plt.title('Изменение температуры в течение недели')  # задаем название всего графика
    # plt.legend()  # создаем легенду
   
    # plt.scatter(weather_changes['Дата'], weather_changes['Ночь'])
    # plt.scatter(weather_changes['Дата'], weather_changes['День'])
   
    # plt.bar(weather_changes['Дата'], weather_changes['Ночь'])
    # plt.bar(weather_changes['Дата'], weather_changes['День'], alpha=0.5)     
    plt.pie(weather_changes['Ночь'], labels=weather_changes['Дата'], autopct='%1.1f%%')   
    plt.show()  # открываем демонстрацию графика

# Точка входа
if __name__ == '__main__':
   main()  # вызываем функцию для запуска основной программы