# source code --> Lexer --> tokens --> Parser --> program tree -> Emitter --> compiled code

# lexer = converts a string of teeny tiny code to tokens
from token1 import *


class Lexer:
  def __init__(self, source) -> None:
    self.source = source + '\n' #convert sc to a string
    self.currChar = '' # curr character
    self.currPos = -1 #curr pos in string
    self.nextChar() 

  def nextChar(self):
    self.currPos += 1
    if self.currPos >= len(self.source):
      self.currChar = '\0' #EOF!!
    else :
      self.currChar = self.source[self.currPos]

  def peek(self):
    if self.currPos + 1 < len(self.source):
      return self.source[self.currPos + 1]
    return '\0'

    
  def abort(self, message):
    pass

  def skipComment(self):
    pass

  def skipWhitespace(self):
    pass

# main function --> gets the next token
  def getToken(self):
    token = None
    if self.currChar == '+':
      token = Token(self.currChar, TokenType.PLUS)
    elif self.currChar == '-':
      token = Token(self.currChar, TokenType.MINUS)
    elif self.currChar == '*':
      token = Token(self.currChar, TokenType.ASTERISK)
    elif self.currChar == '/':
      token = Token(self.currChar, TokenType.SLASH)
    elif self.currChar == '\n':
      token = Token(self.currChar, TokenType.NEWLINE)
    elif self.currChar == '\0':
      token = Token('', TokenType.EOF)
    else:
      #unknown token ! aka not a single char operator
      pass

    self.nextChar()
    return token
    


