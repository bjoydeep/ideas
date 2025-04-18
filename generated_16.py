Here's a Python code sample based on the requirements:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    # Basic input validation
    if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
        raise ValueError('Data must be a list of numbers')
    
    if not isinstance(window, int) or window <= 0:
        raise ValueError('Window must be a positive integer')
    
    moving_averages = []
    for i in range(len(data) - window + 1):
        this_window = data[i : i + window]
        window_avg = sum(this_window) / window
        moving_averages.append(window_avg)
    return moving_averages

# Test
data = [1.0, 2.0, 3.0, 4.0, 5.0]
window = 3
expected_result = [2.0, 3.0, 4.0]
assert calculate_moving_average(data, window) == expected_result, "Test Case 1 Failed"

data = [5.0, 15.0, -10.0, 20.0, -5.0]
window = 2
expected_result = [10.0, 2.5, 5.0, 7.5]
assert calculate_moving_average(data, window) == expected_result, "Test Case 2 Failed"

print("All test cases passed.")
```

This code defines the function `calculate_moving_average` that calculates the moving average of the input data with a given window size. It includes basic input validation to ensure that the inputs are valid before processing. Two test cases are also provided to check the correctness of the function.