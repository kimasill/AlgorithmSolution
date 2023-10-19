class LRUD:
  """
  <Summary>
  상하좌우 알고리즘

  입력값에 대한 최종 좌표 반환
  </Summary>
  <Param>
    N : 공간의 크기 (N * N)
    문자열(L, R, U, D) : 이동할 방향
  </Param>
  """
  Way = []

  def StartAlgorithm(self):
    print("상하좌우 알고리즘")
    self.InputParams(self)
    self.SetWay(self)
    print(self.Calculate(self))

  def InputParams(self):
    print("공간 크기 N 입력 :")
    self.N = int(input())
    print("계획서(L R U D) 입력 :")
    self.W = map(str, input().split())

  def SetWay(self):
    wayX = []
    wayY = []
    for way in self.W:
      if (way == "L"):
        wayX.append(0)
        wayY.append(-1)
      if (way == "R"):
        wayX.append(0)
        wayY.append(1)
      if (way == "U"):
        wayX.append(-1)
        wayY.append(0)
      if (way == "D"):
        wayX.append(1)
        wayY.append(0)
    self.Way = list(zip(wayX, wayY))

  def Calculate(self):
    x, y = 1, 1
    for wayX, wayY in self.Way:
      tempX, tempY = x, y
      tempX += wayX
      tempY += wayY
      if (tempX == 0 or tempY == 0 or tempX > self.N or tempY > self.N):
        print("ignore out of range")
        continue
      x, y = tempX, tempY
    return x, y
