from hw2 import resolve

print "ASSIGNMENT 2 PART ONE"

print "---------test1-------------"
print resolve(["or", "a", "b", "c"], ["not", "b"])

print "---------test2-------------"
print resolve(["or", "a", "b", "c"], ["or", "b", ["not", "c"]])

print "---------test3-------------"
print resolve(["or", ["not", "raining"], "wet ground"], "raining")

print "----------test4------------"
print resolve(["or", "a", "b"], "c")

print "----------test5------------"
print resolve("a",["not","a"])
