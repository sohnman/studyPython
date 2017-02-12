__author__ = 'evan'

import dbus

def vers1():
    bus = dbus.SessionBus()
    session = bus.get_object("org.me.test_session", "/org/me/test_session")

    method_message1 = session.get_dbus_method('session_bus_message1', 'org.me.test1')
    method_message2 = session.get_dbus_method('session_bus_message2', 'org.me.test2')
    method_message3 = session.get_dbus_method('session_bus_strings', 'org.me.test2')

    # Call the methods with their specific parameters
    print(method_message1())
    print(method_message2())
    print(method_message3("Hello", "world"))


def vers2():
    bus = dbus.SessionBus()
    session = bus.get_object("org.me.test_session", "/org/me/test_session")

    interface1 = dbus.Interface(session, "org.me.test1")
    interface2 = dbus.Interface(session, "org.me.test2")

    # Call the methods using the interface
    print(interface1.session_bus_message1())
    print(interface2.session_bus_message2())
    print(interface2.session_bus_strings("Hello", "world"))


vers1()
vers2()