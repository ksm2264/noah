import os
import subprocess
import sys
import uuid
from .test import implement_feature

# Get the input argument from the command line
input_str = sys.argv[1]

# Define the name of the new branch as a UUID
new_branch_name = str(uuid.uuid4())

# Checkout a new branch
subprocess.run(["git", "checkout", "-b", new_branch_name], stdout=subprocess.DEVNULL)

implement_feature(input_str)

# Add the new file to the Git repository
subprocess.run(["git", "add", "."], stdout=subprocess.DEVNULL)

# Commit the changes to the new branch
subprocess.run(["git", "commit", "-m", "made changes"], stdout=subprocess.DEVNULL)
 
# Output the new branch name
sys.stdout.write(new_branch_name)
