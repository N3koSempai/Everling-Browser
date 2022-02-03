#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository.WebKit2 import WebView, Settings
from gi.repository import WebKit2
import re, os


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def searching(self, search):
        url = mainwindow.search.get_text()
        #different behavior depending on if you have http: or not at the beginning
        if re.search(r"^http://*", url):
            mainwindow.webview.load_uri(url)
            print('ok')
        elif re.search(r"^about:", url):
            if url == 'about:history':
                mainwindow.webview.load_uri('file:///var/')
        else:
            print('with engine')
            mainwindow.webview.load_uri((Engine % (url)))
            print('engine second part')
        fhand = open('History', 'a')
        fhand.write(url + '\n')
        fhand.close()

class MainWindow:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('graphic.glade')
        self.webview = self.builder.get_object('Webview')
        self.window = self.builder.get_object('MainWindow')
        self.window.set_default_size(900,500)
        self.window.set_title('Photon Browser')
        self.search = self.builder.get_object('Searchbox')
        self.tabsbar = self.builder.get_object('tabsbar')




#instance the logic in the class Handler
mainwindow = MainWindow()

handler = Handler()

#signals
mainwindow.search.connect('activate', handler.searching)
mainwindow.window.connect('destroy', handler.onDestroy)
Engine = 'https://www.ecosia.org/search?q=%s'


if __name__ == "__main__":
    mainwindow.window.show_all()
    Gtk.main()
