Here is a solution.

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    """
    Calculate the moving average of a list with a given window
    :param data: List of floats
    :param window: Size of moving average window
    :return: List of moving averages
    """
    # Basic Input validations: window size must be positive, and less than or equal to the length of the data
    if not isinstance(window, int) or window <= 0:
        raise ValueError("Window size must be a positive integer")

    if len(data) < window:
        raise ValueError("Window size must be less than or equal to the length of the data")

    return [sum(data[i - window:i]) / window for i in range(window, len(data) + 1)]
     
# Simple Test
def test_calculate_moving_average():
    data = [2.0, 2.0, 2.0, 2.0, 2.0]
    window = 3 
    assert calculate_moving_average(data, window) == [2.0, 2.0, 2.0]

    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    window = 2
    assert calculate_moving_average(data, window) == [1.5, 2.5, 3.5, 4.5]

test_calculate_moving_average()
```

This function `calculate_moving_average` computes the moving average of the data for a specified window. It checks that the window size is a positive integer and not larger than the data length. It raises ValueError if the input is not valid. After input validation, the function applies the moving average on the data.

The helper function `test_calculate_moving_average` is provided for testing purposes. It tests the `calculate_moving_average` function with two different inputs.