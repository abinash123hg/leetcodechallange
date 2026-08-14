class Solution:

  def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    import heapq

    events = []
    for left, right, height in buildings:
      events.append((left, -height, right))
      events.append((right, height, 0))

    events.sort()

    res = [[0, 0]]
    # Store active heights, initialized with ground level height 0
    hp = [0]
    # Lazy deletion dictionary to keep track of removed building heights
    valid = {0: 1}

    for x, h, r in events:
      if h < 0:
        # Building starts: add height
        height = -h
        valid[height] = valid.get(height, 0) + 1
        heapq.heappush(hp, -height)
      else:
        # Building ends: remove height
        valid[h] -= 1

      # Clean up heights from the top of the heap that are no longer active
      while hp and valid[-hp[0]] == 0:
        heapq.heappop(hp)

      max_height = -hp[0]
      if res[-1][1] != max_height:
        res.append([x, max_height])

    return res[1:]