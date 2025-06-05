# Function to perform addition
function add(x, y)
return x + y
end
# Function to perform subtraction
function subtract(x, y)
return x - y
end
# Function to perform multiplication
function multiply(x, y)
return x * y
end
# Function to perform division
function divide(x, y)
if y == 0
println("Error: Division by zero")
return NaN
else
return x / y
end
end
# Main function
function main()
println("Welcome to the Calculator Program")
println("Enter two numbers:")
num1 = parse(Float64, readline()) # Input first number
num2 = parse(Float64, readline()) # Input second number
println("Choose an operation:")
println("1. Addition (+)")
println("2. Subtraction (-)")
println("3. Multiplication (*)")
println("4. Division (/)")
operation = readline()
if operation == "1"
result = add(num1, num2)
println("Result: ", result)
elseif operation == "2"
result = subtract(num1, num2)
println("Result: ", result)
elseif operation == "3"
result = multiply(num1, num2)
println("Result: ", result)
elseif operation == "4"
result = divide(num1, num2)
println("Result: ", result)
else
println("Invalid operation selected")
end
end
# Call the main function
main()
