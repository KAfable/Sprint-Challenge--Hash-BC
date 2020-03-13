#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # seems like we could just use enumerate instead of length

    for index in range(length):
        hash_table_insert(ht, weights[index], index)
        # print(ht.storage)

    for weight in weights:
        # get the index of the first weight
        first_index = hash_table_retrieve(ht, weight)
        # print(f'\nfirst_index: {first_index}')

        difference = limit - weights[first_index]
        # if it exists, get the index of the next weight
        second_index = hash_table_retrieve(ht, difference)
        # print(f'\nsecond_index: {second_index}')

        if first_index is not None and second_index is not None:
            if weights[first_index] < weights[second_index]:
                # print(f'\nFound a sum: ({second_index}), ({first_index})\n')
                return (second_index, first_index)
            else:
                # print(f'\nFound a sum: ({first_index}), ({second_index})\n')
                return (first_index, second_index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
