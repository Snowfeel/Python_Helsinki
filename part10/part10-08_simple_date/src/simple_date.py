# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self,date:int,month:int , year:int) -> None:
        self.__date = date
        self.__month = month
        self.__year = year

    def __lt__ (self,__o:object):
        if self.__year > __o.__year:
            return True
        elif self.__year == __o.__year:
            if self.__month > __o.__month:
                return True
            elif self.__month == __o.__month:
                if self.__date > __o.__date:
                    return True
        return False
    
    def __lt__ (self,__o:object):
        if self.__year < __o.__year:
            return True
        elif self.__year == __o.__year:
            if self.__month < __o.__month:
                return True
            elif self.__month == __o.__month:
                if self.__date < __o.__date:
                    return True
        return False

    def __eq__(self, __o: object):
        if self.__year == __o.__year:
            if self.__month == __o.__month:
                if self.__date == __o.__date:
                    return True
        return False

    def __ne__(self, __o: object):
        if self.__year == __o.__year:
            if self.__month == __o.__month:
                if self.__date == __o.__date:
                    return False
        return True

    def __str__(self) -> str:
        return f'{self.__date}.{self.__month}.{self.__year}'

    def __add__(self,__day:int):
        new_date = self.__date + __day % 30
        new_month = self.__month + __day // 30
        new_year = self.__year
        if new_date > 30:
            new_month += new_date // 30
            new_date %= 30
        if new_month > 12:
            new_year += new_month // 12
            new_month %= 12
        return SimpleDate(new_date,new_month,new_year)

    def __sub__(self,__o:object):
        date_self = self.__date + self.__month * 30 + self.__year * 360
        date_o = __o.__date + __o.__month * 30 + __o.__year * 360
        return abs(date_self-date_o)