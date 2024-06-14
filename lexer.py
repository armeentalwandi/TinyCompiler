# source code --> Lexer --> tokens --> Parser --> program tree -> Emitter --> compiled code

# lexer = converts a string of teeny tiny code to tokens
from token1 import *
import sys


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
    sys.exit("Lexing error: " + message)
    

  def skipComment(self):
    if self.currChar == '#': # aka start of a comment
      while self.currChar != '/n':
        self.nextChar()
      


  def skipWhitespace(self):
    if self.currChar == ' ' or self.currChar == '\t' or self.currChar == '\r':
      self.nextChar()
    

# main function --> gets the next token
  def getToken(self):
    token = None
    self.skipWhitespace() #if the curr char is a white space, it immediately skips it
    self.skipComment() #if there is a comment, its skipped immediately
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

    elif self.currChar == '=':
      if self.peek() == '=':
        token = Token('==', TokenType.EQEQ)
        self.nextChar()
      else:
        token = Token('=', TokenType.EQ)

    elif self.currChar == '!':
      if self.peek() != '=':
        self.abort("Unidentified token: " + self.currChar + self.peek())
      token =  Token('!=', TokenType.NOTEQ)
      self.nextChar()

    elif self.currChar == '>':
      if self.peek() == '=':
        token =  Token('>=', TokenType.GTEQ)
        self.nextChar()
      else:
        token = Token('>', TokenType.GT)

    elif self.currChar == '<':
      if self.peek() == '=':
        token =  Token('<=', TokenType.LTEQ)
        self.nextChar()
      else:
        token = Token('<', TokenType.LT)

    else:
      #unknown token ! aka not a single char operator
      self.abort("not recognized: " + self.currChar)

    self.nextChar()
    return token
    


