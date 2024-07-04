# Chapter : 2 - item : 3 - game of WORD

# ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการใช้ Class สำหรับ “เกมต่อคำ” โดยจะมีกติกาดังต่อไปนี้

# 1. คำล่าสุดจะต้องไม่ซ้ำกับคำที่เคยพูดไปแล้ว เช่นถ้าหากมีคนพูดว่า “Apple” ไปก่อนหน้านั้นแล้ว
# จะไม่สามารถพูดว่า “Apple” ได้อีก

# 2. โดยการดูว่า 2 คำนั้นจะ Match กันหรือไม่ ให้ดู 2 ตัวอักษรสุดท้ายของข้อความสุดท้ายใน List กับ 2
# ตัวอักษรแรก ของคำล่าสุด เช่น [“Apple”, “lemon”] ถ้าหากคำที่จะเข้ามาเป็น “Onion” จะถือว่า Match
# แต่ถ้าหากคำที่เข้ามาเป็น “nectarine” จะถือว่าไม่ Match และเกมจะจบลงทันที

# *** TorKham HanSaa ***
# Enter Input : P apple,P lemon,P nectarine,X
# 'apple' -> ['apple']
# 'lemon' -> ['apple', 'lemon']
# 'nectarine' -> game over

# 3. Ignore Case Sensitive

# โดยจะมีรูปแบบคำสั่งดังต่อไปนี้
# - P < word > จะเป็นการต่อคำ
# - R จะเป็นการเริ่มคำใหม่ทั้งหมด
# - X เป็นการระบุว่าจบการทำงาน

# โดยใช้ class รูปแบบดังนี้


class TorKham:
    def __init__(self):
        self.__past_words: list[str] = []

    def restart(self):
        self.__past_words = []
        return "game restarted"

    def play(self, word: str):
        for past_word in self.__past_words:
            if word.lower() == past_word.lower():
                return f"'{word}' -> game over"

        if len(self.__past_words) == 0:
            self.__past_words.append(word)
        elif self.__past_words[-1][::-1][0:2:][::-1].lower() == word[0:2:].lower():
            self.__past_words.append(word)
        else:
            return f"'{word}' -> game over"
        return f"'{word}' -> {self.__past_words}"


torkham = TorKham()

print("*** TorKham HanSaa ***")
input_strings = input("Enter Input : ").split(",")

for string in input_strings:
    if string.startswith("X"):
        break
    elif string.startswith("R"):
        print(torkham.restart())
    elif string.startswith("P"):
        word = string[2::]
        print(torkham.play(word))
    else:
        print(f"'{string}' is Invalid Input !!!")
        break
