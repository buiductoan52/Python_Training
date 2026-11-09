from pprint import pprint 

lst_film = ["Công chúa ngủ trong rừng",
            "Công chúa ngủ gật",
             "Bạch tuyết và 7 chú lùn",
              "Giang hồ chi cần 1",
               "Thiên đường cua càng xanh" ]

print(lst_film )    # hàm print chỉ in trên 1 hàng , nhìn k thẩm mỹ
# Để đẹp hơn sd import hàm pprint từ thư viện pprint : < from pprint import pprint >
pprint(lst_film)
    #['Công chúa ngủ trong rừng',
    # 'Công chúa ngủ gật',
    # 'Bạch tuyết và 7 chú lùn',
    # 'Giang hồ chi cần 1',
    # 'Thiên đường cua càng xanh']

# -----------------------------------
"""
+ list in list
+ copy list
+ list slicing
"""
# list in list
friends = [["Bod", 23], ["Jen", 34], ["Kenny", 56]]
print(type(friends))
print(friends[0][0])    # Bod
print(friends[0][1])    # 23

# Nếu gán theo kiểu này thì 2 list sẽ trùng địa chỉ bộ nhớ
lst1 = [1,2,3]
lst2 = lst1

print(lst1 is lst2)     # Kiểm tra vị trí 2 list có trùng 1 địa chỉ bộ nhớ không? --> True
print(lst1 == lst2)     # so sánh nội dung 2 list có giống nhau không ?-->True

# .copy()   Sd copy list để giải quyết vấn đề trùng địa chỉ bộ nhớ
lst1 = [1,2,3]
lst2 = lst1.copy()      # copy 1 bản lst1 và gán bản copy đó cho lst2

print(lst1 is lst2)     # False
print(lst1 == lst2)     # True

# list1 is list2   So sánh địa chỉ bộ nhớ (ID) của 2 list có giống hay khác nhau? --> True/False
# id(oject)        Hàm hiển thị ID của 1 đối tượng được truyền vào
print(id(lst1), id(lst2))       # 1994357865152 1994359472192

# list[from : to-1 : bước nhảy]     , bước nhảy mặc định là 1
    # Goi là list slicing --> lấy các phần tử ra và tạo thành 1 list mới với id khác 
a = [1, 2, 4, 0, 100]
new_lst = a[:2]    # hoặc a[0:2], --> [1, 2]
new_lst = a[1:]     # [2, 4, 0, 100]
new_lst = a[:]     # Lấy toàn bộ phần tử  [1, 2, 4, 0, 100]
new_lst = a[1:-1]     # [2, 4, 0] , có thể sd chỉ số âm 
new_lst = a[1:4]      # [2, 4, 0] , dùng chỉ số dương

new_lst = a[::-1]   # [100, 0, 4, 2, 1] , lấy ngược list
print(new_lst)

print(new_lst is a) # False