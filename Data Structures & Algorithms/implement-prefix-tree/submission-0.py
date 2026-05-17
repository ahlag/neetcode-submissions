class TrieNode:
    def __init__(self):
        # Dictionary that maps a character to the next TrieNode.
        # Example: {"a": TrieNode(), "b": TrieNode()}
        self.children = {}

        # True if a full word ends at this node.
        # False if this node is only part of a word.
        self.endOfWord = False


class PrefixTree:
    def __init__(self):
        # Create the root node of the trie.
        # The root does not store a character itself.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start from the root of the trie.
        cur = self.root

        # Go through each character in the word.
        for c in word:
            # If there is no path for this character yet,
            # create a new node for it.
            if c not in cur.children:
                cur.children[c] = TrieNode()

            # Move to the next node for this character.
            cur = cur.children[c]

        # After processing all characters,
        # mark this node as the end of a complete word.
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        # Start from the root.
        cur = self.root

        # Check each character in the word one by one.
        for c in word:
            # If the character path does not exist,
            # the word is not in the trie.
            if c not in cur.children:
                return False

            # Move to the next node.
            cur = cur.children[c]

        # After finishing all characters,
        # return True only if this node marks the end of a full word.
        # This prevents prefixes from being treated as full words.
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:

        # Start from the root.
        cur = self.root

        # Check each character in the prefix.
        for c in prefix:
            # If the path does not exist,
            # then no word starts with this prefix.
            if c not in cur.children:
                return False

            # Move to the next node.
            cur = cur.children[c]

        # If we successfully walked through the whole prefix,
        # then at least one word starts with it.
        return True


        
        