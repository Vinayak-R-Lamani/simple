def octal_to_binary(octal:int) -> str:
    octal_to_binary_map = {
        '0' : '000',
        '1' : '001',
        '2' : '010',
        '3' : '011',
        '4' : '100',
        '5' : '101',
        '6' : '110',
        '7' : '111'
    }
    
    octal_str = str(octal)
    binary_str = ''.join(octal_to_binary_map[digit] for digit in octal_str )
    binary_str = binary_str.lstrip('0')
    print(binary_str) if binary_str else print('0')
    
    
if __name__ == "__main__":
    octal_number = 345
    octal_to_binary(octal_number)