using Plots
x_values1 = -pi:0.01:pi
y11(x) = sin(x) + sin(2x)
y12(x) = sin(2x) + sin(3x)
y_values1 = y11.(x_values1)
y_values2 = y12.(x_values1)
plot(x_values1, y_values1, label="y = sin(x) + sin(2x)", xlabel="x", ylabel="y", title="Plot of
y = sin(x) + sin(2x)")
plot!(x_values1, y_values2, label="y = sin(2x) + sin(3x)")
