function eval_expr(expr)
# Parse the expression using Julia's built-in parser
ast = Meta.parse(expr)
# Evaluate the expression using Julia's built-in evaluator
result = eval(ast)
# Return the result as a Float64
return Float64(result)
end
# Test cases
println(eval_expr("2 + 3"))
println(eval_expr("sqrt(2) * pi"))
println(eval_expr("exp(1) / 2"))
println(eval_expr("sin(pi / 4)"))
println(eval_expr("cos(pi / 3)"))
println(eval_expr("1 / 3 + 2 / 5"))
println(eval_expr("(1 + sqrt(2)) * (1 - sqrt(2))"))
