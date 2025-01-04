### Problem:

# Convergence / Reconciliation
# Connection
# Inference from context
# Minimal yet flexible API / Intelligent defaults

Operating system state
Files
Reads in 
Multiple branching paths based on context from user or machine 
Consistent output

You are tasked with designing a system that parses and compares the contents of two files, and manipulates a third file based on their state and additional context

file1 = 'blah.json'
file2 = 'blah2.json'
preference = file2.contains('preference') which we can guess because file2 

It's unlikely, but not impossible, that the operator wants the preference off when we guess that its on.
Need a plausible explaination for this (customer preference / passivity)

if file1.contains('something') and file2.contains('somethingElse') 

multiple operations / decision points with multiple parameters

return JSON structure based on multiple decisions

property1A = file1.property.A
property1C = file1.property.C
property2A = file2.property.A
property2F = file2.property.F
clientPref = file2.property.H but can be overridden

if property1A and property2A in ()
    if property2F > 23.1
        # False
    elseif property1C == property2F
        # Property1C is also <= 23.1
        UpgradePref
    else
        # Property2F <= 23.1
        # Property1C != 23.1
        True
else
    False

if property1A and property2A if property2F > 23.1 else ( UpgradePref if property1C == property2F else (  ) )


data.val1 = 'someStaticVal'
data.val2 = False if property1A and property2A if property2F > 23.1 else True 
data.val3 = # Value required from operator
data.val4 = # Probably 'defaultValue' but changed at operator discretion 

return data

You are tasked with implementing a system that processes a list of transactions and returns the total amount of money spent on each day. A transaction consists of an amount, a timestamp, and an optional note.

The algorithm to calculate the total amount spent per day is already provided. Your job is to define the function signature, inputs, and outputs, and explain your design decisions.

```python
from collections import defaultdict
from datetime import datetime

def calculate_daily_spending(transactions):
    daily_spending = defaultdict(float)
    
    for transaction in transactions:
        timestamp = datetime.fromtimestamp(transaction['timestamp'])
        date_str = timestamp.strftime('%Y-%m-%d')
        daily_spending[date_str] += transaction['amount']
    
    return daily_spending

```

### Requirements:

1. Each transaction has a timestamp (in Unix epoch format), a numeric amount, and an optional note string.
2. The output should be a dictionary where:
   * The key is the date (in the format 'YYYY-MM-DD').
   * The value is the total amount spent on that date.
3. Your function should gracefully handle invalid or missing data. For example, if a transaction does not have a valid timestamp or amount, the function should ignore that transaction.
4. The transactions can be sorted by timestamp, but your solution should not assume this.
5. The system should be able to handle an arbitrary number of transactions efficiently.

### Your task:

1. Design the function signature: Define the inputs and output of the function.
2. Reason about edge cases: What are some potential edge cases that your solution should handle?
3. Explain the approach: Why did you choose the function signature and handle the data this way?

### Example

#### Input:
```python
transactions = [
    {'timestamp': 1640995200, 'amount': 100.50, 'note': 'Groceries'},
    {'timestamp': 1641081600, 'amount': 50.75, 'note': 'Dining'},
    {'timestamp': 1640995200, 'amount': 25.00, 'note': 'Transport'},
]
```

#### Output:
```python
{
    '2022-01-01': 125.50,
    '2022-01-02': 50.75
}
```

This problem assesses the candidate's ability to:

* Design an effective and clear API.
* Handle real-world concerns like invalid data, edge cases, and efficiency.
* Reason about how to organize and return the data in a meaningful way.