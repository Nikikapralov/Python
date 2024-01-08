"""
The Iterator behavioral pattern is very useful when working with collections and we want to hide the underlying
way we traverse them or potentially use different kind of traversal patterns.

For example, we have a tree data structure. We can traverse the tree in multiple ways, level order traversal,
post order, pre order, depth first traversal. Sure, implementation of all of those traversal methods in our
collection is possible but that will bloat our collection and what about code reusability? Will we have to
implement those methods for each collection? What happens when we want to make a change? And when multiple
teams work on that class, who will deal with the merge conflicts? And the deployment and redeployment?

To solve all of those issues, we take out the traversal algorithms and we move them to a different class,
to an Iterator. Each Iterator implements one algorithm and the Collection object will receive the Iterator class
when the Collection.iterate(Iterator) is called. The Iterator will alone keep track of how far it has iterated as
that allows a collection to be iterated at the same time in different ways.

A real world example is a vacation in Rome. One could walk around on his own and explore, buy a map or hire a guide.
The collection is Rome.
The iterator are the different possibilities.
A client can decide on his own how he wishes to proceed.

We can use an Iterator when we have many different traversal possibilities,
implement Memento to make snapshots or Visitor to trigger events.
"""

from Behavioral.Iterator.iterator import WordsCollection, ForwardIterator, ReverseIterator

collection = WordsCollection(["First", "Second", "Third"])

iterator_forward = collection.iterate(ForwardIterator)
[print(item) for item in iterator_forward]
print("------------------------------------")
iterator_reverse = collection.iterate(ReverseIterator)
[print(item) for item in iterator_reverse]
print("------------------------------------")
[print(item) for item in collection] # Default uses a default iterator being Forward Iterator.
