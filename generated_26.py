Sure, here is the Python code meeting the described requirements:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    """
    Calculate moving average given a data list and window period.
    """
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Data must be list of integers or floats")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("Window must be a positive integer")

    moving_average = []
    
    for i in range(len(data) - window + 1):
        average = sum(data[i: i + window]) / window
        moving_average.append(average)
    
    return moving_average


def test_calculate_moving_average():
    """
    Run a simple test for 'calculate_moving_average' function.
    """
    data = [2.0, 3.0, 4.0, 5.0, 6.0]
    window = 3
    expected_result = [3.0, 4.0, 5.0]
    
    result = calculate_moving_average(data, window)
    
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


# Run test
test_calculate_moving_average()
```

In this code, `calculate_moving_average()` function receives a list of float numbers (`data`) and a positive integer (`window`), and returns the moving average in a list format. If the input validation fails, the function raises a `ValueError`.

The function was tested with a simple test case within `test_calculate_moving_average()`.