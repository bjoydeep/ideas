Sure, here is a Python function that calculates the moving average:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    """Function to calculate the moving average."""
    
    # Input validation 
    if not isinstance(data, list) or not all(isinstance(i, float) for i in data):
        raise ValueError("data should be a list of floats")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("window should be a positive integer")
        
    if len(data) < window:
        raise ValueError("window size should be less than or equal to data size")

    result = []
    for i in range(len(data) - window + 1):
        result.append(sum(data[i: i + window]) / window)
    return result

def test_calculate_moving_average():
    data = [2.5, 5.0, 7.5, 10.0, 12.5, 15.0]
    window = 3

    assert calculate_moving_average(data, window) == [5.0, 7.5, 10.0, 12.5]

test_calculate_moving_average()
```
The main function `calculate_moving_average(data: List[float], window: int) -> List[float]` calculates the moving average of the data over the window size specified. If there's anything wrong with the input arguments, it will raise a ValueError. 

The function `test_calculate_moving_average()` is a simple test that checks if the function works correctly on a predefined dataset. In this case the dataset is data = [2.5, 5.0, 7.5, 10.0, 12.5, 15.0] and window size is 3.
This test will raise an AssertionError if the calculated moving average doesn't match the expected value.