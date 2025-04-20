Here's a Python code that follows the constraints and the requirements of your GitHub issue.

```python
from typing import List


def calculate_moving_average(data: List[float], window: int) -> List[float]:
    # input validation
    if not isinstance(window, int) or window <= 0:
        raise ValueError("window size should be a positive integer")
    if not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("data contains non-numeric values")
    if len(data) < window:
        raise ValueError("data length is less than window size")
    
    # calculate moving average
    result = []
    for i in range(len(data) - window + 1):
        result.append(sum(data[i: i + window]) / window)
    return result


# simple test
def test_calculate_moving_average():
    data = [3.0, 5.0, 7.0, 2.0, 8.0, 10.0, 11.0, 65.0, 72.0, 81.0, 99.0, 100.0, 150.0]
    window = 3
    expected_result = [5.0, 4.666666666666667, 5.666666666666667, 6.666666666666667, 9.666666666666666, 28.666666666666668, 49.333333333333336, 72.66666666666667, 84.0, 93.33333333333333, 116.33333333333333]
    assert calculate_moving_average(data, window) == expected_result


if __name__ == "__main__":
    test_calculate_moving_average()
```

The `calculate_moving_average` function does not require non-standard libraries as per the constraints. We are using a simple sliding window approach to calculate the moving average. 

The test function `test_calculate_moving_average` is designed to validate the moving average function using an example case. It checks whether the output of `calculate_moving_average` function is as expected.

Remember to run the test case to make sure our implementation is correct.