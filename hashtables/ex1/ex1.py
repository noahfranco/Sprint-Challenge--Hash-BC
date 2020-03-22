#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


# *** Understand ***
# We will return two index within a tuple one with the legth of the list and the other with the limit of the list
# The larger index should be placed in the index of zero and the smaller index should be placed in the index of one

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for index in range(length): # if our index is in the range of the length of the table then execute the code below
        hash_table_insert(ht, weights[index], index)

    for index in range(length): # if our index is in the range of the length of the table then execute the code below
        weight_item_difference = limit - weights[index] # assigning a variable to equal limit - the weights item

        difference = hash_table_retrieve(ht, weight_item_difference) # assigning a variable to retrive the weights item difference

        if difference is not None: # if the retrieval is of the index is not None then we execute code below
            if difference >= index: # if the retreval is greater then the original next then we execute code below
                return (difference, index) # returning the retrieval and the index
            else:
                return (index, difference) # else we return the index then the retrieval
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
