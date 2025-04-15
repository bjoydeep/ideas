Below is the Python code.

```python
# Import required libraries
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("Input data should be a list of integers or floats.")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("Window size should be a positive integer.")
    if len(data) < window:
        raise ValueError("Window size should be less than or equal to the length of data.")

    return [sum(data[i - window:i]) / window for i in range(window, len(data) + 1)]

# Test case
def test_calculate_moving_average():
    data = [1.5, 2.5, 3.5, 4.5, 5.5]
    window = 3
    result = calculate_moving_average(data, window)
    print("Test case - calculate_moving_average: {}".format('Pass' if result == [2.5, 3.5, 4.5] else 'Fail'))

# Run test
test_calculate_moving_average()
```
This will calculate the moving average for a provided list of data over the specified window size. Basic input validation is performed to ensure the data is a list of integers or floats, the window size is a positive integer, and that the window size is less than or equal to the length of the list of data.