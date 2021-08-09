class Rectangle:

  def __init__(self, w, h):
    self.w = w
    self.h = h

  def __str__(self):
      return "Rectangle(width={}, height={})".format(self.w, self.h)

  def set_width(self, w):
    self.w = w

  def set_height(self, h):
    self.h = h

  def get_area(self):
    return self.w * self.h

  def get_perimeter(self):
    return (2 * self.w + 2 * self.h)
  
  def get_diagonal(self):
    return (self.w ** 2 + self.h ** 2) ** .5

  def get_picture(self):
    h = self.h
    w = self.w
    res = []
    if h < 50 and w < 50:
      for i in range(h):
        res.append(w * "*")
      res = '\n'.join(res) + "\n"
      return res
    else:
      return "Too big for picture."
  
  def get_amount_inside(self, shape):
    area_x = shape.get_area()
    area_y = self.get_area()
    i = 0 
    while area_y >= area_x:
      area_y = area_y - area_x
      i = i + 1
    return i
        

class Square(Rectangle):
    
  def __init__(self, s):
      super().__init__(s, s)

  def set_side(self, s):
    self.w = s
    self.h = s   
    return self.w, self.h

  def set_width(self, s):
    self.w = s
    self.h = s
    return self.w, self.h  

  def set_height(self, s):
    self.w = s
    self.h = s   
    return self.w, self.h  

  
  def __str__(self):
    return "Square(side={})".format(self.w)


