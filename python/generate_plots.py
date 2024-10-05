import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd
import sys

if len(sys.argv) < 4:
    print("Usage: python3 script.py <S0 value> <I0 value> <R0 value>")
    sys.exit(1)

gamma = "{:.6f}".format(float(sys.argv[1]))
mu = "{:.6f}".format(float(sys.argv[2]))
delta = "{:.6f}".format(float(sys.argv[3]))
R0 = float(sys.argv[2])/float(sys.argv[1])

df = pd.read_csv("../data/SIR_" + gamma + "_" + mu + "_" + delta + ".csv")

fig, ax = plt.subplots(figsize=(6, 4))
fig.subplots_adjust(left=0.09, right=0.91, top=0.9, bottom=0.12)

#view raw data
ax.plot(df["S"], "bo-")
ax.plot(df["I"], "ro-")
ax.plot(df["R"], "go-")
ax.legend(["S","I","R"])
ax.set_ylabel("Ratio")
ax.set_xlabel("Step")
ax.set_title("$(\gamma, \mu, \delta) = ($" + gamma  + ", " + mu + ", " + delta + "$)$")
ax.set_ylim(-0.05, 1.05)

# Set major ticks on even integers for the x-axis
fig.gca().xaxis.set_major_locator(MultipleLocator(50))  # Set major ticks every 2 units

plt.savefig("../data/plots/raw_SIR_" + gamma + "_" + mu + "_" + delta + ".png")
ax.cla()

fig, ax = plt.subplots(figsize=(6, 4))
fig.subplots_adjust(left=0.09, right=0.91, top=0.9, bottom=0.12)

#view phase space
ax.errorbar(x=df.S, y=df.I, fmt="o-")
ax.set_ylabel("$I_{n}$")
ax.set_xlabel("$S_{n}$")
ax.set_title("$(\gamma, \mu, \delta) = ($" + gamma + ", " + mu + ", " + delta + "$)$")


plt.savefig("../data/plots/S_I_phase_space_" + gamma + "_" + mu + "_" + delta + ".png")
ax.cla()


#view phase space (I_{n+1}, I_n)
array = df.I
arrayp1 = array[1:]
array = array[:-1]

ax.errorbar(x=array, y=arrayp1, fmt="o-")
ax.set_ylabel("$I_{n+1}$")
ax.set_xlabel("$I_{n}$")
ax.set_title("$(\gamma, \mu, \delta) = ($" + gamma + ", " + mu + ", " + delta + "$)$")

plt.savefig("../data/plots/Inp1_In_phase_space_" + gamma + "_" + mu + "_" + delta + ".png")
ax.cla()
















