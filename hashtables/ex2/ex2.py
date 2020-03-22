#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


# *** Understand ***
# source and destination are key pair value
# Need to write a function that will reconstruct the trip from the mass of flight tickets
# use to constructor to do this
# should return a list of string with the entire route of the trip
# We don't have to sort the list because we can assume that we will be handed the valid ticket order

def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length -1) # so index will start at one and not zero

    for t in tickets: # for our every index in tickets 
        hash_table_insert(hashtable, t.source, t.destination) # we will get the hash length, the source of the index, and the destination of the index and insert it into our hash

    route[0] = hash_table_retrieve(hashtable, "NONE") # initially hashing at the first index with "None" being our initial key
    for i in range(1, length - 1):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route
