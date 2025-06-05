using LinearAlgebra
function matrix_properties(A)
n = size(A, 1)
# Determinant
detA = det(A)
# Inverse
invA = inv(A)
# Rank
rankA = rank(A)
# Upper and Lower Triangular Matrices
U, L = triu(A)
# Diagonal Elements
diagA = diag(A)
# Euclidean Norm
normA = norm(A)
# Square Root
sqrtA = sqrt(A)
return detA, invA, rankA, U, L, diagA, normA, sqrtA
end
A = [3.0 2.0 -1.0; 1.0 0.0 2.0; 0.0 -1.0 1.0]
detA, invA, rankA, U, L, diagA, normA, sqrtA = matrix_properties(A)
println("Determinant: ", detA)
println("Inverse: ", invA)
println("Rank: ", rankA)
println("Upper Triangular Matrix: ", U)
println("Lower Triangular Matrix: ", L)
println("Diagonal Elements: ", diagA)
println("Euclidean Norm: ", normA)
println("Square Root: ", sqrtA)
