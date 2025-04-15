Certainly, here is a Python function that calculates the moving average of a given list of float with some validations and a test:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    # Input validation
    if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
        raise TypeError("Data should be a list of integers or floats")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("Window should be a positive integer")
    if window > len(data):
        raise ValueError("Window size is larger than data size")

    # Calculate moving average
    moving_averages = []
    for i in range(window, len(data)+1):
        this_window = data[i-window:i]
        window_average = sum(this_window) / window
        moving_averages.append(window_average)

    return moving_averages


# Test case
def test_calculate_moving_average():
    data = [2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
    window = 3
    result = calculate_moving_average(data, window)
    expected_result = [3.5, 4.5, 5.5, 6.5]
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

test_calculate_moving_average()
```

This function takes as parameters a list of floats (`data`) and an integer (`window`), and returns a list of floats containing the moving averages. It checks that `data` is a list of integers or floats and `st_window` is a positive integer. Also, it throws a `ValueError` if the window size is larger than the size of the data. The test function `test_calculate_moving_average()` checks the functionality with a case. Use a test library like `pytest` to run this test function.