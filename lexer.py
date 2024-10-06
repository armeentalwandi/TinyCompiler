# source code --> Lexer --> tokens --> Parser --> program tree -> Emitter --> compiled code

# lexer = converts a string of teeny tiny code to tokens
# a parser = parses the tokens to make sure the correct syntax is being followed
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
      while self.currChar != '\n':
        self.nextChar()
      


  def skipWhitespace(self):
    while self.currChar == ' ' or self.currChar == '\t' or self.currChar == '\r':
      self.nextChar()
    

# main function --> gets the next token
  def getToken(self):
    
    self.skipWhitespace() #if the curr char is a white space, it immediately skips it
    self.skipComment() #if there is a comment, its skipped immediately
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

    elif self.currChar == '\"':  # Get characters between quotations.
      self.nextChar()
      startPos = self.currPos
      while self.currChar != '\"':
        if self.currChar == '\r' or self.currChar == '\n' or self.currChar == '\t' or self.currChar == '\\' or self.currChar == '%':
          self.abort("Illegal character in string.")
        self.nextChar()

      tokText = self.source[startPos : self.currPos] # Get the substring.
      token = Token(tokText, TokenType.STRING)  

    elif self.currChar.isdigit():
      startPos = self.currPos
      while self.peek().isdigit():
        self.nextChar()

      if self.peek() == '.':
        self.nextChar()
        if not self.peek().isdigit():
          self.abort("incorrect number format")
        while self.peek().isdigit():
          self.nextChar()
      
      tottext = self.source[startPos: self.currPos + 1]
      token = Token(tottext, TokenType.NUMBER)
        
    #handling keywords and identifiers 
    elif self.currChar.isalpha():
            # leading character is a letter 
            startPos = self.currPos
            while self.peek().isalnum():
                self.nextChar()

            # Check if the token is in the list of keywords or an identifier
            tokText = self.source[startPos : self.currPos + 1] # Get the substring.
            keyword = Token.checkIfKeyword(tokText)

            if keyword == None: # Identifier
                token = Token(tokText, TokenType.IDENT)
            else:   # Keyword
                token = Token(tokText, keyword)
    
    else:
      #unknown token ! aka not a single char operator
      self.abort("not recognized: " + self.currChar)

    self.nextChar()
    return token
    


