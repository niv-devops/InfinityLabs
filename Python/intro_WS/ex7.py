# Approved by: Matan

def break_fiat(money):
    """ Return minimum amount of bills and coins needed for given amount of money """
    fiat = [200, 100, 50, 20, 10, 5, 2, 1]
    bills = {}
    if money <= 0:
        return bills
    for x in fiat:
        count = money // x
        if count > 0:
            bills[x] = count
            money %= x
    return bills


if __name__ == "__main__":
    money = 378
    print("7) Minimum fiats: ", break_fiat(money))