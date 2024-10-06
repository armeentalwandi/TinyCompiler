import sys
from lexer import *

# parse object is gonna keep track of current and previous tokens and make sure they match the grammar
class Parse:
  def __init__(self, lexer):
    self.lexer = lexer
    self.curToken = None
    self.peekToken = None
    self.nextToken()
    self.nextToken() # initalizes peek and curr token properly!
    
    self.symbols = set()  # variables declared
    self.labelsDeclared = set()  # labels declared
    self.labelsGotoed = set() #labels go-toed


  # returns true if the current token matches the kind of the grammar
  def checkToken(self, kind):
    return self.curToken.kind == kind

  # returns true if the next token matches the kind of the grammar
  def checkPeek(self, kind):
    return self.peekToken.kind == kind

  # tries to match the current token. if not an error, moves on to the text token
  def match(self, kind):
    if self.checkToken(kind):
      self.nextToken()
    else:
      self.abort("token does not match. Expected: " + kind.name + ". Recieved: " + self.curToken.kind.name)
    

  # advances to the next token
  def nextToken(self):
    self.curToken = self.peekToken
    self.peekToken = self.lexer.getToken() # get token gets the next token! 

  # error message
  def abort(self, message):
    sys.exit("Error!: " + message)
  
  def nl(self):
    print("NEWLINE")
    self.match(TokenType.NEWLINE)
    while self.checkToken(TokenType.NEWLINE):
      self.nextToken()

 # entry point into the program:= {statement}
  def program(self):
    print("PROGRAM")
    while self.checkToken(TokenType.NEWLINE):
      self.nextToken()

    while not self.checkToken(TokenType.EOF):
      self.statement()
  
  def statement(self):
    # there are multiple types of statements
     # 1 . "PRINT" (expression | string)
    if self.checkToken(TokenType.PRINT):
      print("STATEMENT-PRINT")
      self.nextToken()

      if self.checkToken(TokenType.STRING):
        self.nextToken()
      else:
        self.expression()

    # 2.  "IF" comparison "THEN" nl {statement} "ENDIF" nl
    elif self.checkToken(TokenType.IF):
      print("STATEMENT-IF")
      self.nextToken()
      self.comparison()
      self.match(TokenType.THEN)
      self.nl()
      # 0 or more statements possible
      while not self.checkToken(TokenType.ENDIF):
        self.statement() 
      self.match(TokenType.ENDIF)

    # "WHILE" comparison "REPEAT" nl {statement nl} "ENDWHILE" nl
    elif self.checkToken(TokenType.WHILE):
      print("STATEMENT-WHILE")
      self.nextToken()
      self.comparison()
      self.match(TokenType.REPEAT)
      self.nl()

      while not self.checkToken(TokenType.ENDWHILE):
        self.statement()
        self.nl()
      
      self.match(TokenType.ENDWHILE)
    
    #"LABEL" ident nl
    elif self.checkToken(TokenType.LABEL):
      print("STATEMENT-LABEL")
      self.nextToken()
      self.match(TokenType.IDENT)
    
    # "GOTO" ident nl
    elif self.checkToken(TokenType.GOTO):
      print("STATEMENT-GOTO")
      self.nextToken()
      self.match(TokenType.IDENT)

     #  "LET" ident "=" expression nl
    elif self.checkToken(TokenType.LET):
      print("STATEMENT-LET")
      self.nextToken()
      self.match(TokenType.IDENT)
      self.match(TokenType.EQ)
      self.expression()
    
     # | "INPUT" ident nl
    elif self.checkToken(TokenType.INPUT):
      print("STATEMENT-INPUT")
      self.nextToken()
      self.match(TokenType.IDENT)
    
    else:
      self.abort("Not a valid statement: " + self.curToken.text + " - " + self.curToken.kind.name)

    self.nl()

 # comparison := expression (( == | != | > | < | >= | <= | ) expression)+  --> boolean expressions
  def comparison(self):
    print("COMPARISON")
    self.expression()

    # has to be atleast one comparison operator ANd another expression for it to be valid (the + indicates that)
    if self.checkToken(TokenType.EQEQ) or self.checkToken(TokenType.NOTEQ) or self.checkToken(TokenType.GT) \
      or self.checkToken(TokenType.LT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LTEQ):
        self.nextToken()
        self.expression()
    else:
      self.abort("Comparison operator error. Expected at " + self.curToken.text)
    
    # can have 0 or more MORE comparison operator and expressions after that
    while self.checkToken(TokenType.EQEQ) or self.checkToken(TokenType.NOTEQ) or self.checkToken(TokenType.GT) \
      or self.checkToken(TokenType.LT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LTEQ):
      self.nextToken()
      self.expression()
  
  # expression ::= term {( "-" | "+" ) term} --> {} means zero or more
  def expression(self):
    print("EXPRESSION")
    self.term()

    while self.checkToken(TokenType.MINUS) or self.checkToken(TokenType.PLUS):
      self.nextToken()
      self.term()
  
  # term ::= unary {( "/" | "*" ) unary}
  def term(self):
    print("TERM")
    self.unary()

    while self.checkToken(TokenType.SLASH) or self.checkToken(TokenType.ASTERISK):
      self.nextToken()
      self.unary()
  
  # unary ::= ["+" | "-"] primary  --> [] is one or zero -- its optional
  def unary(self):
    print("UNARY")
    if self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
      self.nextToken()
    self.primary()
  
   # primary ::= number | ident
  def primary(self):
    print("PRIMARY: " + self.curToken.text)
    if self.checkToken(TokenType.NUMBER):
      self.nextToken()
    elif self.checkToken(TokenType.IDENT):
      self.nextToken()
    else:
      self.abort("Unexpected token: " + self.curToken.text)
  







  


         
         






