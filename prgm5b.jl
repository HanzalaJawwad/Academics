function read_and_print_words(filename)
    # Initialize a variable to store the current word
    current_word = ""
    
    # Loop through each line in the file
    for line in eachline(filename)
        # Loop through each character in the line
        for char in line
            if isletter(char)  # Check if character is a letter
                current_word *= string(char)  # Append character to the word
            else
                if current_word != ""
                    println(current_word)  # Print the word
                    current_word = ""  # Reset word storage
                end
            end
        end
    end

    # If file ends with a word, print it
    if current_word != ""
        println(current_word)
    end
end

# Call the function with "input.txt"
read_and_print_words("5a.txt")
