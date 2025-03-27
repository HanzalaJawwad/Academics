function factorial(n)
if n == 0
return 1
else
return n * factorial(n - 1)
end
end
function main()
n = 5
println("Factorial of $(n) is: ", factorial(n))
end
main()