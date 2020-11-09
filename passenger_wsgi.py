import sys, os

INTERP = "/home/themico1/mico_foundation/bin/python"

if sys.executable != INTERP : os.execl(INTERP, INTERP, *sys.argv)

#Import mico django application to passenger
from MICO.wsgi import application