# https://twigstechtips.blogspot.mx/2011/06/python-calculate-firstlast-monday.html
import calendar
import datetime

def dates():
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    your_date = datetime.date.today()

    date = list()

    for i in range(1, 5, 1):
        month = your_date.month + i
        year = your_date.year
        if month > 12:
            month = month - 12
            year = year + 1
        # Get the first "day" of the month and the number of days in the month  0 1 2 3 4 5 6
        month_range = calendar.monthrange(year, month)
        month_name = months[month - 1]
        if month_range[0] == 6:
            day = 1 + 6
        else:
            day = 1 + (6 - (month_range[0] + 1))

        date.append('Sábado ' + str(day) + ' de ' + str(month_name) + ' de ' + str(year))
    return date
