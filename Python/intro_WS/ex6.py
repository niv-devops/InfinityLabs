# Approved by: Matan

def sum_divisors(num):
    """ Return sum of all dividors of given number """
    sum = 0
    for i in range(1, int(num/2) + 1):
        if num % i == 0:
            sum += i
    return sum+num


if __name__ == "__main__":
    num = 9
    print("6) Sum of", num, "diviosors:", sum_divisors(num))