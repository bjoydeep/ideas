```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    """
    Returns the moving average of a list of data.

    Parameters:
    data (List[float]): The input data to calculate the moving average for.
    window (int): The window for the moving average.

    Returns:
    List[float]: The moving average data.
    """
    # Validate inputs
    if not all(isinstance(item, (int, float)) for item in data):
        raise ValueError("Data contains non-numerical values.")

    if not isinstance(window, int) or window <= 0:
        raise ValueError("Window must be a positive integer.")

    if window > len(data):
        raise ValueError("Window size cannot be larger than data size.")

    # Create moving average
    moving_averages = []
    for i in range(len(data) - window + 1):
        this_window = data[i : i + window]
        window_avg = sum(this_window) / window
        moving_averages.append(window_avg)

    return moving_averages

# Simple test
def test_calculate_moving_average():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    window = 3
    expected_output = [2.0, 3.0, 4.0]
    assert calculate_moving_average(data, window) == expected_output, f'Test failed: {calculate_moving_average(data, window)} != {expected_output}'
    print('Test passed!')

# Run test
test_calculate_moving_average()
```