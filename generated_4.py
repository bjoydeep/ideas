Sure, here is a Python function that accomplishes just that:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
        raise ValueError('Data should be a list of floats or integers.')
    if not isinstance(window, int) or window <= 0:
        raise ValueError('Window size should be a positive integer.')
    if window > len(data):
        raise ValueError('Window size should not be larger than the size of the data.')
    
    moving_averages = []
    for i in range(len(data) - window + 1):
        average = sum(data[i:i + window]) / window
        moving_averages.append(average)
        
    return moving_averages


def test_calculate_moving_average():
    data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    window = 3
    expected_output = [2.0, 3.0, 4.0, 5.0]
    assert calculate_moving_average(data, window) == expected_output
    print('Test passed.')

test_calculate_moving_average()
```

This code starts with some necessary input validation, then calculates the moving averages within the specified window size. After the function is defined, a test is run to make sure it works as intended.

Just make sure to run the `test_calculate_moving_average()` each time you want to test your function. It's currently testing a case with raw decimal values, but you can customize it to match your specific use case.