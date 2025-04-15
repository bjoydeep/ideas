Here is the code that fulfills all the requirements mentioned in the GitHub issue.

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    # input validation
    if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("data should be a list of numbers")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("window should be a positive integer")

    # calculate moving average
    return [sum(data[i: i + window]) / window for i in range(len(data) - window + 1)]

# test case
def test_calculate_moving_average():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    window = 3
    expected_output = [2.0, 3.0, 4.0]
    assert calculate_moving_average(data, window) == expected_output

test_calculate_moving_average()
```

This code defines a function that calculates a moving average of a list of floats. It checks if the inputs are valid. If the inputs are not valid, it raises a ValueError with an appropriate message. It also includes a simple test case to verify that the function works as expected.
