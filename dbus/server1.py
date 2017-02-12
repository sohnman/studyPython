#!/usr/bin/env python
# __author__ = 'evan'
#
# Refer to https://coelhorjc.wordpress.com/2014/12/09/howto-write-dbus-service-for-linux-in-python/
#

# Test
#
# host$ qdbus com.example.SampleService /SomeObject HelloWorld "hello from cli"
# Hello
# from example-service.py
# with unique name
# :1.200
#
# host$ dbus-send --session --print-reply --dest="com.example.SampleService" /SomeObject com.example.SampleInterface.HelloWorld string:"hello from cli"
# method return time=1486899102.131731 sender=:1.200 -> destination=:1.203 serial=5 reply_serial=2
#    array [
#       string "Hello"
#       string "from example-service.py"
#       string "with unique name"
#       string ":1.200"
#    ]

import dbus
import dbus.service


class SomeObject(dbus.service.Object):
    def __init__(self):
        self.session_bus = dbus.SessionBus()
        name = dbus.service.BusName("com.example.SampleService", bus=self.session_bus)
        dbus.service.Object.__init__(self, name, '/SomeObject')

    @dbus.service.method("com.example.SampleInterface", in_signature='s', out_signature='as')
    def HelloWorld(self, hello_message):
        return ["Hello", "from example-service.py", "with unique name", self.session_bus.get_unique_name()]

    @dbus.service.method("com.example.SampleInterface", in_signature='', out_signature='')
    def Exit(self):
        mainloop.quit()


if __name__ == '__main__':
    # using glib
    import dbus.mainloop.glib
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    import gobject
    loop = gobject.MainLoop()
    object = SomeObject()
    loop.run()

