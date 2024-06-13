from lexer import *

def main():
  source = "LET foobar = 123"
  lexer = Lexer(source)

  while lexer.peek() != '\0':
    print(lexer.currChar)
    lexer.nextChar()


main()
