def Capitalize_first_and_last_char(string:str):
    n = len(string) -1
    result = string[0].upper() + string[1:n -1] + string[n].upper()
    print(result)
    
    
string = 'take u forward is awesome'
Capitalize_first_and_last_char(string)