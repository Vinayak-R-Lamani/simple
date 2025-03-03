import re
def sum_of_numbers_in_string(string:str):
    total_sum = 0
    current_number = ""
    for char in string:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                total_sum += int(current_number)
                current_number = ''
                
    if current_number:
        total_sum += int(current_number)
        
    print(total_sum)
    
    
def sum_of_number(string:str):
    numbers = re.findall(r'\d+',string)
    print(sum(map(int,numbers)))
if __name__ == "__main__":
    string = "123abc456efg789"
    sum_of_number(string)