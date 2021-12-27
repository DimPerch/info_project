import random

ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ "
RIMALPHABET = "XIV"


class Code(str):
    def __init__(self, string: str):
        check = Code.check(string)
        self.result = "ОШИБКА ИСХОДНЫХ ДАННЫХ"
        if check:
            result = Code.run(string)
            self.result = result
            


    @staticmethod
    def check(string):
        result = False
        if all([i in ALPHABET for i in string]):
            result = True
        return result


    @staticmethod
    def run(string):
        result = ''
        result1 = []
        for i in range(len(string)):
            result = result + str(ALPHABET.index(string[i]) + 10)
            if i != len(string) - 1:
                result = result + str(random.randint(10,19))
        i = 0
        g = 4
        for i in range(0, len(result), 2):
            perevod = ''
            if g > 9:
                g = 4
            a = int(result[i:i+2])
            if g % 2 == 0:
                while a >= g:
                    perevod = perevod + str(a % g)
                    a = a // g
                if a == g:
                    perevod = perevod + str(1)
                else:
                    perevod = perevod + str(a)
                perevod = perevod[::-1]
            else:
                arr = [1]
                x = 2
                j = 1
                while x <= a:
                    arr.append(x)
                    x = arr[j] + arr[j - 1]
                    j += 1
                x = 0
                j -= 1
                while x != a:
                    if x + arr[j] <= a:
                        x += arr[j]
                        perevod = perevod + "1"
                    else:
                        perevod = perevod + "0"
                    j -= 1
                if (len(perevod) != len(arr)):
                    n = len(arr) - len(perevod)
                    for s in range(n):
                        perevod = perevod + "0"
            result1 += perevod
            g += 1
            perevod = ''
            if i+2 != len(result):
                x = random.randint(1,10)
                for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                                            'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
                    perevod += x // arabic * roman
                    x %= arabic
                result1 += perevod
        return("".join(result1))


class Decode(str):
    def __init__(self, string: str):
        check = Decode.check(string)
        if check:
            string = Decode.run(string)
            self.result = string

    @staticmethod
    def to10ss(x, ss):
        r = 0
        d = 0
        while x > 0:
            d = d + x % 10 * ss ** r
            r += 1
            x //= 10
        return d

    @staticmethod
    def check(string):
        return True


    @staticmethod
    def run(string):
        result = ''
        result1 = []
        i = 0
        g = 4
        while i < len(string):
            if RIMALPHABET.find(string[i]) != -1:
                a = int(string[:i])
                n = Decode.to10ss(a, g)
                result = result + str(n)
                if g == 8:
                    g = 4
                else:
                    g += 2
                string = string[i:]
                i = 0
                while RIMALPHABET.find(string[i]) != -1:
                    i += 1
                string = string[i:]
                i = 0
                while RIMALPHABET.find(string[i]) == -1:
                    i += 1
                string = string[i:]
                i = 0
                while RIMALPHABET.find(string[i]) != -1:
                    i += 1
                string = string[i:]
                i = 0
            i += 1
        a = int(string)
        n = Decode.to10ss(a, g)
        result = result + str(n)
        for i in range(0, len(result), 2):
            n = int(result[i:i+2]) - 10
            result1.append(ALPHABET[n])
        return("".join(result1))