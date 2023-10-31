import sys

def NN(n):
  for i in range (9):
    print(f'{n} * {i+1} = {n*(i+1)}')

def Addition(case):
  for i in range(case):
    a, b = map(int, input().split())
    print(a+b)

def AdditionV4():
  while True:
    try:
      a, b = map(int, input().split())
      print(a+b)
    except EOFError:
      break

def AdditionV5():
  while True:    
    a, b = map(int, input().split())
    if a == 0 and b == 0:
      break
    print(a+b)
      

def AdditionV7(case):
  for i in range(case):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a+b}")

def AdditionV8(case):
  for i in range(case):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")

def SequenceAddition(n):
  if n%2 == 0:
    return n * n//2 + n//2    
  else:
    return n * (n+1)//2

def Receipt(totalMoney, n):
  total = 0
  for i in range(n):
    money, item = map(int, input().split())
    total += money * item
  if total == totalMoney : 
    print("Yes")
  else :
    print("No")

def Byte(n):
  print("long "*(n//4) + "int")

def FastAddition(n):
  input = sys.stdin.readline
  for i in range(n):    
    a,b = map(int, input().split())
    print(a+b)

def Star(n):
  for i in range(n):
    print("*"*(i+1))

def StarV2(n):
  for i in range(n):
    print(" "*(n-i-1)+ "*"*(i+1))

def Counter():
  n = int(input())
  ess = list(map(int, input().split()))
  v = int(input())
  count = 0
  for i in range(n):
    if ess[i] == v:
      count+=1      
  print(count)

def LowNum():
  n, x = map(int, input().split())
  seq = list(map(int, input().split()))
  sol = []
  for i in range(n):
    if seq[i]<x :
      sol.append(seq[i])

  for i in sol:
    print(i, end = " ")

def MaxNumIndex():
  temp = 0
  index = 0
  for i in range(9):
    n = int(input())
    if n > temp :
      temp = n
      index = i+1
  
  print(f"{temp}\n{index}")

MaxNumIndex()