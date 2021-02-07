import sys
sys.path.append('src')
from euler_estimator import EulerEstimator
#SIR infection model
'''
derivatives = {
        'S': (lambda t,x: -0.0003*x['S']*x['I']),
        'I': (lambda t,x: 0.0003*x['S']*x['I'] - 0.02*x['I']),
        'R': (lambda t,x: 0.02*x['I']) 
    }

euler = EulerEstimator(derivatives = derivatives)

initial_values = {'S': 1000, 'I': 1, 'R': 0}
initial_point = (0, initial_values)

euler.plot(initial_point, 0.2, 1500)
'''
derivatives = {
        'D': (lambda t,x: 0.6*x['D'] - 0.05*x['D']*x['W']),
        'W': (lambda t,x: -0.9*x['W'] + 0.02*x['D']*x['W']),

    }

euler = EulerEstimator(derivatives = derivatives)

initial_values = {'D': 100, 'W': 10}
initial_point = (0, initial_values)
euler.plot(initial_point, 0.001, 100000)