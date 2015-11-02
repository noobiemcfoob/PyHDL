##
# PyHDL class for Net Data type
class Net(pyhdl_object):
  def __init__(self, driver):
    super().__init__()

    self.value = None
    self.listeners = list()

    self.Drive = driver

  def Drive(self):
    pass

  def Listen(self, listener):
    self.listeners.append(listener)

    return self

  def GetValue(self):
    return self.value