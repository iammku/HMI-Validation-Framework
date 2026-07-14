## Topic

Advanced PyTest Fixtures

- autouse
- capsys
- tmp_path
- pathlib
- File Handling

---

## Objective

Implement an automotive cluster validation framework demonstrating advanced PyTest fixtures.

---

## Requirements

### Vehicle Class

Create a Vehicle class with the following methods:

- boot_cluster()
- display_speed()
- show_warning()
- display_theme()
- save_cluster_log(path)

---

### autouse Fixture

Create an environment fixture that:

- Runs automatically before every test
- Prints setup message
- Performs cleanup after every test

---

### capsys

Validate console output for:

- display_speed()
- show_warning()

---

### tmp_path

Create a temporary cluster log file.

Validate:

- File creation
- File content

---

### Validation

Verify:

- Cluster Boot
- Cluster Theme
- Speed Display
- Warning Display
- Cluster Log

---