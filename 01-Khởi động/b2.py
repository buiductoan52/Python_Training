# Value -  giá trị
# Value types - kiểu giá trị( numbers, string, boolean,complex )
    # complex : a +bj với a-phần thực, b-phần ảo, j-đơn vị ảo với j*2 = -1
    # Trong Work muốn viêt số mũ (chỉ số trên): Ctrl +Shift + =
    # Trong Work viết chỉ số dưới : Ctrl + =
# Input -->str
# Variables - biến 
    # khi đặt tên biến phải gán đi kèm với nó 1 giá trị
    # tên hằng số phải in Hoa, vd: PI = 3.14
# Nên dùng các tên file như : app.py     test.py     main.py    demo.py
# Gán 2 biến cùng giá trị
num1 = num2 = 5 
print(type(num1))
print(num1,num2)

# ------yêu cầu 1-------------

a = "|"
name = "toan"
age = 38
print(f'{name} {a} {age}')              # toan | 38
print("{} {} {}".format(name,a,age))    # toan | 38
print("%s %s %s" %(name,a,age) )        # toan | 38

print("%s %s %s" %('toan','|',38) )        # toan | 38

# --------yêu cầu 2------------

a_as_int = int(input("nhập số nguyên: "))
b_as_float = float(input("nhập số thực: "))
c_as_string = input("nhập chuỗi: ")

print(a_as_int)
print(b_as_float)
print(c_as_string)
# ------------------------------

print("hello")
print("hello")


