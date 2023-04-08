import os
import subprocess
import sys

# Get the input argument from the command line
input_str = sys.argv[1]

# Define the name of the new branch
new_branch_name = "new-feature-branch"

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

# Push the changes to the remote repository
subprocess.run(["git", "push", "-u", "origin", new_branch_name])

# Create a pull request for the new branch
# Replace <pull_request_title> with the desired title for the pull request
pull_request_title = "Added new file to branch"
subprocess.run(["gh", "pr", "create", "--title", pull_request_title, "--body", "Please review and merge this pull request", "--head", new_branch_name, "--base", "main"])

sys.stdout.write('done')
