function letter_frequency(text)
freq = Dict{Char, Int}()
for char in text
if isletter(char)
if haskey(freq, char)
freq[char] += 1
else
freq[char] = 1
end
end
end
return freq
end
println("Enter a line of text:")
text = readline()
freq = letter_frequency(text)
println("Letter frequencies:")
for (letter, count) in freq
println("$letter: $(count)")
end
