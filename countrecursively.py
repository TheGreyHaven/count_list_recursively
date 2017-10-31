"""Count items in a list recursively.

For example:

        >>> count_recursively([])
        0

        >>> count_recursively([1, 2, 3])
        3

"""


def count_recursively(lst):
    """Return number of items in a list, using recursion."""
    def count_using_recursion(count, lst):
		# print count
		if lst == []:
			return count
		else:
			# print lst
			lst = lst[1:]
			return count_using_recursion(count + 1, lst)


    return count_using_recursion(0, lst)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO YOU!\n"


