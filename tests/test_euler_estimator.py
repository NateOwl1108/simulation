import sys
sys.path.append('src')
from euler_estimator import EulerEstimator


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