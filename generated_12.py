Sure, here is how you can implement a moving average function using Python's built-in standard libraries:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
        raise TypeError("Data should be a list of numbers")
        
    if not isinstance(window, int) or window <= 0:
        raise ValueError("Window size should be a positive integer")
        
    if window > len(data):
        raise ValueError("Window size should not be larger than the data length")

    moving_avgs = []
    for i in range(len(data) - window + 1):
        subset = data[i:i + window]
        avg = sum(subset) / window
        moving_avgs.append(round(avg, 2))
    
    return moving_avgs

# test case
print(calculate_moving_average([2.2, 3.3, 4.4, 5.5, 6.6, 7.7], 3))
```
This function `calculate_moving_average(data: List[float], window: int) -> List[float]` takes two arguments, `data` which is a list of floating-point numbers and `window` which is an integer for the calculation of moving average. The function validates the input and raises an exception if the input is invalid, then calculates the moving average using a sliding window method.

The printed output from the test case should be: `[3.3, 4.4, 5.5, 6.6]` which represents the moving average of the input data with a window size of 3.