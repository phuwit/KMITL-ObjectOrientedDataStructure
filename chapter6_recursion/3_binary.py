"""
**I FEEL LIKE I CHEATED!**

Chapter : 6 - item : 3 - ( 2^(input) ) - 1

****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive เพื่อหาว่าเลขตั้งแต่ 0 จนถึง ( 2^(input) ) - 1 นั้นมีตัวอะไรบ้าง  หากเป็นเลขติดลบให้แสดงผลเป็น Only Positive & Zero Number ! ! !

*** ตัวอย่างเช่น ถ้าหาก input = 2 ก็ต้องแสดงผลลัพธ์เป็น 00 , 01 , 10 , 11

Enter Number : -1
Only Positive & Zero Number ! ! !

Enter Number : 0
0

Enter Number : 1
0
1

Enter Number : 4
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
"""

padding = int(input("Enter Number : "))

if padding < 0:
    print("Only Positive & Zero Number ! ! !")
    exit()

target = (2**padding) - 1


def get_binary(current):
    if current > target:
        return ""
    return f"{current:0{padding}b}\n{get_binary(current+1)}"


print(get_binary(0))
