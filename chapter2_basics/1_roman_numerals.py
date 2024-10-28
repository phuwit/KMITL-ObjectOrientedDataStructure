# Chapter : 2 - item : 1 - roman number

# จงเขียนฟังชั่นแปลง เลขอารบิกเป็นเลขโรมัน และ เลขโรมันเป็นอารบิกโดยที่

# M=1000    CM=900    D=500    CD=400,

# C=100    XC=90    L=50    XL=40,

# X=10    IX=9    V=5    IV=4    I=1

# เช่น 197 = 100 + 90 +7 = 100 + 90 + 5 + 1 + 1 = C XC V I I

# (https://roman-numerals.info/)


class Translator:
    __symbols = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    def decimal_to_roman(self, num: int):
        roman = ""
        for symbol, value in self.__symbols.items():
            while num >= value:
                roman += symbol
                num -= value
        return roman

    def roman_to_decimal(self, string: str):
        digit_values = [self.__symbols[char] for char in string][::-1]
        # print(digit_values)
        subtract_value = 0
        subtotal = 0
        cursor: int = 0
        while cursor < (len(digit_values) - 1):
            if digit_values[cursor] > digit_values[cursor + 1]:
                subtract_value += digit_values.pop(cursor + 1)
            cursor += 1

        for i in digit_values:
            subtotal += i
        # print(subtotal, subtract_value)
        return subtotal - subtract_value


number = int(input("Enter number to translate : "))

print(Translator().decimal_to_roman(number))
print(Translator().roman_to_decimal(Translator().decimal_to_roman(number)))
