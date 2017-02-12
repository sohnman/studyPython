#!/usr/bin/env python
# __author__ = 'evan'
#
# Refer to https://georgemuraruc.wordpress.com/2015/07/16/d-bus-tutorial-for-python/
#

__author__ = 'evan'

from gi.repository import GLib
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop


class Session_DBus(dbus.service.Object):

    def __init__(self):
        bus_name = dbus.service.BusName('org.me.test_session', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, '/org/me/test_session')

    # Interface and Method
    @dbus.service.method('org.me.test1')
    def session_bus_message1(self):
        return "Session Bus 1"

    # Different Interface and different Method
    # The method must not have not the same name as the first
    @dbus.service.method('org.me.test2')
    def session_bus_message2(self):
        return "Session Bus 2"

    # Method with arguments
    @dbus.service.method('org.me.test2')
    def session_bus_strings(self, string1, string2):
        return string1 + " " + string2

DBusGMainLoop(set_as_default=True)
dbus_service = Session_DBus()

try:
    GLib.MainLoop().run()
except KeyboardInterrupt:
    print("\nThe MainLoop will close...")
    GLib.MainLoop().quit()