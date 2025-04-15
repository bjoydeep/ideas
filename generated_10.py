Here's the code based on the Github issue:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    """
    Calculate the moving average.
    :param data: list of float numbers
    :param window: int 
    :return: list of float numbers representing the moving average
    """
    # input validation
    if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
        raise TypeError("Data must be a list of integers or floats.")
    if not isinstance(window, int):
        raise TypeError("Window must be an integer.")

    # moving average calculation
    return [sum(data[i - window:i]) / window for i in range(window, len(data) + 1)]

# tests
def test_calculate_moving_average():
    assert calculate_moving_average([1, 2, 3, 4, 5], 2) == [1.5, 2.5, 3.5, 4.5]
    assert calculate_moving_average([10, 20, 30, 40, 50], 3) == [20.0, 30.0, 40.0]
    try:
        calculate_moving_average(["a", "b", "c"], 3)  # should raise TypeError
    except TypeError as e:
        assert str(e) == "Data must be a list of integers or floats."
    try:
        calculate_moving_average([1, 2, 3], "a")  # should raise TypeError
    except TypeError as e:
        assert str(e) == "Window must be an integer."
        
test_calculate_moving_average()
```
This script has a `calculate_moving_average()` function that calculates the moving average from a list of numbers given a window of a specified size. The function has input validation for the types of both parameters. The script also includes a `test_calculate_moving_average()` function to test `calculate_moving_average()`.