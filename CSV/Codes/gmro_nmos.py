import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\admin\Downloads\New foldhh\gmro.csv"  # Update with the actual file name
nmos_data = pd.read_csv(file_path)

# Define lengths
lengths = range(45, 721, 45)  # 45nm to 720nm with 45nm step

# Plot gm*ro vs gm/Id for each length
plt.figure(figsize=(10, 6))
for length in lengths:
    gmro_col = f"gmro_L{length}"
    gmid_col = f"gmId_L{length}"
    if gmro_col in nmos_data.columns and gmid_col in nmos_data.columns:
        plt.plot(nmos_data[gmid_col], nmos_data[gmro_col], label=f"L = {length}nm")

# Add labels and grid
plt.xlabel(r"$g_m / I_D$")
plt.ylabel(r"$g_m \cdot r_o$")
plt.title("NMOS: $g_m \cdot r_o$ vs $g_m / I_D$")
plt.grid(True)

# Move the legend outside the plot area
plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1), borderaxespad=0)

# Adjust layout to make room for the legend
plt.tight_layout()

# Show the plot
plt.show()
