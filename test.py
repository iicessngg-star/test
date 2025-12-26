name = input("กรอกชื่อ: ")
print(f"ชื่อ {name} ")
age = int(input("กรอกอายุ: "))
print(f"อายุ {age} ปี")
print(f"ปีหน้าอายุ {age+1} ปี")
price = int(input("กรอกราคา: "))
vat_rate = 7 / 100     
vat = price * vat_rate
total = price + vat
print(f"ราคาสินค้า {price} บาท")
print(f"ภาษี 7% = {vat:.2f} บาท")
print(f"รวมทั้งหมด = {total:.2f} บาท")

score = int(input("กรอกคะแนน (1-100): "))

if 1 <= score <= 100:
    if score < 50:
        grade = "F"
    elif score < 60:
        grade = "D"
    elif score < 70:
        grade = "C"
    elif score < 80:
        grade = "B"
    else:
        grade = "A"
    print(f"คุณได้ {score} คะแนน เกรด {grade}")
else:
    grade = None
    print("⚠️ คะแนนไม่ถูกต้อง")


answer = input("สนใจสาย AI ไหม (y/n): ")

if answer == "y":
    is_ai = "สนใจ"
else:
    is_ai = "ไม่สนใจ"

print(f"{is_ai}สาย AI ")

print(f"ชื่อ {name} อายุ")
print(f"อายุ {age} ปี")
print(f"ปีหน้าอายุ {age+1} ปี")
print(f"ราคาสินค้า {price} บาท")
print(f"ภาษี 7% = {vat:.2f} บาท")
print(f"รวมทั้งหมด = {total:.2f} บาท")
print(f"คุณได้ {score} คะแนน เกรด {grade}")
print(f"คุณ{is_ai}สาย AI ")