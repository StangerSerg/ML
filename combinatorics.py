
def recursive_subfact(num: int) -> int:
    """
    Compute the subfactorial (derangement number) using canonical recursion.

    The subfactorial !n represents the number of permutations of n elements
    where no element appears in its original position (derangements).

    This implementation follows the pure mathematical recurrence relation:
        !n = (n - 1) * (!(n-1) + !(n-2))
    with base cases !0 = 1 and !1 = 0.

    Args:
        num: Non-negative integer for which to compute the subfactorial.
    Returns:
        The subfactorial !n as an integer.
        
    Warning:
        This function has exponential time complexity O(2^n) and is provided
        primarily for educational purposes to demonstrate the canonical definition.
        For practical use, prefer `subfact()` which runs in O(n) time.
    """
    match num:
        case 0:
            return 1
        case 1:
            return 0
        case _:
            res = (num - 1) * (recursive_subfact(num - 1) + recursive_subfact(num - 2))
            return res


def subfact(num: int) -> int:
    """
    Compute the subfactorial (derangement number) using iterative dynamic programming.

    The subfactorial !n represents the number of derangements — permutations of
    n elements where no element remains in its original position.

    This implementation uses bottom-up dynamic programming with O(n) time
    complexity and O(1) auxiliary space, making it suitable for production use
    even with moderately large inputs.

    The recurrence relation used is:
        !n = (n - 1) * (!(n-1) + !(n-2))
    with base cases !0 = 1 and !1 = 0.

    Args:
        num: Non-negative integer for which to compute the subfactorial.

    Returns:
        The subfactorial !n as an integer.
    """
    match num:
        case 0:
            return 1
        case 1:
            return 0
        case _:
          prev2, prev1 = 1, 0
          for i in range(2, num + 1):
              curr = (i - 1) * (prev1 + prev2)
              prev2, prev1 = prev1, curr
            
          return prev1


def factorial(num: int) -> int:
    """
    Compute the factorial of a non-negative integer iteratively.
    
    The factorial n! is the product of all positive integers less than
    or equal to n. By convention, 0! = 1.
    
    This implementation uses a simple while loop with O(n) time complexity
    and O(1) auxiliary space.
    
    Args:
        num: Non-negative integer for which to compute the factorial.
    
    Returns:
        The factorial n! as an integer.
    """
    res = 1
    i = num
    while i > 1:
      res *= i
      i -= 1
    
    return res


def euler(precision: int) -> float:
    """
    Approximate Euler's number (e) using the relationship with subfactorials.
  
    This function leverages the remarkable mathematical identity:
        e ≈ n! / !n
  
    The approximation arises from the closed-form expression for subfactorials:
        !n = round(n! / e)
    which implies that for sufficiently large n, n! / !n converges to e.
  
    Args:
        precision: Positive integer controlling the accuracy of the approximation.
                   Higher values yield better precision. Recommended: n >= 10.
                   But if you'd like to see Lev Tolstoy twice use n >= 13
                   (Why Tolstoy? Because 1828 — his birth year — appears twice
                   consecutively in the decimal expansion of e:
                   e ≈ 2.718281828...)
  
    Returns:
        An approximation of Euler's number e as a float.
    """
    return factorial(precision) / subfact(precision)
