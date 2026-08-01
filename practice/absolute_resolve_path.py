import os
from pathlib import Path

# 1. Show exactly where the terminal is running from
print(f"Current Working Directory: {os.getcwd()}\n")

# 2. Create the relative path
my_path = Path("./manual_test_sync.txt")
my_path1 = Path("../../manual_test_sync.txt")
my_path2 = Path("../manual_test_sync.txt")


# 3. Test absolute() -> Just glues the strings together
print("--- Using .absolute() ---")
print(my_path.absolute())
print(my_path1.absolute())
print(my_path2.absolute())

# 4. Test resolve() -> Calculates the real path (cleans up the ../..)
print("\n--- Using .resolve() ---")
print(my_path.resolve())
print(my_path1.resolve())
print(my_path2.resolve())