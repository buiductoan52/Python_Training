print("Hello", "Python")    # Hello Python
print(1, 2, 3, 4, 5)            # 1 2 3 4 5     .In trên cùng 1 hàng ngăn cách nhau bằng space
# muốn chèn vào giữa 1 space và %
print(1, 2, 3, 4, 5, sep=" %")  # 1 %2 %3 %4 %5 
print(6)                        # 6
# Nếu muốn print (1, 2, 3, 4, 5, sep=" %") và 6 trên cùng 1 dòng thì chi cần thêm end = ' '
print(1, 2, 3, 4, 5, sep=" %", end=' ')         # 1 %2 %3 %4 %5 6   # Nếu muốn cho xuống dòng thì end='\n'
print(6) 

 # tab
print("\tHello\t2027") 

# Biến
x = 5
print(type(x))  #<class 'int'>
y = 5.6
print(type(x))  #<class 'float'>

#
x = 3
y = 4
print(x + y) # 7
print(x - y) # -1
print(x / y) # 0.75, kq là float
print(x // y) # 0 , chia lấy phần nguyên, lưu ý cả 2 số x,y là int
print(x ** y) # 81

# Nêu chỉ cần 1 trong 2 số x và y là float thì kq là float
x = 3.4
y = 4.5
print(x // y)   # 0.0 float

# Kiểu dữ liệu : int float oject bool str ... trong python mọi thứ đều là đối tượng
# các toán tử : 
    # + - * / // **
    # > < >= <= == !=  ==> kq False/True
    # and or not

# comment trên 1 dòng or nhấn Ctrl + /
""" comment trên nhiều dòng
line 1
line 2
line 3
"""
# Python operator precedence - Độ ưu tiên toán tử
print(1>2 and 3>4) # toán tử > ưu tiên hơn toán tử and nên đc thực hiện trước , False and False , kq là False

# Lưu ý toán tử and , or
print(bool(1))  # True
print(bool(0))  # False

    # and
print(1 and 2) # 2          1 nhân với bất cứ số nào cũng bằng chính số đó
                                # True thì trả về giá trị thứ 2, False thì trả về giá trị thứ nhất 
print(0 and 2) # 0          0 nhân với bất cứ số nào cũng bằng 0  
   
    # or
print(0 or 1)  # 1          0 cộng với bất cứ số nào cũng bằng chính số đó (0+0=0, 0+1=1, 1+0=1 )
                                # 1+1=1
                                # Nếu True trả về gtri thứ nhất, False trả ve gtri thứ hai
# toán tử not
print(not True) # False
print(not 3)    # False         # 3 là khác 0 nên 3 là True, mà not True thì là False

print(not False) # True
print(not 0)    # True          # 0 là False, not False là True

#-----------------------------------------------------
# Chuỗi str
s = "hello wOrld! "
print(s*3)  # Hello World!  Hello World!  Hello World! 
print(s.upper())
print(s.lower())
print(s.title())    # Hello World!           # In hoa các chữ cái đầu của các từ trong chuỗi
print(s.capitalize()) # Hello world!        # Chỉ in Hoa chữ cái đầu của chuỗi

# Định dạng chuỗi
age = 34
print(f"I am {age}") # I am 34          # biến số 34 thành dạng str "34" khi đặt trong dấu {}
# hoặc
print("I am", age) # I am 34
print("I am " + str(age)) # I am 34
print( "I am {}".format(age)) # I am 34

# Nhập dữ liệu từ bàn phím
user_name = input("Enter your user name: ") #Enter your user name: 123
print(user_name)    # 123

# usd = input("nhập vào usd: ") # mặc định kiểu dữ liệu vào sẽ là chuỗi
# print(usd*24000) # kq sẽ ra 24 nghìn lần số 2 ,nên ta phải chuyển kiểu giá trị input ban đầu từ str sang float

usd = float(input("nhập vào usd: "))    #  2
print(usd*24000) # 48000.0 

# Search và tim các hàm Python Built-in Functions trên docs.python.org
print(type(1 +5j))  # <class 'complex'>
print(abs(1 +5j))   # 5.0990195135927845    # Trả về kích thước của số phức
print(26 ** 0.5)    # 5.0990195135927845    # Kiểm tra bằng công thức lại thì thấy kết quả như nhau

    # abs, max , ...

# --------------------------------------------------------------------------------------------------
# Hàm if    else
age = 18
if age >= 18: 
    print("Được uống bia")
else:
    print("Uống nước ngọt ")

#   if    elif    else
number = -4
if number > 0:
    print("số dương")
elif number == 0:
    print(" số 0")
else:
    print("số âm")
    
