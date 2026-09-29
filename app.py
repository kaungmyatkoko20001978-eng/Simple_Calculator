import sys
import platform

print("Hello from the cloud!")
print(f"Python Version: {sys.version.split()[0]}")
print(f"Operating System: {platform.system()} ({platform.release()})")

import os
import shutil

print("=== DEVOPS SYSTEM CHECKER ===")

# Get user input
username = input("Enter your name: ")
print(f"Welcome to the server, {username}!")

# Check disk space in the Linux container
total, used, free = shutil.disk_usage("/")
gb = 1024 ** 3

print("\n--- Storage Report ---")
print(f"Total Cloud Space: {total / gb:.2f} GB")
print(f"Used Space:        {used / gb:.2f} GB")
print(f"Free Space:        {free / gb:.2f} GB")

# Basic decision logic
free_gb = free / gb
if free_gb > 10:
    print("\nStatus: Server health is optimal! Plenty of space left.")
else:
    print("\nStatus: Warning! Storage is running low.")