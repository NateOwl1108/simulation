import matplotlib.pyplot as plt
plt.style.use('bmh')

class EulerEstimator():
  def __init__(self, derivatives):
    self.derivatives = derivatives
  
  def calc_derivative_at_point(self, point):
    point_list = []
    for char in point:
      if char != '(' or char != ')':
        point_list.append(char)
    x = point_list[0]
    values = point_list[1]
    return_values = dict(values)
    
    for key in values:
      return_values[key] =  self.derivatives[key](x, values)
    return return_values

  def step_forward(self, point, step_size):
    
    point_list = []
    for char in point:
      if char != '(' or char != ')':
        point_list.append(char)
    x = point_list[0] + step_size
    values = point_list[1]
    derivative = self.calc_derivative_at_point(point)
    for key in values:
      values[key] = round(values[key] + step_size * derivative[key],9)
  
    return(x, values)
  
  def calc_estimated_points(self, point , step_size, num_steps):
    value_dict = dict(point[1])
    values = []
    values.append((point[0],value_dict))
    for i in range(num_steps):
      point = self.step_forward(point, step_size)
      value_dict = dict(point[1])

      values.append((point[0],value_dict))
      
    return values

  def plot(self):
    function_values = self.calc_estimated_points((0, {'A': 0, 'B': 0, 'C': 0}), 0.01, 500)
    for key in self.derivatives:
      function=[[],[]]
      for value in function_values:
        function[0].append(value[0])
        function[1].append(value[1][key])
      plt.plot(function[0], function[1] , label = key) 
    plt.xlabel('x - axis') 
    plt.ylabel('y - axis') 
    plt.legend() 
    plt.savefig('EulerEstimator.png')
  






