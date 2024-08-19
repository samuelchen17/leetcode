# Catalan Number
def BracketCombinations(num):
    n = num

    def Fact(n):
        if n == 0:
            return 1
        else:
            return n * Fact(n - 1)

    return int(Fact(2 * n) / (Fact(n + 1) * Fact(n)))


# keep this function call here
print(BracketCombinations(input()))
