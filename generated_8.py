Here is the Python code according to your GitHub issue:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    # Basic input validation
    if not all(isinstance(i, float) for i in data):
        raise ValueError("All data items must be of float type.")

    if not isinstance(window, int):
        raise ValueError("Window must be an integer.")

    if window <= 0:
        raise ValueError("Window size must be a positive integer.")

    if window > len(data):
        raise ValueError("Window size must not be greater than the length of the data.")

    # Moving average calculation
    moving_averages = []
    for i in range(len(data) - window + 1):
        this_window = data[i : i + window]
        window_average = sum(this_window) / window
        moving_averages.append(window_average)

    return moving_averages

# Testing
def test_calculate_moving_average():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    window = 3
    output = calculate_moving_average(data,window)

    assert output == [2.0, 3.0, 4.0], f"For {data} with window {window}, expected [2.0, 3.0, 4.0] but got {output}"

test_calculate_moving_average()
```

This code defines a function `calculate_moving_average` that takes in a list of floats and a integer representing the window and returns the moving average list. We then define a test function `test_calculate_moving_average()`, where we test the function `calculate_moving_average()` with a standard test case.