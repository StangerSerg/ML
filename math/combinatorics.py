
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
            
    Raises:
        ValueError: If num is negative.
        TypeError: If num is not an integer.
    
    Examples:
        >>> subfact(0)
        1
        >>> subfact(1)
        0
        >>> subfact(2)
        1
        >>> subfact(3)
        2
        >>> subfact(4)
        9
        >>> subfact(5)
        44
    """
    # Валидация
    if not isinstance(num, int):
        raise TypeError(f"Expected integer, got {type(num).__name__}")
    
    if num < 0:
        raise ValueError(f"Subfactorial is not defined for negative numbers: {num}")
        
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
    
    Raises:
        ValueError: If num is negative.
        TypeError: If num is not an integer.
    
    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(1)
        1
    """
    # Валидация типа
    if not isinstance(num, int):
        raise TypeError(f"Expected integer, got {type(num).__name__}")
    
    # Валидация значения
    if num < 0:
        raise ValueError(f"Factorial is not defined for negative numbers: {num}")
        
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


def permutation(
    num: int, 
    linked: int = 0, 
    together: bool = True
) -> int:
    """
    Calculate permutations of n elements with optional grouping constraints.
    
    This function handles three scenarios:
    1. When 'linked' = 0: No constraints, simply calculate all permutations
       (equivalent to factorial(num))
    2. When 'together' is True: Treat 'linked' specific elements as a single block
       (calculates permutations where these elements must stay together)    
    3. When 'together' is False: Calculate permutations where 'linked' specific
       elements are NOT allowed to be together
    
    Args:
        num: Total number of elements (n).
        linked: Number of specific elements to treat as a group or exclude.
               Must be between 0 and num inclusive.
        together: 
            - True (default): Calculate permutations where 'linked' elements are grouped together
            - False: Calculate permutations where 'linked' elements are NOT together
    
    Returns:
        Number of valid permutations as integer.
    
    Raises:
        ValueError: If validation fails (invalid num/linked values or missing together flag).
        TypeError: If arguments have incorrect types.
    
    Examples:
        # Group 2 specific elements together out of 5 total
        >>> permutation(5, 2, together=True)
        48  # (5-2+1)! * 2! = 4! * 2! = 24 * 2 = 48
        
        # Count permutations where 2 specific elements are NOT together
        >>> permutation(5, 2, together=False)
        72  # 5! - 48 = 120 - 48 = 72
        
        # Edge cases
        >>> permutation(3, 0)
        6    # 3! = 6
        >>> permutation(3, 1, together=True)
        6    # (3-1+1)! * 1! = 3! * 1 = 6 (single element as a block)
        >>> permutation(3, 1, together=False)
        0    # 3! - 6 = 0 (single element cannot be "not together" with itself)
        >>> permutation(3, 3, together=True)
        6    # (3-3+1)! * 3! = 1! * 6 = 6 (all elements as one block)
        >>> permutation(3, 3, together=False)
        0    # 3! - 6 = 0 (all elements together always)
    """   
    # Валидация типа num
    if not isinstance(num, int):
        raise TypeError(f"Expected integer for 'num', got {type(num).__name__}")
    
    # Валидация типа linked
    if not isinstance(linked, int):
        raise TypeError(f"Expected integer for 'linked', got {type(linked).__name__}")
    
    # Валидация типа together
    if not isinstance(together, bool):
        raise TypeError(f"Expected boolean for 'together', got {type(together).__name__}")
    
    # Валидация диапазонов
    if num < 0:
        raise ValueError(f"'num' cannot be negative, got {num}")
    
    if linked < 0:
        raise ValueError(f"'linked' cannot be negative, got {linked}")
    
    if linked > num:
        raise ValueError(f"'linked' ({linked}) cannot be greater than 'num' ({num})")

    res = factorial(num - linked + 1) * factorial(linked)
    
    if linked > 0 and not together:
        res = factorial(num) - res

    return res


def derangement(num: int) -> int:
    """
    Alias for subfactorial function.
    
    Computes the number of derangements of n elements — permutations where
    no element appears in its original position.
    
    Args:
        num: Non-negative integer for which to compute the number of derangements.
    
    Returns:
        The number of derangements !n as an integer.
    
    Raises:
        ValueError: If num is negative.
        TypeError: If num is not an integer.
    
    Examples:
        >>> derangement(3)
        2
        >>> derangement(4)
        9
        >>> derangement(5)
        44
    """
    return subfact(num)
    

def arrangement(power: int, num: int) -> int:
    """
    Calculate the number of arrangements (permutations) of n elements taken k at a time.
    
    Also known as partial permutations or k-permutations of n.
    The formula is: A(n, k) = n! / (n - k)!
    
    This represents the number of ways to choose and arrange k distinct elements
    from a set of n elements, where order matters.
    
    Args:
        power: Total number of elements available (n). Must be non-negative.
        num: Number of elements to arrange (k). Must satisfy 0 <= k <= n.
    
    Returns:
        Number of possible arrangements as an integer.
    
    Raises:
        ValueError: If validation fails (negative values or k > n).
        TypeError: If arguments are not integers.
        ZeroDivisionError: If power == num (handled by factorial(0) = 1).
    
    Examples:
        # Number of ways to arrange 2 elements from a set of 5
        >>> arrangement(5, 2)
        20  # 5! / 3! = 120 / 6 = 20
        
        # Arrange all 5 elements (regular permutation)
        >>> arrangement(5, 5)
        120  # 5! / 0! = 120 / 1 = 120
        
        # Arrange 0 elements (empty arrangement)
        >>> arrangement(5, 0)
        1    # 5! / 5! = 1
        
        # Edge cases
        >>> arrangement(3, 1)
        3    # 3! / 2! = 6 / 2 = 3
        >>> arrangement(0, 0)
        1    # 0! / 0! = 1
        
    Notes:
        - Also known as: falling factorial, P(n, k), nPk
        - Result is always an integer (factorials divide evenly)
        - For k > n, result is 0 (invalid selection)
        - For k = n, result equals factorial(n)
        - For k = 0, result is 1 (empty arrangement)
    """
    # Валидация типов
    if not isinstance(power, int):
        raise TypeError(f"Expected integer for 'power', got {type(power).__name__}")
    
    if not isinstance(num, int):
        raise TypeError(f"Expected integer for 'num', got {type(num).__name__}")
    
    # Валидация диапазонов
    if power < 0:
        raise ValueError(f"'power' cannot be negative, got {power}")
    
    if num < 0:
        raise ValueError(f"'num' cannot be negative, got {num}")
    
    if num > power:
        raise ValueError(f"'num' ({num}) cannot be greater than 'power' ({power})")
    
    # Вычисление размещений
    # Используем целочисленное деление, так как результат всегда целый
    return factorial(power) // factorial(power - num)
