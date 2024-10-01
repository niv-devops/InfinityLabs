# Approved by: Amit

def luhn_algorithm(card_num):
    """ Function to check validation of credit card number """       
    rev_num = list(map(int, reversed(str(card_num))))
        
    mod_num = list(map(lambda i: rev_num[i] if i%2 == 0 else rev_num[i]*2 if \
    	rev_num[i]*2 < 9 else rev_num[i]*2 - 9, range(len(rev_num))))
    
    if sum(mod_num) % 10 == 0:
        print("Valid credit card number")
    else:
        print("Non-valid credit card number")

if __name__ == "__main__":
    luhn_algorithm(4388576018410707)