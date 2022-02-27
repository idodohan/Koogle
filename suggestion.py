from typing import List


class Suggestion:
    """
    represents a suggestion node/object
    """
    def __init__(self, word: str, is_a_word=False):
        self.is_a_word = is_a_word  # in order to differentiate between 'path words' to actual words
        self.word = word
        self.search_count = 1
        self.most_relevant_searches = []  # stores the 10 most relevant searches
        self.children = {}  # stores all child nodes of the current node

    def add_child(self, word: str) -> None:
        """
        gets a word and adds it as a child (from type suggestion) to the current node
        :param word:
        :return:
        """

        # if we have reached the correct depth of the tree add the word
        if len(word) == len(self.word) + 1:
            self.children[word] = Suggestion(word, is_a_word=True)
        else:
            next_word = word[0:(len(self.word) + 1)]
            self.children[next_word] = Suggestion(next_word, is_a_word=False)
            self.children[next_word].add_child(word)

    def update_most_relevant_searches(self) -> None:
        """
        updates most relevant searches for the current node (and its children)
        :return:
        """
        self.most_relevant_searches = []

        # iterates over all child nodes to merge all relevant searches into one list
        for child in self.children:
            self.children[child].update_most_relevant_searches()
            self.most_relevant_searches = merge_sort(self.most_relevant_searches, self.children[child].most_relevant_searches)

        # check if 'self' needs to enter the most relevant searches list
        if self.is_a_word:
            self.most_relevant_searches = merge_sort(self.most_relevant_searches, [self])


def merge_sort(list_a: List[Suggestion], list_b: List[Suggestion]) -> List[Suggestion]:
    """
    gets 2 sorted lists and merges them. returns the first 10 elements of the merged list
    :param list_a: sorted list
    :param list_b: sorted list
    :return: first 10 elements of merged list
    """

    i = 0
    j = 0
    list_c = []

    while i < len(list_a) and j < len(list_b):
        if list_a[i].search_count > list_b[j].search_count:
            list_c.append(list_a[i])
            i += 1
        else:
            list_c.append(list_b[j])
            j += 1

    list_c += list_a[i:] + list_b[j:]

    return list_c[:10]
