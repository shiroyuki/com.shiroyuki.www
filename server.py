# -*- coding: utf-8 -*-
from logging import ERROR, WARNING, DEBUG, INFO
from sys import exit, argv
from tori.application import Application
from tori.common      import LoggerFactory

LoggerFactory.instance().set_default_level(INFO if '--dev' in argv else ERROR)

application = Application('config/app.xml')
application.start()
