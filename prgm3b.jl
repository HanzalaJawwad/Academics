function read_numbers_from_file(filename)
    numbers = Float64[] 
    open(filename, "r") do file
        for line in eachline(file)
            line = strip(line) 
            if !isempty(line) 
                try
                    push!(numbers, parse(Float64, line))  # Parse each line as Float64 and store it
                catch e
                    println("Warning: Skipping invalid line: '$line'")
                end
            end
        end
    end
    return numbers
end
function calculate_statistics(numbers)
    if isempty(numbers)
        println("No numbers found in the file.")
        return
    end
    max_number = maximum(numbers)
    min_number = minimum(numbers)
    count = length(numbers)
    total_sum = sum(numbers)
    average = total_sum / count
    println("Largest Number: ", max_number)
    println("Smallest Number: ", min_number)
    println("Count: ", count)
    println("Sum: ", total_sum)
    println("Average: ", average)
end
filename = "C:\\Users\\nelvi\\OneDrive\\Desktop\\Julia_Programs\\input.txt"  # Use double backslashes in file path
numbers = read_numbers_from_file(filename)
calculate_statistics(numbers)