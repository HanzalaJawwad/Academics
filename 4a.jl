function gcd(a, b)
while b != 0
a, b = b, a % b
end
return abs(a)
end
function lcm(a, b)
return a * b / gcd(a, b)
end
function main()
a = 56
b = 98
println("GCD of $(a) and $(b) is: ", gcd(a, b))
println("LCM of $(a) and $(b) is: ", lcm(a, b))
end
main()
