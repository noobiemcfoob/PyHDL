
class Counter(Net):
  def __init__( self,
                clk,
                ares              
  ):
    super().__init__()

    self.clk        = clk.listen()
    self.ares       = ares.listen()

    self.count_reg  = Register(clock = clk, reset=ares, d=self)

  
  def Drive(self):
    self.value = self.count_reg + 1