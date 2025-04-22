Here is the Python code to implement your requirements:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    if not isinstance(data, list):
        raise ValueError("The data parameter should be a list")
    if not all([isinstance(i, (int, float)) for i in data]):
        raise ValueError("The data list should contain only int and/or float")
    if not isinstance(window, int):
        raise ValueError("The window parameter should be an int")
    if window < 1:
        raise ValueError("The window value should be 1 or more")
    return [sum(data[i - window:i]) / window for i in range(window, len(data) + 1)]

# Test
data = [2.0, 4.0, 6.0, 8.0, 10.0, 12.0]
window = 3
assert calculate_moving_average(data, window) == [4.0, 6.0, 8.0, 10.0], "Test failed!"
```
In this script, first we have implemented the function `calculate_moving_average` which calculates the moving average of supplied data. The function validates the input for the correct data types and value restrictions. After that, we have a test case where it calculates the moving average of a list with a window of 3. We assert the result with the expected output to make sure function works as expected. If the function doesn't work as expected, it will raise an `AssertionError` with the message "Test failed!"