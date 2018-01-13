from hw2 import resolve
from hw2 import TELL
from hw2 import ASK
from hw2 import CLEAR

print "ASSIGNMENT 2 PART TWO"

print "---------test1-------------"
TELL(["or", ["not", "a"], "b"])
TELL(["or", ["not", "b"], "c"])
TELL("a")
print ASK("c")
CLEAR()

print "---------test2-------------"
TELL(["or", ["not", "a"], "b"])
TELL(["or", ["not", "b"], "c"])
TELL("a")
print ASK("d")
CLEAR()

print "---------test3-------------"
TELL(["or", "p", "q"])
TELL(["or", ["not", "p"], "r"])
TELL(["or", ["not", "q"], "r"])
print ASK("r")
CLEAR()

print "---------test4-------------"
TELL(["not","p"])
TELL("p")
print ASK("z")
CLEAR()

print "---------test5-------------"
TELL(["not","z"])
TELL("p")
print ASK("z")
CLEAR()
