Here is a Python function to calculate moving average based on the information provided with a simple test included.

First, import the necessary libraries.

```python
from typing import List

# unit test requirements 
import unittest
```

Now, let's create the function:

```python
def calculate_moving_average(data: List[float], window: int) -> List[float]:
    
    if not data or window <= 0:
        raise ValueError("Data list must not be empty and window must be a positive number.")
    
    if window > len(data):
        raise ValueError("Window length cannot exceed data length.")
    
    data = [float(i) for i in data]

    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
        
    return averages
```
Next, let's create a simple unit test:

```python
class TestMovingAverageCalculator(unittest.TestCase):
    def test_calculate_moving_average(self):
        self.assertEqual(calculate_moving_average([4.0, 5.0, 5.0, 3.0], 2), [4.5, 5.0, 4.0])
```
The test function `test_calculate_moving_average` in the test case `TestMovingAverageCalculator` is testing the `calculate_moving_average` function with a simple use case.

Finally, add the following lines to the end of your Python file to run the tests when the script is executed:

```python
if __name__ == "__main__":
    unittest.main()
```

The entire code in one block will look like this:

```python
from typing import List

import unittest

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    
    if not data or window <= 0:
        raise ValueError("Data list must not be empty and window must be a positive number.")
    
    if window > len(data):
        raise ValueError("Window length cannot exceed data length.")
    
    data = [float(i) for i in data]

    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
        
    return averages

class TestMovingAverageCalculator(unittest.TestCase):
    def test_calculate_moving_average(self):
        self.assertEqual(calculate_moving_average([4.0, 5.0, 5.0, 3.0], 2), [4.5, 5.0, 4.0])

if __name__ == "__main__":
    unittest.main()
```