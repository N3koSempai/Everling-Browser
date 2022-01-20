#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository import WebKit2


def open_page(url):
    entry.set_text(url)
    webview.laod_uri(url)

def open_history(button):
    open_page('file://' + HISTORY_FILE)

def on_load_changed(webview, event):
    url = webview.get_uri()
    history_file = open(HISTORY_FILE, "a+")
    history_file.writelines("* " + url + "<br>")
    history_file.close()
    webview.load_uri(url)

#logical signals
#entry field url
def on_entry(entry):
    url = entry.get_text()
    webview.load_uri(url)
    if (url == "about:history"):
        open_history(webview)
        return
    open_page(url)

win = Gtk.Window()
webview = WebKit2.WebView()


win.connect("delete-event", Gtk.main_quit)

win.add(webview)
#entry bar in the headerbar
entry = Gtk.Entry.new()
entry.connect('activate',on_entry)

history_button = Gtk.Button()
history_button_image = Gtk.Image.new_from_icon_name("open-menu-symbolic",Gtk.IconSize.SMALL_TOOLBAR)
history_button.add(history_button_image)
history_button.connect("clicked", open_history)


#headerbar
headerbar = Gtk.HeaderBar()
headerbar.set_show_close_button(True)
headerbar.set_custom_title(entry)
headerbar.set_decoration_layout('menu:minimize,maximize,close')
win.set_titlebar(headerbar)

#arrow for back
def on_go_back(button):
    webview.go_back()

go_back_button = Gtk.Button()
go_back_arrow = Gtk.Image.new_from_icon_name("go-previous", Gtk.IconSize.SMALL_TOOLBAR)
go_back_button.add(go_back_arrow)
go_back_button.connect('clicked', on_go_back)
headerbar.pack_start(go_back_button)
headerbar.pack_start(history_button)
#arrow for redo
def on_go_forward(button):
    webview.go_forward()

go_forward_button = Gtk.Button()
go_forward_arrow = Gtk.Image.new_from_icon_name("go-next", Gtk.IconSize.SMALL_TOOLBAR)
go_forward_button.add(go_forward_arrow)
go_forward_button.connect('clicked', on_go_forward)
headerbar.pack_start(go_forward_button)

win.set_default_size(900,500)
win.set_title("Photon Browser")

win.show_all()

Gtk.main()
