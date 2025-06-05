function add_complex(c1, c2)
return complex(c1.re + c2.re, c1.im + c2.im)
end
function subtract_complex(c1, c2)
return complex(c1.re - c2.re, c1.im - c2.im)
end
function multiply_complex(c1, c2)
return complex(c1.re * c2.re - c1.im * c2.im, c1.re * c2.im + c1.im *
c2.re)
end
function divide_complex(c1, c2)
denominator = c2.re^2 + c2.im^2
return complex((c1.re * c2.re + c1.im * c2.im) / denominator, (c1.im *
c2.re - c1.re * c2.im) / denominator)
end
# Example usage
c1 = complex(12, 8)
c2 = complex(3, 4)
println("c1 = ", c1)
println("c2 = ", c2)
println("c1 + c2 = ", add_complex(c1, c2))
println("c1 - c2 = ", subtract_complex(c1, c2))
println("c1 * c2 = ", multiply_complex(c1, c2))
println("c1 / c2 = ", divide_complex(c1, c2))
