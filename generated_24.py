Sure, here is a Python implementation fulfilling the requirements:

```python
from typing import List, Union

def calculate_moving_average(data: List[Union[int, float]], window: int) -> List[float]:
    """ Calculate moving average

    Args:
        data:   Input data to calculate moving avearge.
        window: the window size for moving average calculation.
        
    Returns:
        A list of moving averages
    """
    # Input validation
    if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
        raise ValueError('Data should be a list of numbers.')
    if not isinstance(window, int) or window <= 0:
        raise ValueError('Window size must be a positive integer.')
    if window > len(data):
        raise ValueError('Window size should not exceed the length of the data list.')
    
    moving_averages = []
    for i in range(len(data) - window + 1):
        this_window = data[i : i + window]
        window_average = sum(this_window) / window
        moving_averages.append(window_average)
        
    return moving_averages


# Test the function
def test_calculate_moving_average():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    window = 3
    
    result = calculate_moving_average(data, window)
    expected_result = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
    
    assert result == expected_result, f'Expected {expected_result}, but got {result}'
    print('Test passed.')
    
test_calculate_moving_average()
```
This code defines a function to calculate moving averages, validates the inputs, and then runs a simple test with a known input and output. If the test passes, it prints "Test passed." If the test fails, it will raise an assertion error explaining the issue.