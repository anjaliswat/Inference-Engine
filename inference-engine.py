import copy

#----------------------------------------------ASSIGNMENT 2 PART ONE-----------------------------------------------

def resolve(s1,s2):

  contradictions = 0
  operands1 = []
  notoperands1 = []
  operands2 = []
  notoperands2 = []
  notoperands2array = []
  notoperands1array = []
  sentence1 = []
  sentence2 = []

  #This defines the lists sentence1 and sentence2 baseed on the parameters s1 and s2 passed in to the function

  if isinstance(s1, basestring):
    sentence1.append(s1)
  else:
    sentence1 = s1

  if isinstance(s2, basestring):
    sentence2.append(s2)
  else:
    sentence2 = s2

  #This function goes through the clauses in each sentence and divides the clauses with a "not" as a prefix into the not operands list and the ones without a "not" operand in the operands list

  def parsingClauses(sentence,notoperandsarray,notoperands,operands):
    #The operator is initialized with "or"
    operator = "or"
    for clause in sentence:
      #Checks whether the element in the list is a string or an array. If it is a string we proceed otherwise we go to the elif statement below.
      if isinstance(clause, basestring):
        #Checks whether the current clause is an operator or not
        if clause != "not":
          if clause != "or":
            #If the operator is "not" then the operand will be added to the notoperands list
            if operator == "not":
              notoperandsarray.append(["not",clause])
              notoperands.append(clause)
              operator = "or"
            #If the operator is an "or" then the operand will be added to the operands list
            else:
              operands.append(clause)
        else:
          if clause == "not":
            operator = "not"
          elif clause == "or":
            operator = "or"

      #If the element in the list is a list, then we traverse through that list
      elif isinstance(clause, list):
        for element in clause:
          if element != "not":
            if element != "or":
              if operator == "not":
                notoperandsarray.append(["not",element])
                notoperands.append(element)
                operator = "or"
              else:
                operands.append(element)
          else:
            if element == "not":
              operator = "not"
            elif element == "or":
              operator = "or"


  parsingClauses(sentence1,notoperands1array,notoperands1,operands1)
  parsingClauses(sentence2,notoperands2array,notoperands2,operands2)

  #This function removes any common variables between both sentences and extra "or" operators present in the sentences
  def removeCommonVariables():
    for index1, clause1 in enumerate(operands1):
      for index2, clause2 in enumerate(operands2):
        if clause1 == clause2:
          sentence2.remove(clause2)
        if sentence2 == clause2:
          for i in sentence2:
            sentence2.remove(sentence2[i])


    for index1, clause1 in enumerate(notoperands1):
      for index2, clause2 in enumerate(notoperands2):
        if clause1 == clause2:
          clause2 = notoperands2array[index2]
          if sentence2 == clause2:
            for index,i in enumerate(sentence2):
              sentence2.remove(sentence2[index])
          else:
            sentence2.remove(clause2)

    for y in sentence2:
      if y == "or":
        sentence2.remove(y)

  removeCommonVariables()

  #The number of contradictions will be calculated here
  for index1, clause1 in enumerate(operands1):
    for index2, clause2 in enumerate(notoperands2):
      if clause1 == clause2:
        contradictions = contradictions + 1
        resolvingclause1 = operands1[index1]
        resolvingclause2 = notoperands2array[index2]

  for index1, clause1 in enumerate(notoperands1):
    for index2, clause2 in enumerate(operands2):
      if clause1 == clause2:
        contradictions = contradictions + 1
        resolvingclause1 = notoperands1array[index1]
        resolvingclause2 = operands2[index2]

  #If the number of contradictions is equal to one that means the 2 sentences can be resolved. The sentences will be resolved and the result will be returned

  if contradictions == 1:
    if sentence1 == resolvingclause1:
      sentence1 = []
    if sentence2 == resolvingclause2:
      sentence2 = []
    for x in sentence1:
      if x == resolvingclause1:
        sentence1.remove(x)
    for y in sentence2:
      if y == resolvingclause2:
        sentence2.remove(y)
    resolvedsentence = sentence1 + sentence2
    if len(resolvedsentence) == 2:
      resolvedsentence.remove(resolvedsentence[0])
      resolvedsentence = resolvedsentence[0]
    return resolvedsentence
  #If the number of contradictions is less than or greater than 1 that means it can not be resolved. It will return "False"
  else:
    return "False"

#----------------------------------------------ASSIGNMENT 2 PART TWO AND THREE-----------------------------------------------

knowledgeBase = []

def TELL(sentence):
    #Checks if the operator is biconditional and will convert according to CNF
    for index, element in enumerate(sentence):
      if element == "biconditional":
        variable1 = sentence[index+1]
        variable2 = sentence[index+2]
        sentence = [["implies",variable1,variable2],["implies",variable2,variable1]]

    #Checks if the operator is implies and will convert according to CNF
    for index, element in enumerate(sentence):
      if element == "implies":
        sentence[index] = "or"
        sentence[index+1] = ["not",sentence[index+1]]

    #Checks if operator is not and will remove any double negations
    for index, element in enumerate(sentence):
      if element == "not":
        if isinstance(sentence[index+1], list):
          if sentence[index+1][0] == "or":
            sentence[index+1][0] = "and"
            if sentence[index+1][1] != "not":
              sentence[index+1][1] = ["not",sentence[index+1][1]]
            elif sentence[index+1][1] == "not":
              sentence.remove(sentence[index+1][1])
            if sentence[index+1][2] != "not":
              sentence[index+1][2] = ["not",sentence[index+1][2]]
            elif sentence[index+1][2] == "not":
              sentence.remove(sentence[index+1][2])
            sentence.remove(element)

          elif sentence[index+1][0] == "not":
            sentence.remove(element)

          elif sentence[index+1][0] == "and":
            sentence[index+1][0] = "or"
            if sentence[index+1][1] != "not":
              sentence[index+1][1] = ["not",sentence[index+1][1]]
            elif sentence[index+1][1] == "not":
              sentence.remove(sentence[index+1][1])
            if sentence[index+1][2] != "not":
              sentence[index+1][2] = ["not",sentence[index+1][2]]
            elif sentence[index+1][2] == "not":
              sentence.remove(sentence[index+1][2])
            sentence.remove(element)
    knowledgeBase.append(sentence)

def ASK(query):
  if isinstance(query, basestring):
    TELL(["not",query])
  elif isinstance(query, list):
    if query[0] == "not":
      TELL(query[1])
    elif query[0] != "not":
      TELL(["not",query])

  index1 = 0
  while index1 < len(knowledgeBase):
    index2 = index1 + 1
    while index2 < len(knowledgeBase):
      #This will create a deep copy of that particular sentence in the knowledgeBase so that the original value in the knowledgeBase does not change
      sent1 = copy.deepcopy(knowledgeBase[index1])
      sent2 = copy.deepcopy(knowledgeBase[index2])
      resolution = resolve(sent1,sent2)
      #Checks if the variable is not an empty clause and is not equal to false, then we will add it to the knowledge base.
      if resolution != []:
        if resolution != "False":
          knowledgeBase.append(resolution)
      #If the resolution results into an empty clause that means that the query has been succesfully proved and hence will return TRUE
      elif resolution == []:
        return "True"
      index2 = index2 + 1
    index1 = index1 + 1
  #If this sentence runs then that means that no further resolutions can be made and hence will return FALSE
  return "False"

def CLEAR():
  global knowledgeBase
  knowledgeBase = []
