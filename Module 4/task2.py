def prepare_data(data):
    data = sorted(data)
    data.pop(0)
    data = sorted(data)
    data.pop()
    new_data = sorted(data)
    return new_data
    
my_list = [1, 12, 3, 25,56,4,345,45,45,2,34,5,6,7]
print(prepare_data(my_list))  # [1, 3.1415, 30, 41, 3]  
