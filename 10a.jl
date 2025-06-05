using Plots
# Generate data points for x in the range -5 to 5
x = range(-5, 5, length=100)
# Calculate corresponding y values for the function y = x²
y1 = x.^2
# Calculate corresponding y values for the function y = -x²
y2 = -x.^2
# Create a plot
plt = plot(x, y1, label="y = x²", linestyle=:solid, linewidth=2, xlabel="x",
ylabel="y", title="Plot of y = x² (solid) and y = -x² (dotted)")
# Add a dotted line to the plot
plot!(x, y2, label="y = -x²", linestyle=:dot, linewidth=2)
# Show the plot
display(plt)
