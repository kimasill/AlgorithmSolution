import DataStructure as Data
from Algorithm.AlgorithmManager import AlgorithmManager as Algorithm


class Manager:

  def Initialize(self):
    self.__Manager = self
    self.__Dics = Data.Dictionarys
    self.__AlgorithmManager = Algorithm
    self.__AlgorithmManager.Initialize(Algorithm)

  def Manager(self):
    return self.__Manager

  def Dics(self):
    return self.__Dics

  def Algorithm(self):
    return self.__AlgorithmManager
