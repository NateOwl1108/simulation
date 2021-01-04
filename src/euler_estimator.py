class EulerEstimator():
  def __init__(self, derivative):
    self.derivative = derivative
  
  def calc_derivative_at_point(self, point):
    coordinates = str(point)
    coordinates = coordinates.replace('(', '')
    coordinates = coordinates.replace(')', '')
    coordinates = coordinates.split(',')

    x_value = float(coordinates[0])
    return self.derivative(x_value)

  def step_forward(self, point, step_size):
    coordinates = str(point)
    coordinates = coordinates.replace('(', '')
    coordinates = coordinates.replace(')', '')
    coordinates = coordinates.split(',')
    
    x_value = float(coordinates[0])
    y_value = float(coordinates[1])
    y_value += step_size * self.calc_derivative_at_point(point)
    y_value = round(y_value, 2)
    x_value += step_size
    x_value = round(x_value, 2)
    return(x_value,y_value)
  
  def calc_estimated_points(self, point , step_size, num_steps):
    values = []
    values.append(point)
    for i in range(num_steps):
      point = self.step_forward(point, step_size)
      values.append(point)
      
    return values







