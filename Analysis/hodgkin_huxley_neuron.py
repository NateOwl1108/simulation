import math
import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

def alpha_n(t, x):
  V = x['V']
  return (0.01*(10-x['V']))/(math.exp(0.1*(10-x['V']))-1)

def beta_n(t,x):
  V = x['V']
  return 0.125*math.exp(-V/80)

def dn_dt(t,x):
    V = x['V']
    n = x['N']
    return alpha_n(t,x) * (1-n) - beta_n(t,x) * n

def alpha_m(t, x):
  V = x['V']
  return (0.1*(25-x['V']))/(math.exp(0.1*(25-x['V']))-1)

def beta_m(t,x):
  V = x['V']
  return  4*math.exp(-x['V']/18)

def dm_dt(t,x):
    V = x['V']
    m = x['N']
    return alpha_n(t,x) * (1-m) - beta_m(t,x) * m

def alpha_h(t, x):
  V = x['V']
  return 0.07*math.exp(-x['V']/20)

def beta_h(t,x):
  V = x['V']
  return  1/(math.exp(0.1*(30-x['V']))+1)

def dh_dt(t,x):
    V = x['V']
    h = x['H']
    return alpha_n(t,x) * (1-h) - beta_m(t,x) * h

def I_Na(t,x):
  V = x['V']
  h = x['H']
  m = x['M']
  return 120*(m**3)*h*(V-115)

def I_K(t,x):
  V = x['V']
  n = x['N']
  return 36*(n**4)*(V + 12)

def I_K(t,x):
  V = x['V']
  return 0.3*(V + 10.6)

def s(t):
  if t> 10 and t< 11:
    return 150
  elif t> 20 and t< 21:
    return 150
  elif t> 30 and t< 40:
    return 150
  elif t> 50 and t< 11:
    return 150
  elif t> 53 and t< 54:
    return 150
  elif t> 56 and t< 57:
    return 150
  elif t> 59 and t< 60:
    return 150
  elif t> 62 and t< 63:
    return 150
  elif t> 65 and t< 66:
    return 150
  else:
    return 0  
    
def dV_dt(t, x):
  return s(t)-I_Na(t,x) - I_K(t,x)- I_K(t,x)

derivatives = {
        'V': (lambda t,x: dV_dt(t,x)),
        'N': (lambda t,x: dn_dt(t,x)),
        'M': (lambda t,x: dm_dt(t,x)),
        'H': (lambda t,x: dh_dt(t,x))
    }

euler = EulerEstimator(derivatives = derivatives)

initial_values = {'V': 0, 'N': 0.317676914, 'M': 0.0529324854, 'H': 0.596120753}
initial_point = (0, initial_values)

euler.plot(initial_point, 0.01, 800)