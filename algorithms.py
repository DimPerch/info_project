ALPHABET = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


class Code(str):
    def __init__(self, string: str):
        check = Code.check(string)
        if check:
            result = Code.run(string)
            


    @staticmethod
    def check(string):
        return True


    @staticmethod
    def run(string):
        return string


class Decode(str):
    def __init__(self, string: str):
        check = Decode.check(string)
        if check:
            self.result = string


    @staticmethod
    def check(string):
        return True


    @staticmethod
    def run(string):
        return string