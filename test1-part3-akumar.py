from hw2 import resolve
from hw2 import TELL
from hw2 import ASK
from hw2 import CLEAR

print "ASSIGNMENT 2 PART THREE"

print "---------test1-------------"
TELL(["implies", "a", "b"])
TELL(["implies", "b", "c"])
TELL("a")
print ASK("c")
CLEAR()

print "---------test2-------------"
TELL(["implies", "a", "b"])
TELL(["implies", "b", "c"])
TELL("a")
print ASK("d")
CLEAR()



