Certainly, here is Python code considering the details from the GitHub issue:

```python
from typing import List
import statistics

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    """
    Function to calculate moving average of a list of floats
    :param data: List of floats
    :param window: Integer indicating the moving average window
    :return: List of moving averages
    """
    # input validation
    if not isinstance(data, list) or not all(isinstance(i, float) for i in data):
        raise ValueError("Data must be a list of float values")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("Window must be a positive integer")

    # calculate moving averages
    moving_averages = []
    for i in range(len(data) - window + 1):
        moving_averages.append(statistics.mean(data[i:i+window]))
        
    return moving_averages


# test
def test_calculate_moving_average():
    data = [2.0, 4.0, 6.0, 8.0, 10.0]
    window = 3
    print("\nTest case: Calculate moving average")
    print(f"Data: {data}")
    print(f"Window: {window}")
    output = calculate_moving_average(data, window)
    print(f"Output: {output}")
    assert output == [4.0, 6.0, 8.0], "Test case failed"

# Run the test function
test_calculate_moving_average()
```
This script creates a moving average function that takes a list of float values and a window size (in integer) as inputs. It validates the inputs, calculates, and returns the moving averages as per the window size.

Additionally, a test function `test_calculate_moving_average()` is created to test the main function. The test function will raise an `AssertionError` if the function's output does not match the expected output for given test case data.