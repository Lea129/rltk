import utils
import collections
import math

class TfIdf(object):
    _similarity = 0

    def __init__(self, bag1, bag2, corpus_list=None, dampen=True):
        """
        code modified from py_stringmatching
        """
        utils.check_for_none(bag1, bag2)
        utils.check_for_type(list, bag1, bag2)

        # if corpus is not provided treat input string as corpus
        if corpus_list is None:
            corpus_list = [bag1, bag2]
        corpus_size = len(corpus_list)

         # term frequency for input strings
        tf_x, tf_y = collections.Counter(bag1), collections.Counter(bag2)

        # number of documents an element appeared
        element_freq = {}

        # set of unique element
        total_unique_elements = set()
        for document in corpus_list:
            temp_set = set()
            for element in document:
                # adding element only if it is present in one of two input string
                if element in bag1 or element in bag2:
                    temp_set.add(element)
                    total_unique_elements.add(element)
            # update element document frequency for this document
            for element in temp_set:
                element_freq[element] = element_freq[element] + 1 if element in element_freq else 1
        idf_element, v_x, v_y, v_x_y, v_x_2, v_y_2 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

        # tfidf calculation
        for element in total_unique_elements:
            idf_element = corpus_size * 1.0 / element_freq[element]
            v_x = 0 if element not in tf_x else (math.log(idf_element) * math.log(tf_x[element] + 1)) if dampen else (
                idf_element * tf_x[element])
            v_y = 0 if element not in tf_y else (math.log(idf_element) * math.log(tf_y[element] + 1)) if dampen else (
                idf_element * tf_y[element])
            v_x_y += v_x * v_y
            v_x_2 += v_x * v_x
            v_y_2 += v_y * v_y

        self._similarity = 0.0 if v_x_y == 0 else v_x_y / (math.sqrt(v_x_2) * math.sqrt(v_y_2))

    def similarity(self):
        return self._similarity

    def distance(self):
        return None