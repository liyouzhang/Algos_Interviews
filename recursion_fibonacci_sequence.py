"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions.

function getFib(position) {
  if (position == 0) { return 0; }
  if (position == 1) { return 1; }
  var first = 0,
      second = 1,
      next = first + second;
  for (var i = 2; i < position; i++) {
    first = second;
    second = next;
    next = first + second;
  }
  return next;
}

"""

# 20200427 LZ answer
# Yay!!!! The first function I wrote right :)))

def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1 
    else:
        output = get_fib(position -1)
        output2 = get_fib (position-2)
        return output + output2 
    return -1

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)

'''
more notes from course:
https://classroom.udacity.com/courses/ud513/lessons/7123524086/concepts/78810568040923


You may have noticed that this solution will compute the values of some inputs more than once. For example get_fib(4) calls get_fib(3) and get_fib(2), get_fib(3) calls get_fib(2) and get_fib(1) etc. The number of recursive calls grows exponentially with n.

In practice if we were to use recursion to solve this problem we should use a hash table to store and fetch previously calculated results. This will increase the space needed but will drastically improve the runtime efficiency.
'''