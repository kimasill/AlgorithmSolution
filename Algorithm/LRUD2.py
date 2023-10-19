print("상하좌우 알고리즘2")
x,y = 1,1
plan = input().split()
size = input()

xpos =[-1, 1, 0, 0]
ypos =[0, 0, -1, 1]
plans = ["L", "R", "U", "D"]
tx, ty = x, y
for c in plan:
  for i in range(len(plans)):
    if c == plans[i] :
      tx += xpos[i]
      ty += ypos[i]
      if tx < 1 or tx > int(size) or ty < 1 or ty > int(size):
        print("Out of Range")
        continue
      x+= xpos[i]
      y+= ypos[i]
print(y,x)
