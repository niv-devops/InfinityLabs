# Approved by: Arin

lst = ["cartman", "kyle", "cartman", "kenny", "stan", "randy"]
words = ["cartman", "stan"]
lst = list(filter(lambda word: word not in words, lst))
print("Modified list:",lst)