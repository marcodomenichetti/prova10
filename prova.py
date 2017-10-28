#import mysqlite
from mylibrary import *

mypath = '/Users/marcodomenichetti/Desktop/new/largeText.db'
tabella = 'myTable'


mysqlite.sqOpen(mypath)
print mysqlite.sqLen(tabella)
mysqlite.sqClose()
