"""
Command is a behavioral design pattern which aims to decouple business logic and GUI representation.
For example, imagine we have an application with a GUI. We have multiple buttons and whenever we
click a button, that button does something. One button loads the data, another processes it and
another saves the data. Well, this doesn't quite sound right as we have business logic in the GUI
implementation! Why is that bad, though? Imagine we are asked to change how one button looks like.
Suddenly we are exposed to the business logic code. In a team of multiple people, that will immediately
cause merge issues and is very likely to produce spaghetti code. Not only that, but what if we want to
use the save functionality as a part of a shortcut? We have the code in the save button, so we just copy
paste it, right? And when something changes, we now have to update 2 copies of the same code. Not a very good
design at all.

The Command pattern provides a solution to all of those problems. It is a sort of an API.
The GUI buttons have a reference to a command object. They pass their request to the command object
and it then passes it (as a standalone) to the business logic object which does the job.
That way we now have 3 layers. GUI layer, Command layer, Business logic layer.

We can have multiple command types. The command type determines what actions are allowed to be
asked from the business layer.

A real world example would be the current state of the Web Internet with the HTTP protocol.
The Front End (GUI) lives separately from the Back End. They are connected through the HTTP Protocol.
The Command is the Server on which the backend code lives. The Front End sends a request to the Server,
which then delegates it to the Back End code that does the work.

An easier example would be a restaurant. A client says his order to a server. The server writes the order down
and gives it to the chef. When he has time, the chef completes the order.

The Command pattern can be used easily to revert operations.
There are 2 possibilities for that.
We keep the state of the previous operation and when asked to revert, we simply use that state.
(RAM or Storage Memory intensive)
OR
We invert calculate the result from the current operation to the previous one.
(CPU intensive or may not even be possible.
"""

from Behavioral.Command.command import Button, CoolButton, SaveCommand, DeleteCommand, Receiver

receiver = Receiver()
save_command = SaveCommand(receiver=receiver)
delete_command = DeleteCommand(receiver=receiver)
normal_button = Button(command=save_command)
cool_button = CoolButton(command=delete_command)
"""
It may seem as we haven't changed much as now we still have a SaveButton and DeleteButton but that is totally
dependent on what command they receive. We may decide to implement a list of commands that may be called
as a chain of responsibility of have one command that is responsible for multiple options (this one is not
a good solution as it will get bloated).
"""
normal_button.click({"method": "Save"})
cool_button.click({"method": "Save"})
normal_button.click({"method": "Delete"})
cool_button.click({"method": "Delete"})