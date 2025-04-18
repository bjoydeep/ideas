Sure, I will create the `calculate_moving_average` function as per the instructions. Here is the Python code.

```python
from typing import List
import unittest

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    """Calculates the moving average of a list based on the window size.

    Args:
        data (List[float]): The list of floats for which the moving average is to be calculated.
        window (int): The window size for moving average.

    Returns:
        List[float]: The list of moving averages.

    Raises:
        ValueError: If the window size is not a positive integer or is greater than the size of data.
    """

    # input validation
    if not isinstance(window, int) or window <= 0:
        raise ValueError("Window size should be a positive integer.")
    
    if window > len(data):
        raise ValueError("Window size should not be greater than the size of data.")

    moving_averages = []
    
    for i in range(len(data) - window + 1):
        avg = sum(data[i:i+window]) / window
        moving_averages.append(avg)

    return moving_averages

class TestCalculateMovingAverage(unittest.TestCase):
    def test_calculate_moving_average(self):
        data = [2.5, 5.0, 7.5, 10.0, 12.5, 15.0]
        window = 3
        self.assertEqual(calculate_moving_average(data, window), [5.0, 7.5, 10.0, 12.5])

if __name__ == "__main__":
    unittest.main()
```

The `calculate_moving_average` function takes a list of floats `data` and an integer `window`. It validates the inputs first. If the inputs are invalid, it raises an `ValueError`.

Then, it calculates the moving average with the help of a sliding window of size `window`. The moving average for each window is calculated by taking the sum of values in the window and dividing it by the window size.

The function finally returns the list of moving averages.

The test case `test_calculate_moving_average` in `TestCalculateMovingAverage` class tests the function with a specific scenario. It verifies if the returned moving averages from the function match the expected list of moving averages. If they match, the test passes, otherwise it fails.