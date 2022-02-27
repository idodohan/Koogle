from suggestion import Suggestion
from typing import List


class Koogle:
    """
    search engine object
    """
    def __init__(self):
        self.suggestion_tree = Suggestion(word="")  # initializes suggestion tree with an empty word

    def search(self, word: str) -> None:
        """
        occurs when user hits 'enter'. if the word exists in the tree update its search count, else add to the tree
        :param word:
        :return:
        """

        tree_iterator = self.suggestion_tree
        n = 1  # used in order to take the first n elements of the word

        # goes over the necessary nodes for creating the word
        while word[0:n] in tree_iterator.children:
            tree_iterator = tree_iterator.children[word[0:n]]
            n += 1

        # if we have reached the word
        if word == tree_iterator.word:

            # if is a word update its search count
            if tree_iterator.is_a_word:
                tree_iterator.search_count += 1

            # else make it a 'real' word
            else:
                tree_iterator.is_a_word = True

        # if we haven't reached the desired word, meaning word doesn't exist- add it to the tree
        else:
            tree_iterator.add_child(word)

        # updates most relevant searches for the entire tree
        self.suggestion_tree.update_most_relevant_searches()

    def suggest(self, word: str) -> List[Suggestion]:
        """
        occurs when user is typing.
        :param word:
        :return: 10 most relevant searches
        """
        tree_iterator = self.suggestion_tree
        n = 1  # used in order to take the first n elements of the word

        # goes over the necessary nodes for creating the word
        while word[0:n] in tree_iterator.children:
            tree_iterator = tree_iterator.children[word[0:n]]
            n += 1

        return tree_iterator.most_relevant_searches
