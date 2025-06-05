function calculate_pay(hours_worked, rate_of_pay)
regular_pay = 0
overtime_pay = 0
if hours_worked <= 40
regular_pay = hours_worked * rate_of_pay
else
regular_pay = 40 * rate_of_pay
overtime_hours = hours_worked - 40
overtime_pay = overtime_hours * rate_of_pay * 1.5
end
gross_pay = regular_pay + overtime_pay
return regular_pay, overtime_pay, gross_pay
end
# Example usage
hours_worked = 45
rate_of_pay = 10
regular_pay, overtime_pay, gross_pay = calculate_pay(hours_worked,
rate_of_pay)
println("Regular Pay: ", regular_pay)
println("Overtime Pay: ", overtime_pay)
println("Gross Pay: ", gross_pay)
