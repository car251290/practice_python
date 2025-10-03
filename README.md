# practice_python
🔹 Example 1 – Importing a built-in module

Python comes with many modules that you can use right away.

import math

print(math.sqrt(25))  # This uses the sqrt (square root) function from the math module


✅ Explanation:

import math → brings all the tools from the math module.

math.sqrt(25) → uses the square root function inside that module.

🔹 Example 2 – Importing just one part of a module

If you only need one thing, you can import just that part.

from math import pi

print(pi)  # Prints 3.141592653589793

✅ Explanation:

from math import pi means “bring only pi from math.”

🔹 Example 3 – Importing your own file

If you made another Python file called greetings.py:

def say_hello():
    print("Hello from greetings.py!")


Then in another file:

import greetings

greetings.say_hello()


✅ This lets you reuse your own code in different programs.
# Python function 
 <img style=width:15%;height:15%  src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png">
