
class Code:
  def __init__(self,codigo):
    self.codigo = codigo
    self.operand_one = codigo[1]
    self.operand_two = codigo[2]
    self.location = codigo[3]
  def operacion():
    if codigo[0]==1:
      return operand_one + operand_two
    elif codigo[0]==2:
      return operand_one * operand_two
    elif codigo[0]==99:
      return null
  def locacion():
    return location