# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"

    def __eq__(self, __o: object):
        if self.__euros == __o.euros:
            if self.__cents == __o.cents:
                return True
        return False

    def __lt__(self,__o: object):
        if self.__euros < __o.euros:
            return True
        elif self.__euros == __o.euros:
            if self.__cents < __o.cents:
                return True
        return False

    def __gt__(self,__o: object):
        if self.__euros > __o.euros:
            return True
        elif self.__euros == __o.euros:
            if self.__cents > __o.cents:
                return True
        return False

    def __ne__(self,__o: object):
        if self.__euros != __o.euros:
            return True
        elif self.__euros == __o.euros:
            if self.__cents != __o.cents:
                return True
        return False

    def __add__ (self,__o:object):
        euros = self.__euros+__o.euros
        cents = self.__cents+__o.cents
        if cents >= 100:
            euros += 1
            cents -= 100
        return Money(euros,cents)

    def __sub__ (self,__o:object):
        euros = self.__euros - __o.euros
        cents = self.__cents - __o.cents
        if cents < 0:
            euros -= 1
            cents += 100
        if euros < 0:
            raise ValueError(f"a negative result is not allowed")
        return Money(euros,cents)