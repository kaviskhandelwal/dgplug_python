#!/usr/bin/env python

import getpass
from cmd2 import Cmd
import requests        
     
__version__ = '0.1'
     
class Application(Cmd):
        """
       The main Application class
     
       """
     
        def __init__(self):
            Cmd.__init__(self)
     
        def do_hello(self, line): """ prints hello <line> on command hello <line> """
            print "Hello:", line
 
        def do_sayit(self, line):  """ prints Pyhton Rocks! on command sayit <line> """
            print "Python rocks !"
 
        def do_greet(self, line):
            print "Hi! %s" %(getpass.getuser()) """ Greet current user on command greet <line>"""
                                        

        def do_stock(self,line):  """ print the current stock price on command stock <stock>"""
            r = requests.get('http://download.finance.yahoo.com/d/quotes.csv?s='+line+'&f=l1')
            p = float(r.text)
      if p == 0.00
                 print "Invalid Code"
            else:
                 print "%f" % (p)


    
if __name__ == '__main__':
        app = Application()
        app.cmdloop()
