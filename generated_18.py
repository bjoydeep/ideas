Here is the Python code based on the mentioned GitHub issue.

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    if not isinstance(data, list) or not all(isinstance(i, float) for i in data):
        raise ValueError("data must be a list of floats.")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("window must be a positive integer.")
    if window > len(data):
        raise ValueError("window cannot be greater than the length of the data.")
    
    return [sum(data[i - window:i]) / window for i in range(window, len(data) + 1)]
    
    
# Test
data = [1.0, 2.0, 3.0, 4.0, 5.0]
window = 2
expected_output = [1.5, 2.5, 3.5, 4.5]
assert calculate_moving_average(data, window) == expected_output
```

About the test case: given the data [1.0, 2.0, 3.0, 4.0, 5.0] and a window of 2, the moving averages are:
- (1.0 + 2.0) / 2 = 1.5
- (2.0 + 3.0) / 2 = 2.5
- (3.0 + 4.0) / 2 = 3.5
- (4.0 + 5.0) / 2 = 4.5

So the expected output is [1.5, 2.5, 3.5, 4.5]