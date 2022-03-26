#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk 
from gi.repository.WebKit2 import WebView, Settings
from gi.repository import WebKit2
import re, os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

class Handler:
    def __init__(self):
        self.about = ('file://' +  os.path.abspath(__file__) + '/History')


    def onDestroy(self, *args):
        Gtk.main_quit()

    def searching(self, search):
        url = mainwindow.search.get_text()
        #different behavior depending if you have http: or not at the beginning
        
        if re.search(r"^http?://", url):
            temppage = mainwindow.tabsbar.get_current_page()
            mainwindow.webview.load_uri(url)
            title = mainwindow.webview.get_title()
            print(title)
            list = mainwindow.tabsbar.get_children()
            child = list[temppage]
            print(type(child))
            mainwindow.tabsbar.set_tab_label(child, title)

        elif re.search(r"^about:", url):
            if url == 'about:history':
                mainwindow.webview.load_uri(self.about)
        else:
            print('with engine')
            mainwindow.webview.load_uri((Engine % (url)))
        #file for save the history
        fhand = open('History.html', 'a')
        fhand.write('<p' + url + '\n')
        fhand.close()


    def add_page(self, _):
        label1 = Gtk.Label.new("new page")
        webview2 = mainwindow.webview.new()
        mainwindow.tabsbar.prepend_page(webview2, label1)
        print(mainwindow.tabsbar.get_children())
        webview2.load_uri('about:error')
        # mainwindow.tabsbar.set_tab_detachable(mainwindow.tabsbar.props.page, True)
        mainwindow.window.show_all()


class Headerbar:

    def back(self, back):
        enable = mainwindow.webview.can_go_back()
        if enable == True:
            mainwindow.webview.go_back()

    def forward(self, next):
        enable = mainwindow.webview.can_go_forward()
        if enable == True:
            mainwindow.webview.go_forward()

    def reload(self, url):
        mainwindow.webview.reload()

    


class MainWindow():

    def __init__(self):
        self.builder = Gtk.Builder()
        #load GUI
        self.builder.add_from_file('graphic.glade')
        self.webview = self.builder.get_object('Webview')
        self.window = self.builder.get_object('MainWindow')
        self.window.set_default_size(900,500)
        self.window.set_title('Everling Browser')
        self.search = self.builder.get_object('Searchbox')
        self.tabsbar = self.builder.get_object('tabsbar')
        
        self.back = self.builder.get_object('back')
        self.next = self.builder.get_object('next')
        self.reload = self.builder.get_object('reload')
        self.mainmenu = self.builder.get_object('MainMenu')
        self.mainfile = self.builder.get_object('MainFile')
        self.new_page = self.builder.get_object('new_page')


#instance the logic in the class Handler
mainwindow = MainWindow()
headerbar = Headerbar()
handler = Handler()

#signals

#headerbard signals
mainwindow.search.connect('activate', handler.searching)
mainwindow.back.connect('clicked', headerbar.back)
mainwindow.next.connect('clicked', headerbar.forward)
mainwindow.reload.connect('clicked', headerbar.reload)
mainwindow.new_page.connect('clicked', handler.add_page)


mainwindow.window.connect('destroy', handler.onDestroy)
Engine = 'https://www.ecosia.org/search?q=%s'


if __name__ == "__main__":
    mainwindow.window.show_all()
    Gtk.main()
