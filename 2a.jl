function calculate_charge(hours_worked, parts_cost)
labor_cost = max(100 * hours_worked, 150) # Ensure minimum charge of
$150
total_cost = labor_cost + parts_cost
return total_cost
end
# Main function
function main()
println("Welcome to the Computer Repair Shop!")
println("Enter the number of hours worked:")
hours_worked = parse(Float64, readline())
println("Enter the cost of parts:")
parts_cost = parse(Float64, readline())
total_charge = calculate_charge(hours_worked, parts_cost)
println("The total charge for the repair job is:", total_charge)
end
# Call the main function
main()
