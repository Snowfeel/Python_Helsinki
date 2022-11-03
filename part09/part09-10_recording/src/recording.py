# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self,length :int):
        if length > -1:
            self.__length = length
        else:
            raise ValueError
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self,length: int):
        if length > -1:
            self.__length = length
        else:
            raise ValueError