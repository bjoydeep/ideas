Here's a Python function following the details you provided:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    """Calculates moving average based on the specified data and window width."""
    
    # Input validation
    if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("Data must be a list of numbers.")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("Window must be a positive integer.")
    if window > len(data):
        raise ValueError("Window must not be greater than data length.")

    return [sum(data[i - window:i]) / window for i in range(window, len(data) + 1)]


# Test case:
# moving_average([1.0, 2.0, 3.0, 4.0, 5.0], 3) should return [2.0, 3.0, 4.0]
data = [1.0, 2.0, 3.0, 4.0, 5.0]
window = 3
print(calculate_moving_average(data, window))  # Expected output: [2.0, 3.0, 4.0]
```
In this script, the `calculate_moving_average` function first checks if its inputs are valid. If not, it raises a `ValueError`. If the inputs are valid, it calculates the moving average of the data and returns the result as a list of floats.

Finally, the script has a test case that you can run to check if the function is working as expected. The test case uses the `print` function to display the output of the `calculate_moving_average` function.