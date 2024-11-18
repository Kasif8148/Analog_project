import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\admin\Downloads\New foldhh\idw_1.csv"  # Update with the actual file name
nmos_data = pd.read_csv(file_path)

# Define lengths
lengths = range(45, 721, 45)  # 45nm to 720nm with 45nm step

# Plot Id/W vs gm/Id for each length
plt.figure(figsize=(10, 6))
for length in lengths:
    idw_col = f"IdW_L{length}"  # Column name for Id/W for the given length
    gmid_col = f"gmId_L{length}"  # Column name for gm/Id for the given length
    if idw_col in nmos_data.columns and gmid_col in nmos_data.columns:
        plt.plot(nmos_data[gmid_col], nmos_data[idw_col], label=f"L = {length}nm")

# Add labels and grid
plt.xlabel(r"$g_m / I_D$")
plt.ylabel(r"$I_D / W$ (A/μm)")
plt.title("NMOS: $I_D / W$ vs $g_m / I_D$")
plt.grid(True)

# Move the legend outside the plot area
plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1), borderaxespad=0)

# Adjust layout to make room for the legend
plt.tight_layout()

# Show the plot
plt.show()
