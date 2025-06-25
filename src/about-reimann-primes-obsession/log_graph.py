import matplotlib.pyplot as plt
import numpy as np
import pickle


with open("SpotSaver.pkl", "rb") as infile:
    data = pickle.load(infile)

X = np.array(data["x"])
Y_Frac = np.array(data["y_frac"])
Y_Float = np.array(data["y_float"])


with open("Y_vector.pkl", "rb") as infile:
    Y = pickle.load(infile)


plt.figure(figsize=(8, 6))  # Set the figure size
plt.plot(
    X,
    Y,
    label="Logarithmic Curve",
    color="blue",
    marker="x",
    markersize=5,
    markerfacecolor="red",
)  # Plot the curve
plt.xscale("log")
plt.title("Logarithmic Graph")  # Add a title
plt.xlabel("X-axis")  # Label x-axis
plt.ylabel("Log(X)")  # Label y-axis
plt.grid(True)  # Add a grid for better readability
plt.legend()  # Display the legend
plt.show()  # Show the graph
