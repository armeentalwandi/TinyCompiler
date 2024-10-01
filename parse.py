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





