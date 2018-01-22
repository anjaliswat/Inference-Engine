import copy

class Resolve:

  def _init_(self):
    self.contradictions = 0
    self.operands_sent1 = []
    self.notoperands_sent1 = []
    self.operands_sent2 = []
    self.notoperands_sent2 = []
    self.clauses_sent1 = []
    self.clauses_sent2 = []
    self.sentence1 = []
    self.sentence2 = []
    self.knowledgeBase = []

    #This defines the lists sentence1 and sentence2 baseed on the parameters s1 and s2 passed in to the function
  def defineSentence(self,s1,s2):
      if isinstance(s1, basestring):
        self.sentence1.append(s1)
      else:
        self.sentence1 = s1

      if isinstance(s2, basestring):
        self.sentence2.append(s2)
      else:
        self.sentence2 = s2

  #This function goes through the clauses in each sentence and divides the clauses with a "not" as a prefix into the not operands list and the ones without a "not" operand in the operands list

  def parsingClauses(self,sentence,notoperandsarray,notoperands,operands):
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
                notoperandsarray.append(["not", element])
                notoperands.append(element)
                operator = "or"
              else:
                operands.append(element)
          else:
            if element == "not":
              operator = "not"
            elif element == "or":
              operator = "or"

  #This function removes any common variables between both sentences and extra "or" operators present in the sentences
  def removeCommonVariables(self):
    for index_sent1, clause_sent1 in enumerate(self.operands_sent1):
      for index_sent2, clause_sent2 in enumerate(self.operands_sent2):
        if clause_sent1 == clause_sent2:
          self.sentence2.remove(clause_sent2)
        if self.sentence2 == clause_sent2:
          for elem in self.sentence2:
            self.sentence2.remove(self.sentence2[elem])

    for index_sent1, clause_sent1 in enumerate(self.notoperands_sent1):
      for index_sent2, clause_sent2 in enumerate(self.notoperands_sent2):
        if clause_sent1 == clause_sent2:
          clause_sent2 = self.clauses_sent2[index_sent2]
          if self.sentence2 == clause_sent2:
            for index,elem in enumerate(self.sentence2):
              self.sentence2.remove(self.sentence2[index])
          else:
            self.sentence2.remove(clause_sent2)

    for elem in self.sentence2:
      if elem == "or":
        self.sentence2.remove(elem)

  def calculate_contradictions(self):
  #The number of contradictions will be calculated here
    for index1, clause1 in enumerate(self.operands_sent1):
      for index2, clause2 in enumerate(self.notoperands_sent2):
        if clause1 == clause2:
          self.contradictions = self.contradictions + 1
          self.resolvingclause1 = self.operands_sent1[index1]
          self.resolvingclause2 = self.clauses_sent2[index2]

    for index1, clause1 in enumerate(self.notoperands_sent1):
      for index2, clause2 in enumerate(self.operands_sent2):
        if clause1 == clause2:
          self.contradictions = self.contradictions + 1
          self.resolvingclause1 = self.clauses_sent1[index1]
          self.resolvingclause2 = self.operands_sent2[index2]

  #If the number of contradictions is equal to one that means the 2 sentences can be resolved. The sentences will be resolved and the result will be returned
    if self.contradictions == 1:
      if self.sentence1 == self.resolvingclause1:
        self.sentence1 = []
      if self.sentence2 == self.resolvingclause2:
        self.sentence2 = []
      for clause in self.sentence1:
        if clause == self.resolvingclause1:
          self.sentence1.remove(clause)
      for clause in self.sentence2:
        if clause == self.resolvingclause2:
          self.sentence2.remove(clause)
      self.resolvedsentence = self.sentence1 + self.sentence2
      if len(self.resolvedsentence) == 2:
        self.resolvedsentence.remove(self.resolvedsentence[0])
        self.resolvedsentence = self.resolvedsentence[0]
      return(self.resolvedsentence)
      #If the number of contradictions is less than or greater than 1 that means it can not be resolved. It will return "False"
    else:
      return("False")

  def resolve_sentences(self):
    self.parsingClauses(self.sentence1, self.clauses_sent1, self.notoperands_sent1, self.operands_sent1)
    self.parsingClauses(self.sentence2, self.clauses_sent2, self.notoperands_sent2, self.operands_sent2)
    self.removeCommonVariables()
    solution = self.calculate_contradictions()
    return solution

  def reset_values(self):
    self.contradictions = 0
    self.operands_sent1 = []
    self.notoperands_sent1 = []
    self.operands_sent2 = []
    self.notoperands_sent2 = []
    self.clauses_sent1 = []
    self.clauses_sent2 = []
    self.sentence1 = []
    self.sentence2 = []

  # Accepts one arguement (a sentence) and adds that sentence to the knowledge base
  def TELL(self,sentence):
      self.knowledgeBase.append(sentence)

  # Accepts a single arguement (a single proposition or negated proposition) and returns True or False.
  # This indicates whether the query is true or cant be determined.
  def ASK(self,query):
    if isinstance(query, basestring):
      self.TELL(["not",query])
    elif isinstance(query, list):
      if query[0] == "not":
        self.TELL(query[1])
      elif query[0] != "not":
        self.TELL(["not",query])

    index1 = 0
    while index1 < len(self.knowledgeBase):
      index2 = index1 + 1
      while index2 < len(self.knowledgeBase):
        #This will create a deep copy of that particular sentence in the knowledgeBase so that the original value in the knowledgeBase does not change
        sent1 = copy.deepcopy(self.knowledgeBase[index1])
        sent2 = copy.deepcopy(self.knowledgeBase[index2])

        self.reset_values()
        self.defineSentence(sent1,sent2)
        resolution = self.resolve_sentences()
        #Checks if the variable is not an empty clause and is not equal to false, then we will add it to the knowledge base.
        if resolution != []:
          if resolution != "False":
            self.knowledgeBase.append(resolution)
        #If the resolution results into an empty clause that means that the query has been succesfully proved and hence will return TRUE
        elif resolution == []:
          return "True"
        index2 = index2 + 1
      index1 = index1 + 1
    #If this sentence runs then that means that no further resolutions can be made and hence will return FALSE
    return("False")

  #Will clear the knowledge base
  def CLEAR(self):
    self.knowledgeBase = []
