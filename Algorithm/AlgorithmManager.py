import Manager
from . import Greedy
from . import Implementation


class AlgorithmManager:

  def Initialize(self):
    global dics
    dics = Manager.Manager.Dics(Manager.Manager)
    self.InitializeDictionary()
    self.InitializeList()

  def InitializeDictionary():
    # Greedy
    dics.Greedy(dics, 1, Greedy.ChangeMoney)
    dics.Greedy(dics, 2, Greedy.RuleOfBigNumber)
    dics.Greedy(dics, 3, Greedy.RuleOfBigNumberSolution)
    dics.Greedy(dics, 4, Greedy.NumberCardGame)
    dics.Greedy(dics, 5, Greedy.UntillOne)

    #Implementation
    dics.Implementation(dics, 1, Implementation.LRUD)

  def InitializeList():
    dics.AppendDicsInList(dics, dics.greedy)
    dics.AppendDicsInList(dics, dics.implementation)

  def ShowSpecificDictionary(listIndex):
    dictionary = dics.GetAlgorithmSet(dics, listIndex)
    for i in range(len(dictionary)):
      print(str(i + 1) + " : " + dictionary[i + 1].__name__)

  def StartAlgorithm(listIndex, dicIndex):
    dictionary = dics.GetAlgorithmSet(dics, listIndex)
    dictionary[dicIndex].StartAlgorithm(dictionary[dicIndex])
