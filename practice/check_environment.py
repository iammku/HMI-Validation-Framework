import os

print("FRAMEWORK_ENV:")
print(os.getenv("FRAMEWORK_ENV"))

print()

print("Using default:")
print(os.getenv("FRAMEWORK_ENV", "dev"))