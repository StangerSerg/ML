import math


class Bernoulli:
  def __init__(self, p):
    self.p = p

  def prob(self, x):
    if x not in (0, 1):
      raise ValueError(f"Value of x should be 0 or 1, {x} gain!")
                       
    return self.p if x else 1 - self.p
