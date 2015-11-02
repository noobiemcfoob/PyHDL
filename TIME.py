##
# Specialized Net type for PyHDL time
class TIME(Net):
  def __init__(self,unit='ns'):
    super().__init__()

  def Drive(self):
    self.value = self.value + 1

    for listener in self.listeners:
      listener.Drive()
