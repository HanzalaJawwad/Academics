function fibonacci(n)
if n == 0
return 0
elseif n == 1
return 1
else
return fibonacci(n - 1) + fibonacci(n - 2)
end
end
function generate_fibonacci_series(n)
series = [fibonacci(i) for i in 0:n]
return series
end
n = 10
series = generate_fibonacci_series(n)
println("Fibonacci series of length $(n+1):")
println(series)