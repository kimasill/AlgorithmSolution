def addition(a,b):
  return a + b

def subtraction(a,b):  
  return a - b

def printer():
  print("Hello World!")

def multiplication(a,b):  
  return a*b

def division(a, b, share = False):
  if share == True:
    return a//b
  return a/b  

def scanner():
  a, b = map(int, input().split())
  return a, b

def remain(a, b):
  return a%b

def surprise(string):
  return string+"??!"

def taiYear(year):
  return year-543


a = int(input())
b = input()
nums = []
sum = 0
for i in range(3):
  nums.append(int(b[i])*a)

for i in range(3):
  print(nums[2-i])
  sum += (nums[2-i]*10**i)
print(sum)

  
