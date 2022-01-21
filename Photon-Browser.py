#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository import WebKit2

builder = Gtk.Builder()
builder.add_from_file('graphic.glade')

window = builder.get_object('MainWindow')
window.show_all()

Gtk.main()
