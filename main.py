""" Головний модуль задачі
- Виводить розрахункову табліцю на екран та в файл
- Виводить первинні данні на екран
"""

import os
from process_data import income_gross
from data_service import show_dovidniks, show_tovaroobigs, get_dovidnik, get_tovaroobig

MAIN_MENU = \
""" 
~~~~~~~~~~   ОБРОБКА ВАЛОВОГО ДОХОДУ УНІВЕРМАГУ   ~~~~~~~~~

1 - Вивід таблиці валового доходу універмагу на екран
2 - Запис таблиці валового доходу універмагу в файл
3 - Вивід списка товарообігу універмагу
4 - Вивід списка довідника товарних груп
0 - Завершення роботи

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

TITLE = "ВАЛОВИЙ ДОХІД УНІВЕРМАГУ НА ПОТОЧНИЙ РІК"

HEADER = \
"""
================================================================================================================
Найменування        |   Рік   |        Товарообіг, тис.крб.      |   Торгова   |     Валовий дохід, тис.крб.
товарної групи      |         |   План   |  Очіковане виконання  |  скидка, %  |   План   |  Очіковане виконання
================================================================================================================
"""

FOOTER =  \
'''
================================================================================================================

'''

STOP_MESSAGE = 'Для продовження натисніть <Enter> '

def show_income(income_list):
    """ Виводить таблицю валового доходу

    Args:
        income_list ([type]): Список доходу
    """
    print(f"\n\n{TITLE:^113}")
    print(HEADER)

    for income in income_list:
        print(f"{income['name_product']:20}",
              f"{income['year']:^9}",
              f"{income['plan_1']:^10}",
              f"{income['inplementation_1']:^23}",
              f"{income['discount']:^13}",
              f"{income['plan_2']:^10}",
              f"{income['inplementation_2']:^21}")

    print(FOOTER)

def write_income(income_list):
    """ Записує список валового доходу у текстовий файл

    Args:
        income_list ([type]): список доходу
    """

    with open('./data/income.txt', 'w') as income_file:
        for income in income_list:
            line = \
               income['name_product'] + ';' +                \
               str(income['year']) + ';' +                   \
               str(income['plan_1']) + ';' +                 \
               str(income['inplementation_1']) + ';' +       \
               str(income['discount']) + ';' +               \
               str(income['plan_2']) + ';' +                 \
               str(income['inplementation_2'])  + '\n' 
               
            income_file.write(line)  
            
    print('Файл успішно записано...')     

while True:

    # Виводить головне меню
    os.system('cls')
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")

    # Обробка команд користувача
    if command_number == '0':
        print('Програма завершила роботу')
        exit(0)

    elif command_number == '1':
        income_list = income_gross()
        show_income(income_list)
        input(STOP_MESSAGE)

    elif command_number == '2':
        income_list = income_gross()
        write_income(income_list)
        input(STOP_MESSAGE)
        
    elif command_number == '3':
        tovaroobigs = get_tovaroobig()
        show_tovaroobigs(tovaroobigs)
        input(STOP_MESSAGE)
        
    elif command_number == '4':
        dovidniks = get_dovidnik()
        show_dovidniks(dovidniks)
        input(STOP_MESSAGE)