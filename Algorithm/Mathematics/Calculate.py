def addition(a,b):
  return a + b

def additionV2():
  n = int(input())
  num = input()
  sum = 0
  for i in range(n):
    sum+= int(num[i])
  print(sum)

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

def remain42():
  count = 0
  list = [0 for x in range(42)]
  for i in range(10):
    num = int(input())
    list[num%42] += 1
  for i in list:
    if i >= 1:
      count += 1
  print(count)
  
def surprise(string):
  return string+"??!"

def taiYear(year):
  return year-543

def dog():
  print("|\_/|")
  print("|q p|   /}")
  print('( 0 )"""\\')
  print('|"^"`    |')
  print("||_/=\\\\__|")

def average():
  average = 0
  n = int(input())
  score = list(map(int, input().split()))
  for i in range(n):
    temp = score[i]/max(score)*100
    average += temp
  print(average/n)
  
additionV2()
  
