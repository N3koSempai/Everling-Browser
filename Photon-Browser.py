#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository.WebKit2 import WebView, Settings
import re


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def searching(self, search):
        url = search.get_text()

        if re.search(r"^http://*", url):
            webview.load_uri(url)
            print('ok')
        else:
            print(['with engine'])
            webview.load_uri((Engine % (url)))
        fhand = open('History', 'a')
        fhand.write(url + '\n')
#call builder for glade
builder = Gtk.Builder()
builder.add_from_file('graphic.glade')
#call objects in the glade template
webview = builder.get_object('Webview')
window = builder.get_object('MainWindow')
search = builder.get_object('Searchbox')

#default size of all window
window.set_default_size(900,500)
window.set_title('Photon Browser')
#instance the logic in the class Handler
handler = Handler()

#signals
search.connect('activate', handler.searching)
window.connect('destroy', handler.onDestroy)
Engine = 'https://www.ecosia.org/search?q=%s'


if __name__ == "__main__":
    window.show_all()
    Gtk.main()
