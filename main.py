intInput = int(input ("Enter a number >0: "))
while (intInput <= 0):
  intInput = int(input("Invalid. Try another: "))
total = 1
for i in range(1, intInput+1):
  total *= i
  print (i)
print (intInput,"! = ", total, sep = "")