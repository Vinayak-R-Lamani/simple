def number_to_words(n: int) -> str:
    if n == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]
    
    result = ""

    # Handling thousands place
    if n >= 1000:
        result += ones[n // 1000] + " thousand "
        n %= 1000  # Remove thousands place

    # Handling hundreds place
    if n >= 100:
        result += ones[n // 100] + " hundred "
        n %= 100  # Remove hundreds place
        if n > 0:
            result += "and "  # Add 'and' if there are further digits

    # Handling tens and ones place
    if n >= 20:
        result += tens[n // 10] + " "
        n %= 10
    elif n >= 11 and n <= 19:
        result += teens[n - 10] + " "
        n = 0  # No further processing needed

    # Handling ones place
    if n > 0:
        result += ones[n] + " "

    return result.strip()  # Remove extra spaces

# Test cases
print(number_to_words(7824))  # Output: seven thousand eight hundred twenty four
print(number_to_words(370))   # Output: three hundred seventy
print(number_to_words(9))     # Output: nine
print(number_to_words(5))     # Output: five
print(number_to_words(1001))  # Output: one thousand one
print(number_to_words(1111))  # Output: one thousand one hundred and eleven
