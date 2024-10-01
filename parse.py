import sys
from lexer import *

# parse object is gonna keep track of current and previous tokens and make sure they match the grammar
class Parse:
  def __init__(self, lexer):
    pass

  # returns true if the current token matches the kind of the grammar
  def checkToken(self, kind):
    pass

  # returns true if the next token matches the kind of the grammar
  def checkPeek(self, kind):
    pass

  # tries to match the current token. if not an error, moves on to the text token
  def match(self, kind):
    pass

  # advances to the next token
  def nextToken(self):
    pass

  # error message
  def abort(self, message):
    sys.exit("Error!: " + message)





