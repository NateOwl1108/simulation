
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
