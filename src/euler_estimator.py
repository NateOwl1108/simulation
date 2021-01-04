class EulerEstimator():
  def __init__(self, derivative, point):
    coordinates = str(point)
    coordinates = coordinates.replace('(', '')
    coordinates = coordinates.replace(')', '')
    coordinates = coordinates.split(',')
    
    self.x_value = int(coordinates[0])
    self.y_value = int(coordinates[1])
    self.point = (self.x_value, self.y_value)
    self.derivative = derivative
  
  def calc_derivative_at_point(self):
    return self.derivative(self.x_value)

  def step_forward(self, step):
    self.y_value += step * self.calc_derivative_at_point()
    self.y_value = round(self.y_value, 2)
    self.x_value += step
    self.x_value = round(self.x_value, 2)
    self.point = (self.x_value, self.y_value)
  
  def calc_estimated_points(self, initial_point , step_size, num_steps):
    coordinates = str(initial_point)
    coordinates = coordinates.replace('(', '')
    coordinates = coordinates.replace(')', '')
    coordinates = coordinates.split(',')
    self.x_value = float(coordinates[0])
    self.y_value = float(coordinates[1])
    for i in range(num_steps):
      self.step_forward(step_size)
      print(self.point)




euler = EulerEstimator(derivative = (lambda t: t+1),
                           point = (1,4))

print(euler.point)
(1,4)

print(euler.calc_derivative_at_point())
2   

euler.step_forward(0.1)
print(euler.point)
(1.1, 4.2)      

print(euler.calc_derivative_at_point())
2.1

euler.step_forward(-0.5)
print(euler.point)
(0.6, 3.15)    

euler.calc_estimated_points((0.6, 3.15),0.5,4)
[
    (0.6, 3.15),
    (1.1, 3.95), # after 1st step
    (1.6, 5), # after 2nd step
    (2.1, 6.3), # after 3rd step
    (2.6, 7.85), # after 4th step
]


