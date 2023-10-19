import Manager

manager = Manager.Manager
manager.Initialize(manager)
dics = manager.Dics

while (True):
  print("알고리즘 유형 선택" + "\n 1 : Greedy" + "\n 2 : Implementation" +
        "\n 0 : End")

  listCount = int(input()) - 1
  if (listCount == -1): exit()
  print("알고리즘 선택")
  manager.Algorithm(manager).ShowSpecificDictionary(listCount)
  dicsCount = int(input())

  manager.Algorithm(manager).StartAlgorithm(listCount, dicsCount)
