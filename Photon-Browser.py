#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository import WebKit2



#logical signals
#entry field url
def on_entry(entry):
    url = entry.get_text()
    webview.load_uri(url)

win = Gtk.Window()
webview = WebKit2.WebView()


win.connect("delete-event", Gtk.main_quit)

win.add(webview)
#entry bar in the headerbar
entry = Gtk.Entry.new()
entry.connect('activate',on_entry)



#headerbar
headerbar = Gtk.HeaderBar()
headerbar.set_show_close_button(True)
headerbar.set_custom_title(entry)
win.set_titlebar(headerbar)



win.set_default_size(900,500)
win.set_title("Photon Browser")

win.show_all()

Gtk.main()
