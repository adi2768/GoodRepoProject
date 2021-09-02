def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sum1 = 0

    if x > 0:
        n = len(str(x))
        for i in range(n):
            rem = x % 10
            x = x // 10
            sum1 = (sum1 * 10) + rem
        return sum1

    elif x < 0:
        x = x * -1
        n = len(str(x))
        for i in range(0, n):
            rem = x % 10
            x = x // 10
            sum1 = (sum1 * 10) + rem
        return sum1 * -1

    else:
        return x


if __name__ == '__main__':

    num = int(input("Enter a number:"))
    rev_num = reverse(num)
    print(rev_num)