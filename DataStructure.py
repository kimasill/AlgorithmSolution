class Dictionarys:
  greedy = {}
  implementation = {}
  dicList = []

  def Greedy(self, key, value):
    self.greedy[key] = value

  def Implementation(self, key, value):
    self.implementation[key] = value

  def AppendDicsInList(self, dic):
    self.dicList.append(dic)

  def GetAlgorithmSet(self, index):
    return self.dicList[index]
