using ArgParse
function parse_commandline()
    s = ArgParseSettings()
    @add_arg_table s begin
        "--P" 
        arg_type = Float64
        help = "The principal amount."
        "--r"  
        arg_type = Float64
        help = "The interest rate percentage."
    end
    return parse_args(s)
end
function print_amounts(P::Float64, r::Float64)
    println("Year 1 amount: ", P)
    for year in 2:10
        P = P * (1 + r / 100)
        println("Year $year amount: ", P)
        if P > 2 * P
            println("Amount exceeded 2P, stopping further printing.")
            break
        end
    end
end
function main()
    parsed_args = parse_commandline()
    P = get(parsed_args, "P", nothing)
    r = get(parsed_args, "r", nothing)
    if P === nothing
        println("Enter the principal amount (P): ")
        P = parse(Float64, readline())
    end
    if r === nothing
        println("Enter the interest rate (r) in percentage: ")
        r = parse(Float64, readline())
    end
    print_amounts(P, r)
end
main()