class Node_Trie:
    """A node in the trie structure"""

    def __init__(self, char: chr) -> None:
        # the character stored in this node
        self.char = char
        # whether this can be the end of a word
        self.is_end = False

        self.sentences = {}

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}
