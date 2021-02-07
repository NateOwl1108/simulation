import matplotlib.pyplot as plt
plt.style.use('bmh')

class EulerEstimator():
  def __init__(self, derivatives):
    self.derivatives = derivatives
  
  def calc_derivative_at_point(self, point):
    return_values = dict(point[1])
    copy_dict = dict( self.derivatives)
    for key in point[1]:
      return_values[key] = copy_dict[key](point[0], point[1])
    return return_values

  def step_forward(self, point, step_size):
    
    
    x = float(point[0] + step_size)
    values = dict(point[1])
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

  def plot(self, initial_point, step_size, num_steps):
    function_values = self.calc_estimated_points(initial_point, step_size, num_steps)
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
  






