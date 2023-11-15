import sys

def IndexOfStr():
  str = input()
  n = int(input())
  print(str[n-1])

def LengthOfStr():
  str = input()
  print(len(str))

def SubStr():
  n = int(input())
  for i in range(n):
    str = input()
    print(f"{str[0]}{str[-1]}")

def ASCII():
  str = input()
  print(ord(str))

def Alphabet(str):
  alphabetList = [-1 for x in range(26)]
  for i in range(len(str)):
    if alphabetList[ord(str[i])-97] == -1:
        alphabetList[ord(str[i])-97] = i
      
  for i in range(len(alphabetList)):
    print(alphabetList[i], end = " ")

def AlphaNumeric():
  n = int(input())
  
  for i in range(n):
    num, al = input().split()
    alphabetList = ""
    for j in range(len(al)):
      alphabetList += al[j]*int(num)
    print(alphabetList)  

def WordCount():
  str = input()
  print(len(str.split()))

def Printer():
  while(True):
    try:
      str = input()
      print(str)
    except EOFError:
      break

def PrintSprout():
  str="""         ,r'"7
r`-_   ,'  ,/
 \. ". L_r'
   `~\/
      |
      |"""
  print(str)

def Pelindrome():
  str = input()
  for i in range(len(str)):
    if str[i] != str[len(str)-i-1]:
      print(0)
      return
  print(1)

def AlphaMax():
  str = input().upper()
  count ={}
  for i in str:
    try:
      count[i] += 1
    except:
      count[i] = 1
  values = [k for k,v in count.items() if max(count.values()) == v]
  if len(values)>1:
    print("?")
  else :
    print(values[0])
