def fibonacci(index):
  if index <= 0:
    return 0
  elif index == 1:
    return 1
  a,b,temp = 0,1,0
  for x in range(2, index+1):
    temp = a+b
    a = b
    b = temp
  return b

if __name__ == "__main__":
  index = int(input("Enter an index for the Fibonacci sequence: "))
  print(f"Fibonacci({index}) = {fibonacci(index)}")
