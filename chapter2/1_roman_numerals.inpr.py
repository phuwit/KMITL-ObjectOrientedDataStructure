# Chapter : 2 - item : 1 - roman number

# จงเขียนฟังชั่นแปลง เลขอารบิกเป็นเลขโรมัน และ เลขโรมันเป็นอารบิกโดยที่

# M=1000    CM=900    D=500    CD=400,

# C=100    XC=90    L=50    XL=40,

# X=10    IX=9    V=5    IV=4    I=1

# เช่น 197 = 100 + 90 +7 = 100 + 90 + 5 + 1 + 1 = C XC V I I

# (https://roman-numerals.info/)


class Translator:
    __symbols = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400,
        "C": 100, "XC": 90, "L": 50, "XL": 40,
        "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
    }

    def decimal_to_roman(self, num: int):
        roman = ''
        for symbol, value in self.__symbols.items():
            while num >= value:
                roman += symbol
                num -= value
        return roman

    def roman_to_decimal(self, string: str):
        total = 0
        previous_value = 0
        symbols = reversed(string)
        for symbol, value in reversed(self.__symbols.items()):
            for current_symbol in symbols:
                if current_symbol == symbol:
                    if value > previous_value:
                        total += value
                    previous_value = value
                elif value > 
                    total -= previous_value
                else:
                    break
        return total

number = int(input("Enter number to translate : "))

print(Translator().decimal_to_roman(number))
print(Translator().roman_to_decimal(Translator().decimal_to_roman(number)))
