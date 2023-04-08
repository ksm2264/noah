import os
import subprocess
import sys
import uuid

# Get the input argument from the command line
input_str = sys.argv[1]

# Define the name of the new branch as a UUID
new_branch_name = str(uuid.uuid4())

# Checkout a new branch
subprocess.run(["git", "checkout", "-b", new_branch_name])

# Create a new file in the current directory
new_file_path = os.path.join(os.getcwd(), "new_file.txt")
with open(new_file_path, "w") as f:
    f.write(input_str)

# Add the new file to the Git repository
subprocess.run(["git", "add", new_file_path])

# Commit the changes to the new branch
subprocess.run(["git", "commit", "-m", "Added new file to branch"])

sys.stdout.write(new_branch_name)
