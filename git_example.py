```
This python file si a goood starting pouint.
Activation Funstions
```

#libraries
import numpy as np

def sigmoid(x):
  # enter code below
  return (1 / (1 + np.exp(-x)))

def tanh(x):
  return (np.exp(x) - np.exp(-x) )/( np.exp(x) + np.exp(-x))
  
def relu(x):
  return max(0, x)
  
