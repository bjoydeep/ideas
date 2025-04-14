Sure, here's the Python code:

```python
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    # Input validation
    if not isinstance(data, list) or not all(isinstance(i, float) for i in data):
        raise ValueError("Input data must be a list of floats.")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("Window size must be a positive integer.")
    if window > len(data):
        raise ValueError("Window size must be less than or equal to the data size.")
    
    moving_averages = []
    for i in range(len(data) - window + 1):
        this_window = data[i : i + window]
        window_average = sum(this_window) / window
        moving_averages.append(window_average)
    return moving_averages

# Test
def test_calculate_moving_average():
    data = [2.0, 4.0, 6.0, 8.0, 10.0]
    window = 3
    expected_output = [4.0, 6.0, 8.0]
    assert calculate_moving_average(data, window) == expected_output

    # Add more tests as necessary

# Run the test
test_calculate_moving_average()
```

In this solution: 
- We first validate the input arguments to be sure they are in the correct form and within acceptable limits.
- We calculate the moving average for each window of the input data. This is done by iterating through the data, creating a window for each iteration, calculating the average of the window, and appending it to the list of moving averages.
- We also include a simple test function that applies the `calculate_moving_average` function to a small data set and compares the output to the expected result.