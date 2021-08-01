from data.node_trie import Node_Trie


class Word_Trie:
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = Node_Trie("")

    def insert(self, suffix: str, full_sentence_id: int, offset: int):
        """Insert a word into the trie"""
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in suffix:
            if char in node.children:
                node = node.children[char]
                node.sentences.update({full_sentence_id: offset})

            else:
                # If a character is not found,
                # create a new node in the trie

                new_node = Node_Trie(char)
                node.children[char] = new_node
                node = new_node
                node.sentences.update({full_sentence_id: offset})

        # Mark the end of a word
        node.is_end = True

    def search(self, sentence: str):
        node = self.root
        for char in sentence:
            if char in node.children:
                node = node.children[char]
            else:
                return {}
        return node.sentences
