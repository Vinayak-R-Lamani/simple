import sys
def sum_number_range(l ,r):
    return sum(x for x in range(l,r+1))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python script.py <number>')
    else:
        try:
            l = int(sys.argv[1])
            r = int(sys.argv[2])
            print(sum_number_range(l,r))
        except ValueError:
            print('Invalid number')