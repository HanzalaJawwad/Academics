function evaluate_expression(expression)
try
result = eval(Meta.parse(expression))
println("Result: $result")
catch e
println("Error: $e")
end
end
# Main function
function main()
println("Enter an expression to evaluate:")
expression = readline()
evaluate_expression(expression)
end
# Call the main function
main()
