def count_vowel_consonants_space(string:str):
    vowels = "aeiouAEIOU" 
    v , c , s = 0 , 0,  0 
    for i in string:
        if i in vowels:
            v += 1
        elif i == " ":
            s += 1
        else:
            c += 1
            
    print(f"vowels {v} consonants {c} space {s}")
            
if __name__ == "__main__":
    string = "Take u forward is Awesome"
    count_vowel_consonants_space(string)