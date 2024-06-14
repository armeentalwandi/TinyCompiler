from lexer import *

def main():
  source = "+-/ *"
  lexer = Lexer(source)

  token = lexer.getToken() # gets the token and moves position to the next one
  while token.kind != TokenType.EOF:
    print(token.kind)
    print(token.text)
    token = lexer.getToken() #runs the function again


main()

