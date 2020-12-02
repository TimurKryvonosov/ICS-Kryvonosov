""" Валовий доходу універмагу на поточний рік
"""

# Підключити функції з модуля 'data_service'
from data_service import get_tovaroobig, get_dovidnik

# Структура аналізу руху основних засобів вихідних даних
income = {
    'name_product'         : '',    # Найменування товарної групи 
    'year'                 : 0,     # Рік
    'plan_1'               : 0,     # План товарообігу
    'inplementation_1'     : 0,     # Очіковане виконання товаообігу
    'discount'             : 0.0,   # Торгова скидка
    'plan_2'               : 0,     # План валового доходу
    'inplementation_2'     : 0      # Очіковане виконання валового доходу
}


tovaroobigs = get_tovaroobig()
dovidniks = get_dovidnik()

def income_gross():
    """ Формування валового доходу універмагу
    """

    def get_dovidnik_name(dovidnik_code):
        """ Повертає назву засоба по його коду

        Args:
            dovidnik_name ([type]): код засоба

        Returns:
            [type]: назва засобу
        """

        for dovidnik in dovidniks:
            if dovidnik[0] == dovidnik_code:
                return dovidnik[1]

        return "*** Код засобу не знайдений"

    # Накопичувач валового доходу універмагу
    income_list = []

    for tovaroobig in tovaroobigs:

        # Створити копію шаблона
        income_tmp = income.copy()

        income_tmp['name_product'] = get_dovidnik_name(tovaroobig[1])
        income_tmp['year'] = tovaroobig[3]
        income_tmp['plan_1'] = tovaroobig[1]
        income_tmp['inplementation_1'] = tovaroobig[2]
        income_tmp['discount'] = get_dovidnik_name(tovaroobig[2])
        income_tmp['plan_2'] = income_tmp['plan_1'] * income_tmp['discount'] 
        income_tmp['inplementation_2'] = income_tmp['inplementation_1'] * income_tmp['discount'] 

        income_list.append(income_tmp)

    return income_list

result = income_gross()

for r in result:
    print(r)