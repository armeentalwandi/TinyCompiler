from lexer import *
from parse import *
from emitter import *
import sys

def main():
  print("My Tiny Compiler")
  if len(sys.argv) != 2:
    sys.exit("argument number is incorrect")
  
  with open(sys.argv[1], 'r') as source_file: #opens (and takes care of closing the entire file - source_file is the variable assigned to the opened file)
    source = source_file.read() #reads the entire file and stores in source

  lexer = Lexer(source)
  emitter = Emitter("out.c")
  parser = Parse(lexer, emitter)

  parser.program()
  emitter.writeFile()
  print("Compiling complete")

  # token = lexer.getToken() # gets the token and moves position to the next one
  # while token.kind != TokenType.EOF:
  #   print(token.kind)
  #   print(token.text)
  #   token = lexer.getToken() #runs the function again


main()

