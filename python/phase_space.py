import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pandas as pd
import sys

'''
if len(sys.argv) < 4:
    print("Usage: python3 script.py <S0 value> <I0 value> <R0 value>")
    sys.exit(1)

gamma = "{:.6f}".format(float(sys.argv[1]))
mu = "{:.6f}".format(float(sys.argv[2]))
delta = "{:.6f}".format(float(sys.argv[3]))
R0 = float(sys.argv[2])/float(sys.argv[1])
'''

gamma = "0.250000"
mu = "0.700000"

df00 = pd.read_csv("../data/SIR_" + gamma + "_" + mu + "_" + "0.000000" + ".csv")
df0125 = pd.read_csv("../data/SIR_" + gamma + "_" + mu + "_" + "0.125000" + ".csv")
df0225 = pd.read_csv("../data/SIR_" + gamma + "_" + mu + "_" + "0.225000" + ".csv")
df025 = pd.read_csv("../data/SIR_" + gamma + "_" + mu + "_" + "0.250000" + ".csv")


#view phase space
fig, ax = plt.subplots(figsize=(8, 6))
fig.subplots_adjust(left=0.08, right=0.94, top=0.94, bottom=0.09)

col=["blue", "orange", "green", "red"]
ax.errorbar(x=df00.S, y=df00.I, fmt="o-", color=col[0], label="$\delta = 0.0$")
ax.errorbar(x=df0125.S, y=df0125.I, fmt="o-", color=col[1], label="$\delta = 0.125$")
ax.errorbar(x=df0225.S, y=df0225.I, fmt="o-", color=col[2], label="$\delta = 0.225$")
ax.errorbar(x=df025.S, y=df025.I, fmt="o-", color=col[3], label="$\delta = 0.25$")

x = [ df.loc[df['I'].idxmax(), 'S'] for df in [df00, df0125, df0225, df025]]
ymax = [ df.loc[df['I'].idxmax(), 'I'] for df in [df00, df0125, df0225, df025]]

for i in range(4):
	ax.vlines(x=x[i], ymin=0, ymax=ymax[i], linestyles="dashed", color=col[i])
	ax.scatter(x=[x[i]], y=[0], color=col[i])

ax.set_ylabel("$I_{n}$")
ax.set_xlabel("$S_{n}$")
ax.set_title("$(\gamma, \mu) = ($" + gamma + ", " + mu + "$)$")
ax.legend()
ax.grid(True)

plt.savefig("../data/plots/All_S_I_phase_space_" + gamma + "_" + mu + ".png")
ax.cla()


#view phase space (I_{n+1}, I_n)
fig, ax = plt.subplots(figsize=(8, 8))
fig.subplots_adjust(left=0.08, right=0.94, top=0.94, bottom=0.09)

lab = ["$\delta = 0.0$", "$\delta = 0.125$", "$\delta = 0.225$", "$\delta = 0.25$"]
df = [df00, df0125, df0225, df025]
for i in range(4):
	array = df[i].I
	arrayp1 = array[1:]
	array = array[:-1]

	ax.errorbar(x=array, y=arrayp1, fmt="o-", label=lab[i])
ax.plot([-0.05,0.7], [-0.05,0.7], linestyle="dashed", color="black")
ax.set_ylabel("$I_{n+1}$")
ax.set_xlabel("$I_{n}$")
ax.set_ylim(-0.05, 0.7)
ax.set_xlim(-0.05, 0.7)
ax.set_title("$(\gamma, \mu) = ($" + gamma + ", " + mu + "$)$")
ax.legend()
ax.grid(True)

plt.savefig("../data/plots/All_Inp1_In_phase_space_" + gamma + "_" + mu + ".png")
ax.cla()
















