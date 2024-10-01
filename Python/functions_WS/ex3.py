# Approved by: Arin

lst = [-5, 10, -10, -7, 17, 2]
lst_pos_sum = sum(list(filter(lambda x: x>0, lst)))
lst_neg_sum = sum(list(filter(lambda x: x<0, lst)))
print("Positive sum:", lst_pos_sum, "| Negative sum:", lst_neg_sum)

""" Another solution: 
lst_pos_sum = sum(x for x in lst if (lambda x: x>0)(x))
lst_neg_sum = sum(x for x in lst if (lambda x: x<0)(x)) """