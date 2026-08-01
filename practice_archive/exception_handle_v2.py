class NoFunds(Exception):
    pass
try:
    amt, bal = 500, 100
    if amt > bal:
        raise NoFunds("Broke!")  # 1. RAISE triggers error

except TypeError:
    print("Use numbers, not words!")  # 2a. EXCEPT handles wrong data types

except NoFunds as e:
    print(e)  # 2b. EXCEPT handles our custom error

else:
    print("Success!")  # 3. ELSE runs if NO error

finally:
    print("Done.")  # 4. FINALLY always runs