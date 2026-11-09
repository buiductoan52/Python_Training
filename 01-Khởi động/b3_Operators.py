# Toán tử : + - * / // %
print(3//2) # 1, chia lấy phần nguyên
print(3%2)  # 1, chia lấy phần dư
# Toán tử so sánh : > < >= <= == !=
# Biểu thức so sánh: x > y, x == y, ...
# Toán tử : and or not
    # and,  chỉ cần có False kq là False
        # True and True -> True
        # True and False ->False
        # False and True ->False
        # False and False ->False

    # or , chỉ cần có True thì kq là True
        # True or True -> True
        # True or False ->True
        # False or True ->True
        # False or False ->False

    # not
        # print( not True) -> False
        # print( not False) -> True
   
# Thực tế của and:
    # print(value1 and value2) 
    # bool(value1) , nếu True thì lấy value2, ngược lại False thì lấy value1
print(1 and 2) # bool(1)= True , nên kq là 2
print(1 and 0) # bool(1)= True, nên kq là 0
print(0 and 5) # bool(0)= False, nên kq là 0
# Thực tế của or thì ngược lại với and
    # print(value1 and value2) 
    # bool(value1) , nếu False thì lấy value2, ngược lại True thì lấy value1

# not
print(not 1) # False
print(not 0) # True

# Các Falsy khi truyền vào hàm bool() --> False
    # 0  0.0   0j   None : tức no value
    # List trống : []
    # Set trông  : set()
    # Dict trống : {}
    # Tupple trống: ()
    # Chuỗi trống: '' , ""

# Toán tử Gán +=, -=, *=, /=, //=, %=, **=

x = 5
x += 5      # x = x + 5
x -= 9      # x = x - 9
x *= 12     # x = x * 12
x /= 7      # x = x / 7
print("x =",x)

# ----------------------------------------------
# BÀI TẬP
num1 = int(input("nhập vào số nguyên number 1: "))
num2 = int(input("nhập vào số nguyên number 2: "))

print(num1,"+",num2,"=",num1 + num2)
print(num1,"-",num2,"=",num1 - num2)
print(num1,"*",num2,"=",num1 * num2)
print(num1,"/",num2,"=",num1 / num2)
print(num1,"//",num2,"=",num1 // num2)
print(num1,"%",num2,"=",num1 % num2)
print(num1,"^",num2,"=",num1 ** num2)

print(''<' ')  # True,   Lưu ý ''<' '
print(ord('a')) # 97
print(ord('b')) # 98
print('a'<'b') # True

