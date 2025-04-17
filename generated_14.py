Sure, here is the Python code as per your requirement:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    if not isinstance(data, list):
        raise TypeError('The data must be a list.')
    if not all(isinstance(i, (int, float)) for i in data):
        raise TypeError('All elements in the data must be numbers.')
    if not isinstance(window, int):
        raise TypeError('The window value must be an integer.')
    if window <= 0:
        raise ValueError('The window value must be greater than 0.')
    if window > len(data):
        raise ValueError('The window value must not be greater than the length of the data list.')

    moving_averages = []
    for i in range(len(data) - window + 1):
        this_window = data[i : i + window]
        window_avg = sum(this_window) / window
        moving_averages.append(window_avg)
        
    return moving_averages

# Test case
def test_calculate_moving_average():
    data = [1, 2, 3, 4, 5]
    window = 2
    expected_result = [1.5, 2.5, 3.5, 4.5]
    result = calculate_moving_average(data, window)
    assert result == expected_result, f'Expected {expected_result}, but got {result}'

test_calculate_moving_average()
```
This code defines a function that calculates the moving average in a list of float numbers and validates the input parameters. Also, a test case is added.