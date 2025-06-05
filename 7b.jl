function fetch_words(file_path::AbstractString)
# Initialize an empty set to store unique words
unique_words = Set{String}()
# Open the file for reading
open(file_path) do file
# Read each line from the file
for line in eachline(file)
# Remove punctuation and split the line into words
words = split(replace(lowercase(line), r"[[:punct:]]" => ""), " ")
# Add each word to the set
for word in words
push!(unique_words, word)
end
end
end
return unique_words
end
# Example usage
file_path = " C:\Users\LENOVO\Desktop" # Replace with your file path
words_set = fetch_words(file_path)
println("Unique words found in the file:")
for word in words_set
println(word)
end
