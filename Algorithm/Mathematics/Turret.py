t = input()
for i in range(int(t)):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  
  distance = ((abs(x2 - x1)) ** 2 + (abs(y2 - y1))** 2) ** 0.5
  radius = r1 + r2
  if distance == 0 :
    if r1 == r2 and radius>0 :
      print(-1)      
    elif r1 == 0 and r2 == 0:
      print(1)
    else     :
      print(0)
  elif (distance == radius or abs(r1 - r2) == distance):
    print(1)
  elif (abs(r1 - r2) < distance < radius):
    print(2)
  elif (abs(r1 - r2) > distance or radius< distance):
    print(0)