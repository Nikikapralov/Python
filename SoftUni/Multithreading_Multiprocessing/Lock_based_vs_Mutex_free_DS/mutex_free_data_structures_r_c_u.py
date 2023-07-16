"""
In python, due to the presence of the GIL, a complete lock free data structure is impossible. A mutex free data structure
though is completely possible to implement.
Mutex free datastructures use no locks as a synchronisation mechanism and therefor are completely immune of the problems
of starvation, deadlocks and livelocks. A popular mutex free data structure is the Read Copy Update data structure.
It is used when we have a lot of readers and a relatively small amount of updaters, for example when using a copy
of a website to protect against DDOS attacks. Should one happen, we just switch to another copy and relocate the new
readers to it.

How to implement it:
A read update copy data structures copies the data from the main source at each pull, but does NOT copy the data
when making an update. As such, when updating, there is no race condition and when reading, should a thread attempt
to access data that has been deleted from another thread, it will have no problem doing it, since it has a copy from
a point before that.

A mutex free datastructure can also be used to solve the approximate counters problem.
"""