# There are six groups that students are to be assigned for discussion posts.
# The following script will iterate the course list provided in csv format and 
# assign each student a group that is to be input to the Group column in the csv 
# file. 

import numpy as np 
import pandas as pd

# Define group names (use a list to preserve order)
groups = ["bottom", "charm", "down", "strange", "top", "up"]
crn = 11388  # Course number
file = f"{crn}_gradesheet.csv"

# Load CSV
class_list = pd.read_csv(file)
n_students = len(class_list)
n_groups = len(groups)

# Determine how many students per group
base, remainder = divmod(n_students, n_groups)
assignments = [g for i, g in enumerate(groups) for _ in range(base + (i < remainder))]

# Shuffle the assignments
np.random.shuffle(assignments)

# Assign to new column
class_list["Group"] = assignments

# Save updated file
output_file = file.replace(".csv", "_with_groups.csv")
class_list.to_csv(output_file, index=False)
print(f"[OK] Saved updated file: {output_file}")