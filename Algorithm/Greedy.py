class ChangeMoney:
  """
  <Summary>
  거스름돈 알고리즘
  
  입력값의 거스름돈에 대한 최소 동전 수 반환
  
  동전 종류: 500, 100, 50, 10
  
  </Summary>
  <Param>
    num (int): 지불하는 값 
  </Param>
  """

  def StartAlgorithm(self):
    print("거스름돈 알고리즘 \n 금액 입력 :")
    self.num = int(input())
    print(self.ReturnChangeCount(self))

  def ReturnChangeCount(self):
    coins = [500, 100, 50, 10]
    count = 0
    for coin in coins:
      count += self.num // coin
      self.num %= coin
    return count


class RuleOfBigNumber:
  """
  <Summary>
  가장 큰 수 알고리즘
  
  파라미터에 따라 인덱스에서 가장 큰 수 더하여 반환
  </Summary>
  
  <Param>
    arrayLengh : 배열 길이
  
  countSum : 더할 횟수
  
  continuity : 같은 숫자를 연속으로 더할 수 있는 횟수
  </Param>
  """

  def StartAlgorithm(self):
    print("가장 큰 수")
    self.InputParams(self)
    print(self.Calculate(self))

  def InputParams(self):
    print("배열 크기, 더할 개수, 연속으로 더할 수 있는 최대 개수 :")
    self.__N, self.__M, self.__K = map(int, input().split())
    print("배열 :")
    self.__data = list(map(int, input().split()))

  def Calculate(self):
    count = 0
    result = 0
    self.__data.sort()
    while (count < self.__M):
      for i in range(0, self.__K):
        result += self.__data[self.__N - 1]
        count += 1
        if (count == self.__M): return result
      if (count < self.__M):
        result += self.__data[self.__N - 2]
        count += 1
    return result


class RuleOfBigNumberSolution:

  def StartAlgorithm(self):
    print("가장 큰 수 - 시간 복잡도 솔루션")
    self.InputParams(self)
    print(self.Calculate(self))

  def InputParams(self):
    print("배열 크기, 더할 개수, 연속으로 더할 수 있는 최대 개수 :")
    self.__N, self.__M, self.__K = map(int, input().split())
    print("배열 :")
    self.__data = list(map(int, input().split()))

  def Calculate(self):
    self.__data.sort()
    first = self.__data[self.__N - 1]
    second = self.__data[self.__N - 2]

    count = int(self.__M / (self.__K + 1)) * self.__K
    count += self.__M % (self.__K + 1)

    result = 0
    result += count * first
    result += (self.__M - count) * second
    return result


class NumberCardGame:

  def StartAlgorithm(self):
    print("숫자 카드 게임")
    self.__min = 0
    self.InputParams(self)
    print(self.__min)

  def InputParams(self):
    print("배열 크기 입력 (행, 열)")
    self.__N, self.__M = map(int, input().split())

    print("배열 입력 :")
    for i in range(self.__N):
      array = list(map(int, input().split()))
      if (min(array) > self.__min):
        self.__min = min(array)


class UntillOne:

  def StartAlgorithm(self):
    print("1이 될 때까지 \n N이 K로 나누어 떨어지면 나누고, 아니라면 1을 빼는것을 1이 될 때까지 반복. ")
    if (self.InputParams(self) == False):
      return False
    print(self.Calculate(self))

  def InputParams(self):
    print("N(어떠한 수), K(나눌 수)")
    self.__N, self.__K = map(int, input().split())
    if (self.__N < 2 | self.__K < 2):
      print("입력 값은 2보다 커야합니다.")
      return False

  def Calculate(self):
    result = 0
    count = 0
    N = self.__N
    K = self.__K
    while (result != 1):
      if (N % K == 0):
        result = N / K
        N = result
      else:
        result = N - 1
        N = result
      count += 1
    return count
