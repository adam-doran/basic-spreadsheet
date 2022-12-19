# Simple Spreadsheet   
Basic spreadsheet implementation to satisfy assessment requirements

Supports insert and get operations on cells, as well as basic arithmetic operations and cell references.

Behaviour is to raise an error on any attempt to create cyclic formula references as 
opposed to filling the cell with an error code and having to handle that throughout.

## Improvements:
For complex formulas with many shared references, observer updates are inefficient.

Eg: for the following sheet:
    
     ("A2", "=A1+2"), ("A3", "A1+A2"), ("A4","=A1+A2+A3")

An update to the value in A1 would cause A4 to be calculated 3 times. Topological sorting
of observer updates and a cache of calculated cells could eliminate this problem at cost of additional complexity

## Formula

Formula parsing is overly simplistic as anything more complicated deemed outside scope of assignment.
- Input validation required for anything passed to eval()
- Only supports setting of integers in cells & formulas
    - Floats only supported as result of formula evaluation