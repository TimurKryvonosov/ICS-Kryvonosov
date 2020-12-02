""" Модуль для отримання даних про товарообіг універмагу та вивід їх на екран
"""

def get_tovaroobig():
    """ Повертає вміст файла "tovaroobigs.txt" у вигляді списка
    Returns:
        tovaroobig_list - список рядків файла
    """

    with open('./data/tovaroobigs.txt') as tovaroobig_file:
        tovaroobig_list = tovaroobig_file.readlines()

    # Накопичувач товарообігу
    tovaroobig_drive = []

    for line in tovaroobig_list:
        line_list = line.split(';')
        line_list[3] = line_list[3][:-1]  # Видаляє '\n' в кінці
       # line_list[0] = float(line_list[0])
       # line_list[1] = float(line_list[1])
       # line_list[2] = float(line_list[2])
       # line_list[3] = float(line_list[3])
        tovaroobig_drive.append(line_list)


    return tovaroobig_drive


def show_tovaroobigs(tovaroobigs):
    """ Виводить список товарообігу

    Args:
        tovaroobigs (list): список товарообігу
    """

    # Задати інтервал виводу
    tovaroobig_code_from = input("З якого кода виду засобів виводити? ")
    tovaroobig_code_to = input("По який код виду засобів виводити? ")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for tovaroobig in tovaroobigs:
        if tovaroobig_code_from <= tovaroobig[0] <= tovaroobig_code_to:
            print("Код: {:6} План: {:6}  Очікуєме виконання: {:6}  Рік: {:6}".format(tovaroobig[0], tovaroobig[1], tovaroobig[2], tovaroobig[3]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту руху засобів нічого не знайдено.")


tovaroobigs = get_tovaroobig()
show_tovaroobigs(tovaroobigs)



def get_dovidnik():
    """ Повертає вміст файла "dovidniks.txt" у вигляді списка

    Returns:
        dovidnik_list - список рядків файла
    """

    with open('./data/dovidniks.txt', encoding="utf8") as dovidnik_file:
        dovidnik_list = dovidnik_file.readlines()

    # Накопичувач довідника товарних груп
    dovidnik_drive = []

    for line in dovidnik_list:
        line_list = line.split(';')
        line_list[2] = line_list[2][:-1]  # Видаляє '\n' в кінці
        dovidnik_drive.append(line_list)


    return dovidnik_drive


def show_dovidniks(dovidniks):
    """ Виводить список довідника

    Args:
        dovidniks (list): список довідника
    """

    # Задати інтервал виводу
    dovidnik_code_from = input("З якого кода довідника виводити? ")
    dovidnik_code_to = input("По який код довідника виводити? ")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for dovidnik in dovidniks:
        if dovidnik_code_from <= dovidnik[0] <= dovidnik_code_to:
            print("Код: {:6} Найменування: {:17} Скидка: {:5}".format(dovidnik[0], dovidnik[1], dovidnik[2]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту довідникіка нічого не знайдено.")


dovidniks = get_dovidnik()
show_dovidniks(dovidniks)