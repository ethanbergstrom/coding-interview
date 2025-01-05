## Problem 1:

You are tasked with implementing a script that assesses system state to determine whether upgrading a software package is necessary, and whether to issue a restart.

The algorithm to determine whether an upgrade is necessary is already provided (see `sample.py`). Your job is to define the function signature, inputs, and outputs, and explain your design decisions.


### Requirements:

1. The script assesses system state by comparing the presence and version of two related software packages (Microsoft .NET Framework and Nuance Dragon Medical One), speced in this problem with simple JSON files.
    * If the version of `.NET Framework` is less than `4.5` **and** the version of `Nuance Dragon Medical One` is greater than `2020.1`, an upgrade to the latest version of .NET is necessary.
    * If `Nuance Dragon Medical One` is version `2020.1` or higher and `.NET Framework` is installed but below version `4.5`, `.NET Framework` must be upgraded 
2. The script assesses whether a restart action is required based on whether an upgrade is necessary.
    * By default, if an upgrade is considered necessary (see previous requirement), a restart is also deemed necessary.
3. The script operator has discretion to overrule the script's default determination of both the upgrade and restart actions.
    * The operator requires the ability to pass an argument that **forces** an upgrade response, regardless of the script's default determination
    * The operator requires the ability to pass an argument that **prevents** an automatic restart, regardless of the script's default determination
4. Specific upgrade and restart implementations are **out of scope** for this script - it should simply print a JSON response (see example output below) indicating whether an upgrade and/or restart is necessary.

### Your task:

1. Design and implement the function inputs and default behavior
2. Reason about edge cases: What are some potential edge cases that your solution should handle?
3. Explain the approach: Why did you choose the function signature and handle the data this way?

### Example Output
```python
{
    "title": ".NET Framework Upgrade",
    "upgrade": true,
    "restart": false
}
```
