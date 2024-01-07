"""

"A simple interface to a complex system..."

The Facade is a structural design pattern that aims to hide complexity of a system from the user.
It can also be used to decouple a bunch of complex classes and provide a simple interface for interaction,
thus making sure that should something change, only the Facade class is to be rewritten.

For example:

A master - slave architecture task design.
We may have a system where a master is initialised, then some worker nodes. Each of those worker nodes,
then have their own operations with their own distinct order. They may cache the operation, send notifications
and then perform the work that was requested. We can expose the user to that system and all of it's underlying
details, how to start a master, then add it's worker nodes and make sure that each specific node does it's specific
operation in a distinct order. That would be a lot to learn, it may not even be needed. Our user just wants to run
the master and the workers and to get his jobs done. We can provide a Facade class that hides the complexity but
provides a simple interface to the user, of just a few function with which he can interact with.

A good example of Facades are the libraries implemented in C but having the ability to be invoked in Python.
For example Numpy. Numpy provides you with a small interface that hides a complex C implementation of various
mathematical algorithms.

Use Facade when a subsystem is complex and a detailed set up is required, which the user does not necessarily need
to master in order to user your system.

"""
from Structural.Facade.facade import SubsystemTasksFacade
from Structural.Facade.subsystem import PostProcessor, Emailer
facade = SubsystemTasksFacade(tasks=["1", "2"], api=Emailer(), post_processor=PostProcessor())
facade.complete_tasks()

