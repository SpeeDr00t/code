#
#
# write by kyoung chip , jang
#
# python 3.6
#
#
from ctypes import cdll

class CHello(object):

    def __init__( self ):

        self.lib = cdll.LoadLibrary('./libhello.so')
        self.obj = self.lib.CHello_new()

    def printOut( self ):

        self.lib.CHello_print( self.obj )

    def push_back( self , s ) :
        
        self.lib.CHello_push_back( self.obj, s )

if __name__ == '__main__':

    f = CHello()
    f.push_back("-------------------------------------")
    f.push_back("  hello world ")
    f.push_back("-------------------------------------")
    f.printOut()
