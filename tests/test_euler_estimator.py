import sys
sys.path.append('src')
from euler_estimator import EulerEstimator
'''

euler = EulerEstimator(derivative = (lambda t: t+1))

assert euler.calc_derivative_at_point((1,4)) == 2

assert euler.step_forward(point=(1,4), step_size=0.5) == (1.5, 5)

assert euler.calc_estimated_points(point=(1,4), step_size=0.5, num_steps=4) == [
    (1, 4), # starting point
    (1.5, 5), # after 1st step
    (2, 6.25), # after 2nd step
    (2.5, 7.75), # after 3rd step
    (3, 9.5) # after 4th step
]'''

derivatives = {
        'A': (lambda t,x: x['A'] + 1),
        'B': (lambda t,x: x['A'] + x['B']),
        'C': (lambda t,x: 2*x['B']) 
    }

euler = EulerEstimator(derivatives = derivatives)

initial_values = {'A': 0, 'B': 0, 'C': 0}
initial_point = (0, initial_values)

assert euler.calc_derivative_at_point(initial_point) == {'A': 1, 'B': 0, 'C': 0}

point_2 = euler.step_forward(point = initial_point, step_size = 0.1)
assert point_2 == (0.1, {'A': 0.1, 'B': 0, 'C': 0})

assert euler.calc_derivative_at_point(point_2) == {'A': 1.1, 'B': 0.1, 'C': 0}

point_3 = euler.step_forward(point = point_2, step_size = -0.5)
assert point_3 == (-0.4, {'A': -0.45, 'B': -0.05, 'C': 0})

assert euler.calc_estimated_points(point=point_3, step_size=2, num_steps=3) == [
   (-0.4, {'A': -0.45, 'B': -0.05, 'C': 0}), # starting point 
   (1.6, {'A': 0.65, 'B': -1.05, 'C': -0.2}), # after 1st step
   (3.6, {'A': 3.95, 'B': -1.85, 'C': -4.4}), # after 2nd step
   (5.6, {'A': 13.85, 'B': 2.35, 'C': -11.8}) # after 3rd step
]

euler.plot()
