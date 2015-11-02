##
# A basic Register with a clock and asynchronous reset
class Register(Net):
  def __init__(
    self,
    clock,
    reset,
    d
  ):

    self.clock = clock.Listen(self)
    self.reset = reset.Listen(self)
    self.d     = d

  def Drive(self):
    if self.clock.GetValue() or self.reset.GetValue():
      if self.reset.GetValue():
        self.Value = 0
      else:
        self.Value = self.d.GetValue()
