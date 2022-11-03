# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls,my_list: list):
        freq = {}
        for i in my_list:
            if i not in freq:
                freq[i] = my_list.count(i)
        result = 0
        count = 0
        for i in freq:
            if freq[i] > count:
                result = i
                count = freq[i]
        return result

    @classmethod
    def doubles(cls,my_list: list):
        dou = []
        count = []
        for i in my_list:
            if i not in count:
                count.append(i)
            else:
                if i not in dou:
                    dou.append(i)
        return len(dou)
        
        