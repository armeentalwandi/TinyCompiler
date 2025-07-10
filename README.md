# Tiny Compiler

A simple compiler for a minimal BASIC-like language written in Python, it lexes  source files, parses them via a recursive-descent parser, and emits equivalent C code that you can build with GCC or Clang. 

## Features
- **Lexing & Parsing** of keywords, identifiers, numbers, strings, operators, and comments
- **Print** statements:  
  - `PRINT "text"`  
  - `PRINT expression`
- **Input** statements:  
  - `INPUT var`
- **Variable assignment**:  
  - `LET x = expression` 
- **Control flow**:  
  - `IF comparison THEN … ENDIF`  
  - `WHILE comparison REPEAT … ENDWHILE` 
- **Labels & GOTO**:  
  - `LABEL name` / `GOTO name` 
- **Comments**: single-line starting with `#` 
- **Build script**: `build.sh` automates compilation & linking 

## Getting Started

- Python 3.x  
- GCC or Clang 
