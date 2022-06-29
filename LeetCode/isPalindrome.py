def isPalindrome(x):
    x = str(x)
    n = len(x)
    for i in range(n):
        if x[i] != x[n-i-1]:
            return False
    return True


if __name__ == '__main__':
    print(isPalindrome(12321))