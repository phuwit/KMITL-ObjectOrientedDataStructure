"""
Chapter : 6 - item : 2 - Length of a String EXTRA

ให้นักศึกษาเขียนฟังก์ชันที่ทำงานเหมือนกับฟังก์ชัน len() เพื่อหาความยาวของ string และแสดงผลดังตัวอย่าง(print ตัวอักษรตามด้วยเครื่องหมายพิเศษสลับกันคู่คี่)

****ห้ามใช้คำสั่ง len, for, while, do while, split*****

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว
def length(txt):
    #Code Here
print("\\n",length(input("Enter Input : ")),sep="")
#ตรง print(เป็นแค่ตัวอย่างสามารถแก้ไขได้)

Enter Input : hello
h*e~l*l~o*
5

Enter Input : data structure is easy
d*a~t*a~ *s~t*r~u*c~t*u~r*e~ *i~s* ~e*a~s*y~
22

Enter Input : *~*~*~
**~~**~~**~~
6
"""

txt_symbol = ""


def length(txt):
    global txt_symbol
    if not txt:
        return 0

    if txt_symbol == "*":
        txt_symbol = "~"
    else:
        txt_symbol = "*"

    print(f"{txt[0]}{txt_symbol}", sep="", end="")

    return 1 + length(txt[1::])


print("\n", length(input("Enter Input : ")), sep="")
