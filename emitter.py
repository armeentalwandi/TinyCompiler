
class Emitter:
  def __init__(self, fileName):
    self.fileName = fileName
    self.header = ""
    self.code = ""

  def emit(self, code):
    self.code += code

  def emitLine(self, code):
    self.code += code + '\n'

  def headerLine(self, code):
    self.header += code + '\n'

  def writeFile(self):
    with open(self.fileName, 'w') as outputFile:
      outputFile.write(self.header + self.code)

  