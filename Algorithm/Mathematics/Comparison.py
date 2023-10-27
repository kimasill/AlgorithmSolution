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

x = int(input())
y = int(input())
print(Quadrant(x, y))
