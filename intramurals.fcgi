#!/usr/bin/python
import sys,os

#os.system('fcgikill; ~/intramurals.fcgi')

#add this dir to the path
sys.path.insert(0, '/home/users8/dlaskows/local_html/intramural-manager/intramurals/')

#set the django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method='threaded', daemonize='false')
