from lexer import *
from parse import *
import sys

def main():
  if len(sys.argv) != 2:
    sys.exit("argument number is incorrect")
  
  source_file = open(sys.argv[1], 'r')
  source = source_file.read()


  lexer = Lexer(source)
  parser = Parse(lexer)

  parser.program()
  print("parsing complete")

  # token = lexer.getToken() # gets the token and moves position to the next one
  # while token.kind != TokenType.EOF:
  #   print(token.kind)
  #   print(token.text)
  #   token = lexer.getToken() #runs the function again


main()

