import sys, os

INTERP = "/home/themico1/mico_foundation/bin/python"

if sys.executable != INTERP : os.execl(INTERP, INTERP, *sys.argv)

#from mico_site.flask_app import app as application
from MICO.wsgi import application