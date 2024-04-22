def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)

    return fib_series

n_terms = int(input("Enter the number of terms in the Fibonacci series: "))

if n_terms <= 0:
    print("Please enter a positive integer.")
else:
    fib_series = fibonacci(n_terms)
    print("Fibonacci series up to {} terms:".format(n_terms), fib_series)