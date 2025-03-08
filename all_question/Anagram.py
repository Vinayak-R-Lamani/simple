def arr_anagram(str1 , str2):
    return sorted(str1) == sorted(str2)


def arr_anagram_2(str1 , str2):
    if len(str2) != len(str1):
        return False
    
    count = [0] * 26

print(arr_anagram("listen","silent"))
print(arr_anagram("hello ", "world"))