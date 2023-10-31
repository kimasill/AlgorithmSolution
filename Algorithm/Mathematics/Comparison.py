def CompareAB(a, b):
  if a > b :
    return ">"
  elif a < b :
    return "<"
  elif a == b:
    return "=="

def Grading(score):
  if 100 >= score >= 90:
    return "A"
  elif 90 > score >= 80:
    return "B"
  elif 80 > score >= 70:
    return "C"
  elif 70 > score >= 60:
    return "D"
  else :
    return "F"

def LeapYear(year):
  if year % 4 == 0 and year % 100 != 0:
    return 1
  elif year % 400 == 0:
    return 1
  else:
    return 0
  
def Quadrant(x, y):
  if x>0 and y>0:
    return 1
  elif x<0 and y>0:
    return 2
  elif x<0 and y<0:
    return 3
  elif x>0 and y<0:
    return 4

def Alarm(hour, minute):
  restTime = minute - 45
  if restTime < 0 :
    hour -= 1
    minute = 60 + restTime
    if hour < 0:
      hour = 23
  else :
    minute = restTime
  return hour, minute

def Oven(hour, minute, time):
  pTime = time//60
  restTime = time - pTime*60

  if minute + restTime > 59:
    hour += 1
    minute = minute + restTime - 60
  else :
    minute = minute + restTime

  hour = hour + pTime
  if hour > 23:
    hour = hour - 24

  return hour, minute
  
def ThreeDice(eyes):
  rewards = 0
  if eyes[0]==eyes[1]==eyes[2] :
    rewards = 10000+eyes[0]*1000
    return rewards

  for i in range(3):
    if eyes[i] == eyes[(i+1)%3] or eyes[i] == eyes[(i+2)%3] :
      rewards = 1000+eyes[i]*100
      return rewards

  rewards = max(eyes) * 100
  return rewards

def MinMax(n, arr):
  arr.sort()
  print(arr[-n], arr[n-1])

n = int(input())
arr = list(map(int, input().split()))
MinMax(n, arr)


