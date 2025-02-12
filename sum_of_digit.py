import sys
def sum_digits(n):
    return sum(int(i) for i in str(n))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python script.py <number>')
    else:
        try:
            n = int(sys.argv[1])
            print(sum_digits(n))
        except ValueError:
            print('Invalid number')