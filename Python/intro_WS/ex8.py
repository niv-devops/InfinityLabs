# Approved by: Matan

def is_prime(num):
    """ Return true if given number is prime """
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    num = 653
    print("8) Is", num, "a prime number?", is_prime(num))