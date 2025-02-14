class TrieNode:
  def __init__(self):
    self.children: Dict[str, TrieNode] = collections.defaultdict(TrieNode)
    self.isWord = False


class Trie:
  def __init__(self):
    self.root = TrieNode()

  def insert(self, word: str) -> None:
    node: TrieNode = self.root
    for c in word:
      if c not in node.children:
        node.children[c] = TrieNode()
      node = node.children[c]
    node.isWord = True

  def search(self, word: str, l: int, r: int) -> bool:
    node: TrieNode = self.root
    for i in range(l, r):
      if word[i] not in node.children:
        return False
      node = node.children[word[i]]
    return node.isWord


class Solution:
  def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
    ans = 0
    trie = Trie()

    for s in forbidden:
      trie.insert(s)

    # r is the rightmost index to make word[l..r] a valid substring.
    r = len(word) - 1
    for l in range(len(word) - 1, -1, -1):
      for end in range(l, min(l + 10, r + 1)):
        if trie.search(word, l, end + 1):
          r = end - 1
          break
      ans = max(ans, r - l + 1)

    return ans
