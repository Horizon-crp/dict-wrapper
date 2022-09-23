def getkeys(*dicts, deep: bool = False) -> list:
  '''
  get the keys from some dicts (no limit of dicts btw)
  
  '''
  e: list = []
  if deep is False:
    for i in dicts:
      e.append(i.keys())
    return e
  else:
    for d in dicts:
      for p, i in d.items():
        if type(i) is dict:
          for a in getkeys(i, deep=True):
            e.append(a)
        else:
          e.append(p)
    return e
