These are some examples on how to use the inference engine.

This program has 2 use cases. The first is a simple resolution function in which you can enter 2 sentences and the resolved output will be displayed. Some examples on how to use this are shown below :

EXAMPLE 1
  print resolve(["or", "a", "b", "c"], ["not", "b"])

EXAMPLE 2
  print resolve(["or", "a", "b", "c"], ["or", "b", ["not", "c"]])

EXAMPLE 3
  print resolve(["or", ["not", "raining"], "wet ground"], "raining")

EXAMPLE 4
  print resolve(["or", "a", "b"], "c")

EXAMPLE 5
  print resolve("a",["not","a"])



The second use case is that of a Complete Resolution Reference Engine. That means you can enter some sentences into the knowledge base and enter a query. The program will then return whether the query is satisfiable (no new resolutions are possible) or contradictory. Some examples are shown below:


EXAMPLE 1
  TELL(["or", ["not", "a"], "b"])
  TELL(["or", ["not", "b"], "c"])
  TELL("a")
  print(ASK("c"))
  CLEAR()

EXAMPLE 2
  TELL(["or", ["not", "a"], "b"])
  TELL(["or", ["not", "b"], "c"])
  TELL("a")
  print(ASK("d"))
  CLEAR()

EXAMPLE 3
  TELL(["or", "p", "q"])
  TELL(["or", ["not", "p"], "r"])
  TELL(["or", ["not", "q"], "r"])
  print(obj.ASK("r"))
  CLEAR()

EXAMPLE 4
  TELL(["not","p"])
  TELL("p")
  print(ASK("z"))
  CLEAR()

EXAMPLE 5
  TELL(["not","z"])
  TELL("p")
  print(ASK("z"))
  CLEAR()

