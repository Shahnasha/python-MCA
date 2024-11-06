def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series
n = int(input("Enter the number of terms in the Fibonacci series: "))
result = fibonacci_series(n)
print("Fibonacci series:", result)
