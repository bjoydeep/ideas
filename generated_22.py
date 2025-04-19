Sure, here you go:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    if not isinstance(data, list) or not all(isinstance(item, (int, float)) for item in data):
        raise ValueError("Data must be a list of integers or floats")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("Window must be a positive integer")
    if window > len(data):
        raise ValueError("Window size must be less than or equal to the length of the data list")

    moving_avg = []
    for i in range(len(data) - window + 1):
        moving_avg.append(sum(data[i : i + window]) / window)
    return moving_avg

def test_calculate_moving_average():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    window = 2
    result = calculate_moving_average(data, window)
    assert result == [1.5, 2.5, 3.5, 4.5], f'Expected [1.5, 2.5, 3.5, 4.5], but got {result}'
    print('Test passed.')

test_calculate_moving_average()
```
This follows best Python practices and includes basic input validation checking for data type of the passed values. The function `calculate_moving_average` calculates the simple moving average for a given data list and window. A test case `test_calculate_moving_average` is also provided.