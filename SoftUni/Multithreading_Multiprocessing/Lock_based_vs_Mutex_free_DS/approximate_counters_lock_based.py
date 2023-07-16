"""
Perfect scalability is the ability of a program to keep its performance constant over a wide range of thread/process
counts. In short, a program should complete in the same amount of time, regardless of it using 1 or 100 threads or
processes. Perfect scalability is almost impossible to achieve, if our design choices do not limit us, our hardware
will. Locks can destroy a concurrent program and turn it into a sequential one, thus destroying the perfect scalability.
For example, a lock based counter. Without the lock, it will suffer from race conditions and never achieve the correct
result, but with one, perfect scalability cannot be achieved as the program will become sequential.
Approximate counters is a solution to the scalability problem of a Lock based counter.
How it works:
If we have 1 counter that all threads must access, the program will scale very bad. As such, a possible solution
is to give each thread its own counter. That will increase the memory that is to be used, but also solve the
scalability issue. We can also make it so that multiple threads report to one local counter to save memory or
also make local counters report to level 1 counters that will then report to level 2 (global counters) themselves.
At the end, we have to choose the Threshold S, or the point at which a local counter will update the next level
counter. The smaller the S, the less scalable our program is, but the bigger the S, the less frequent the updates
to the global counter.
"""
