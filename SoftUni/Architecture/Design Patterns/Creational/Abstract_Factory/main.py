"""
Abstract factory is a creational design pattern, whose job is to provide methods of instantiation
of a family of connected classes, thus uncoupling the classes and their implementation from the
place where they are used.

For example:

UI Factory:
- create Form
- create Button

MacUI Factory:
- create MacForm
- create MacButton

WindowsUI Factory:
- create WindowsForm
- create WindowsButton

Now we have an 2 abstract factories that allow us to create a set of objects from the same family,
without specifying their concrete classes beforehand, instead, we have to specify the factory.

This comes in handy when we develop applications for multiple OSs. At the start, we can check which OS we have
and then simply instantiate the appropriate factory, which will in turn create all objects. As such, we
will be sure that we won't mistakenly create a WindowsButton in a MacOS environment, which will obviously
break our code.

Single Responsibility - Object creation code is extracted in a single, specific place.
Open Closed Principle - As all Factories, it allows for easy extension.

Alternatively, we can combine Bridge and Abstract factory. Here we can have MacOSRedButton and MacOSBlueButton.
Instead, we can use the Bridge pattern and Dependency Injection to lower the amount of classes we have to
maintain and still neatly pack them in factories.
"""
from Abstract_Factory.colours import Blue, Red
from Abstract_Factory.factories import WindowsFactory, MacOSFactory

#current_OS = "Windows"
current_OS = "MacOS"

if current_OS == "Windows":
    factory = WindowsFactory()
    colour = Red()

elif current_OS == "MacOS":
    factory = MacOSFactory()
    colour = Blue()

else:
    print("Not implemented.")
    exit()

button = factory.build_button(colour=colour)
form = factory.build_form()

print(button.click())
print(form.fill_data())
