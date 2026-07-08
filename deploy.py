import subprocess
import sys

print("========== Starting Deployment ==========")

subprocess.run([sys.executable, "app.py"], check=True)

print("========== Deployment Successful ==========")