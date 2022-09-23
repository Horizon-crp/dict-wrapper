def deep(data: dict, *, still: bool = True) -> dict:
  e: dict = {}
  if still:
    for k, v in data.items():
      if type(v) is dict:
        for a, i in deep(v).items(): e[a] = i
      e[k] = v
  else:
    for k, v in data.items():
      if type(v) is dict:
        for a, i in deep(v).items(): e[a] = i
      else:
        e[k] = v
  return e

def deeps(*dicts, still: bool = True) -> dict:
  data: dict = {}
  for d in dicts:
    data.update(deep(d, still = still))
  return data
