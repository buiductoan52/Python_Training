# Trong 1 list các phần tử có thể trùng lặp
#  Index ( Chỉ số)
# index    0    1    2    3   4    
#         -5   -4   -3   -2  -1
numbers = [1, 2, 3, 4, 5]
print(numbers[1]) # 2

# .append(value)    Thêm phần tử vào cuối list
numbers.append(100) #  [1, 2, 3, 4, 5, 100] # thêm 100 vào cuối List 
print(numbers)

# .pop()    Lấy ra giá trị cuối cùng trong list, List đó sẽ mất đi phần tử vừa lấy ra
lst_numbers = [1, 2, 3, 4, 1]
last_value = lst_numbers.pop()
print(last_value)   # 1
print(lst_numbers)  # [1, 2, 3, 4]

# .extend([list])       Mở rộng list từ cuối list
lst_numbers = [1, 2, 3, 4, 1]
lst_numbers.extend(['a', 12, 2.5])
print(lst_numbers)      # [1, 2, 3, 4, 1, 'a', 12, 2.5]

# .count(value)     Đếm số lượng value có trong list, nếu k có thì trả về 0
lst_numbers = [1, 2, 3, 4, 1]
int_amount1 = lst_numbers.count(1) 
int_amount2 = lst_numbers.count(100) 
print(int_amount1)   # 2
print(int_amount2)   # 0

# .clear()   Xoá toàn bộ phần tử trong list -- > []
lst_numbers.clear()
print(lst_numbers) # []

# del list[index]   Xoá phần tử dựa vào index

# .remove(value)    Xoá phần tử dựa vào giá trị, 
#                   xoá value đầu tiên gặp được trong list từ trái qua phải
#                   , nếu k tìm thấy thì sẽ báo lôi
numbers = [1, 2, 3, 4, 1]
numbers.remove(1) # [2, 3, 4, 1]    Chỉ xoá phần tử có giá trị là 1 đầu tiên
# numbers.remove(-100) # xoá một giá trị k tồn tại trong list thì sẽ báo lỗi
print(numbers)
# 

# len(list_name)        Đếm số lượng phần tử( items) có trong list
lst_numbers = [1, 2, 3, 4, 1]
amount = len(lst_numbers)
print(amount)       # 5

# .insert(index, value)     
# Chèn vào 1 value tại vị trí Index của list, và value cũ tại vị trị Index sẽ đẩy về bên phải
lst_numbers = [1, 2, 3, 4, 1]
lst_numbers.insert(2, 1000)
print(lst_numbers)      # [1, 2, 1000, 3, 4, 1]

# .index(value)     Trả về Index tương ứng với value đc truyền có trong list, 
#                   nếu value k có trong list thì sẽ báo lỗi
lst_numbers = [1, 2, 3, 4, 1]
Index_value1 = lst_numbers.index(4)
print(Index_value1)     # 3

# Index_value2 = lst_numbers.index(10)  
# print(Index_value2)    # báo lỗi 

# .reverse()        Đảo ngược phần tử trong list
lst_numbers = [1, 2, 3, 4]
lst_numbers.reverse()
print(lst_numbers)  # [4, 3, 2, 1]

# .sort()               Sắp xếp tăng dần
# .sort(reverse=True)   Sắp xếp giảm dần 
lst_numbers = [1, 2, 3, 4, 1]
# lst_numbers.sort() # sắp xếp tăng dần
lst_numbers.sort(reverse=True) # sắp xêp giảm dần, [4, 3, 2, 1, 1]
print(lst_numbers)

# max(list)     Tìm số lớn nhất
# min(list)     Tìm số nhỏ nhất


# In ra tất cả các phương thức và hàm của List
print(dir(list))

# Tham khảo thời gian chạy của các hàm : Timecomplexity