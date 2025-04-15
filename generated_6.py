Sure, I can generate a Python code as per your requirement. See the snippet below:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    # Input Validation
    if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("Invalid input data, expected a list of numeric values.")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("Invalid window size, should be a positive integer.")
    if window > len(data):
        raise ValueError("Window size should not be larger than the size of the data.")
    
    mov_avg = []
    for i in range(len(data) - window + 1):
        avg = sum(data[i: i + window]) / window
        mov_avg.append(round(avg, 2))
    return mov_avg

# Unit test
def test_calculate_moving_average():
    sample_data = [2.5, 3.2, 4.9, 5.1, 6.3, 7.4]
    window_size = 3
    expected_result = [3.53, 4.4, 5.44, 6.27]
    assert calculate_moving_average(sample_data, window_size) == expected_result

test_calculate_moving_average()
```

In this code, the `calculate_moving_average` function calculates the moving average from a provided list of floats over a given window. The function validates the inputs to ensure that the data is a list of numeric values, window is a positive integer, and that the window size is not larger than the size of the data. The `test_calculate_moving_average` function serves as the unit test for the moving average function.

Disclaimer: The use of assert statements in production code is generally discouraged, they should be used in test cases and debugging.