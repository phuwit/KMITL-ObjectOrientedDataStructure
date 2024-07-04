# Chapter : 1 - item : 2 - BMI Calculate

# รับ input 2 จำนวนโดยที่ input ที่ 1 คือ h เป็นค่าความสูง(เมตร) และ Input ที่ 2 คือ w เป็นค่าน้ำหนัก(กิโลกรัม) โดยให้คำนวณหาค่า BMI ที่คำนวณจากสูตร BMI = w / (h^2) โดยให้แสดงผลตามข้อความข้างล่าง

# BMI < 18.50 แสดงผล Less Weight

# 18.50 <= BMI  < 23 แสดงผล Normal Weight

# 23 <= BMI  < 25 แสดงผล Morethan Normal Weight

# 25 <= BMI  < 30 แสดงผล Getting Fat

# BMI  >= 30 แสดงผล Fat

input_string = input("Enter your High and Weight : ")
(height, weight) = [float(n) for n in input_string.split(" ")]

bmi = weight / (height**2)

if bmi >= 30:
    print("Fat")
elif bmi >= 25:
    print("Getting Fat")
elif bmi >= 23:
    print("More than Normal Weight")
elif bmi >= 18.5:
    print("Normal Weight")
else:
    print("Less Weight")
