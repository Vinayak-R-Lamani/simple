def is_leap_year(year):
    return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

if __name__ == '__main__':
    year = 1700
    print(is_leap_year(year))