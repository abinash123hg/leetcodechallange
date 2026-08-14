class Solution:

  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    # Build a Trie
    trie = {}
    for word in words:
      node = trie
      for char in word:
        node = node.setdefault(char, {})
      node['$'] = word

    res = []
    rows, cols = len(board), len(board[0])

    def dfs(r, c, node):
      char = board[r][c]
      next_node = node[char]
      
      # If we found a complete word
      if '$' in next_node:
        res.append(next_node['$'])
        del next_node['$']  # Avoid duplicate entries

      board[r][c] = '#'  # Mark as visited
      for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in next_node:
          dfs(nr, nc, next_node)
      board[r][c] = char  # Restore cell

      # Optimization: prune Trie nodes that have no more matches
      if not next_node:
        node.pop(char)

    for r in range(rows):
      for c in range(cols):
        if board[r][c] in trie:
          dfs(r, c, trie)

    return res