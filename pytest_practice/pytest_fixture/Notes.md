# Part A - capsys

## Q1. What is capsys?

capsys is a built-in PyTest fixture that captures everything written to stdout and stderr during test execution.

Example

```python
def test_speed(capsys):
    print("Speed")
    captured = capsys.readouterr()
    assert captured.out == "Speed\n"
```

---

## Q2. What is stdout?

stdout (Standard Output) is the default output stream used to display normal program output on the console.

Example

```python
print("Vehicle Ready")
```

writes to stdout.

---

## Q3. What is stderr?

stderr (Standard Error) is the output stream used for error messages and exceptions.

---

## Q4. Does print() return the printed value?

No.

print() writes data to stdout and returns None.

Example

```python
result = print("Hello")

print(result)
```

Output

```
Hello
None
```

---

## Q5. Why do we use capsys?

To verify console output produced by print() statements.

Instead of manually checking the terminal, tests automatically validate the output.

---

## Q6. What does readouterr() return?

It returns a CaptureResult object.

It contains:

- captured.out
- captured.err

Example

```python
captured = capsys.readouterr()
```

---

## Q7. What happens after readouterr()?

PyTest returns the captured output and clears the internal capture buffer.

---

## Q8. When should capsys be used?

Only when testing console output.

If a function returns a value, use a normal assertion instead.

---

# Part B - File Handling & tmp_path

## Q9. Why is with open() preferred?

Because it automatically closes the file, even if an exception occurs.

---

## Q10. What does open() return?

A File Object.

The File Object is used to read from and write to the file.

---

## Q11. What is pathlib?

pathlib is Python's object-oriented library for handling file and directory paths.

---

## Q12. What is a Path Object?

A Path Object represents a file or directory path as a Python object instead of a string.

Example

```python
Path("logs/report.txt")
```

---

## Q13. Why was pathlib introduced?

To provide a cleaner, more readable, and cross-platform way to work with file paths.

---

## Q14. Difference between write() and write_text()

write()

- Works with File Objects
- Requires open()
- Requires close()

Example

```python
with open("log.txt","w") as file:
    file.write("PASS")
```

write_text()

- Works with Path Objects
- Automatically opens, writes, and closes the file

Example

```python
path.write_text("PASS")
```

---

## Q15. What is tmp_path?

tmp_path is a built-in PyTest fixture that provides a temporary directory as a Path Object.

Each test gets its own isolated folder.

---

## Q16. Why use tmp_path?

To create temporary files without cluttering the project.

PyTest automatically deletes the directory after the test.

---

## Q17. Why is tmp_path a Path Object?

Because it supports methods like:

- write_text()
- read_text()
- exists()
- mkdir()

and allows joining paths using "/".

---

# Part C - autouse

## Q18. What is autouse?

autouse=True makes a fixture execute automatically before every applicable test.

Example

```python
@pytest.fixture(autouse=True)
def environment():
    yield
```

---

## Q19. Why was autouse introduced?

To avoid repeating common setup code across multiple tests (DRY principle).

---

## Q20. Difference between normal fixture and autouse?

Normal Fixture

```python
def test(vehicle):
```

The fixture must be requested explicitly.

Autouse Fixture

```python
@pytest.fixture(autouse=True)
```

Runs automatically without being requested.

---

## Q21. When should autouse be used?

When almost every test requires the same setup.

Examples

- Logger
- CANoe
- Environment setup
- Authentication

---

## Q22. When should autouse NOT be used?

When only a few tests need the fixture.

Examples

- GPS Emulator
- Bluetooth
- Camera

---

## Q23. Can autouse use yield?

Yes.

yield allows setup before the test and cleanup after the test.

Execution Flow

Setup

↓

Test

↓

Cleanup

---

## Q24. Can autouse have scope?

Yes.

Example

```python
@pytest.fixture(
    autouse=True,
    scope="session"
)
```

---

# Best Practices

✔ Return values whenever possible.

✔ Use capsys only for printed output.

✔ Use tmp_path for temporary test files.

✔ Use write_text() for simple file writing.

✔ Use with open() for complex file operations.

✔ Use autouse only for common setup shared by most tests.