"""
Chain of Responsibility is a behavioural design pattern. Let us imagine a system
where we have to do different authentication steps, one after another, but sometimes,
some of the steps can be omitted. Our code can look like this:
check_1 -> check_2 -> check_3 -> check_4 at one place and like this in another:
check_1 -> check_4 etc

This can quickly blow out of proportion and become unmanageable and hard to debug in big
systems. And how do you implement alternative logic? If result from check_1 go to check_2 or drop
do something else? The method this is used will quickly become bloated and hard to support and maintain.

A chain of responsibility is used in this case.
It is made up of multiple Handlers, connected with each other through one directional linked list.
The request arrives at one Handler, which does check_1, then the result is sent to check_2 and so on and
so fort until the end. This allows for the drop and continue clauses to be integrated inside the Handler classes
and not have to be outside the check_1 functions, in the other module. This provides better decoupling
and allows for specific changes in Handlers that do not require the redeployment of the whole system.

Alternatively, one can use a Chain of Responsibility as a series of escalatory actions.
For example, attempt to write the data in the Database. Well if it doesn't work, escalate,
attempt to write the data in the File system. If that also doesn't work, attempt to send
the data to a Cloud Storage. Each of those actions is encompassed in a Handler that upon
failure will send the request to the next in line Handler.

A different modification allows for the data to go through all Handlers but only be modified by some of them.

A Chain of Responsibility can also be imagined as a Tree Data Structure, where each branch off account
for a different outcome and a different chain. As this can quickly become quite complex and even evolve
into a Graph, it must be advised that a chain of responsibility should remain just that - a chain,
with exceptions, where required.

*A request can be sent to any handler in the chain, which picks up from there.

TO USE WHEN:
We have many handlers and don't know which one can handle the request we received.
When order and set of Handlers are unknown -
Providing a setter for the next Handler in the previous Handler will ensure that
we will build the Chain dynamically with the exact handlers that we need.
"""

from handlers import *

first = FirstHandler()
first.set_next(SecondHandler()).set_next(ThirdHandler())

handled_by_first = {"first": 1}
handled_by_second = {"second": 2}
handled_by_third = {"third": 3}

print(first.handle(handled_by_first))
print(first.handle(handled_by_second))
print(first.handle(handled_by_third))

print(SecondHandler().handle(handled_by_first))