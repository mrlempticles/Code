
class Trie(object):

    def __init__(self):
        self.root = {}
        self.END = "*"

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root

        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]

        node[self.END] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root

        for char in word:
            if char not in node:
                return False
            node = node[char]

        return self.END in node

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root

        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True
