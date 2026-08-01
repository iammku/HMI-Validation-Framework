# HMI Validation Framework

A Python-based automation framework for Automotive HMI (Human Machine Interface) and Instrument Cluster validation.

This project is being developed from scratch to learn automation framework design while following software engineering best practices such as modular architecture, centralized logging, configuration management, clean code, and scalable framework development.

> **Current Version:** Framework v1.0

---

# Overview

The HMI Validation Framework aims to provide a clean, modular, and scalable automation framework for validating Automotive HMI and Instrument Cluster features.

The framework is built incrementally with a strong focus on:

- Python best practices
- Clean architecture
- Reusable components
- Maintainable code
- Interview-ready framework design

---

# Current Features

- Centralized logging framework
- JSON configuration support
- YAML configuration support
- Dynamic project path resolution using `pathlib`
- Configuration validation
- Required key validation
- Configuration value validation
- Custom framework exceptions
- Fail Fast architecture
- Modular project structure

---

# Technologies Used

- Python 3.12
- JSON
- YAML (PyYAML)
- pathlib
- logging
- Git
- GitHub
- PyTest (learning completed, framework integration planned)

---

# Project Structure

```text
HMI-Validation-Framework/
│
├── config/
│   ├── test_config.json
│   └── test_config.yaml
│
├── core/
│   ├── __init__.py
│   ├── cluster.py
│   ├── config_reader.py
│   └── logger.py
│
├── tests/
│
├── practice/
│
├── practice_archive/
│
├── reports/
│
├── logs/
│
├── pytest.ini
├── README.md
└── .gitignore
```

---

# Framework Architecture

```text
Configuration File
        │
        ▼
Config Reader
        │
        ▼
Configuration Validation
        │
        ▼
Framework Modules
        │
        ▼
Automation Tests
```

---

# Design Principles

This framework currently follows:

- Single Responsibility Principle (SRP)
- Modular Design
- Fail Fast Principle
- Centralized Configuration Management
- Centralized Logging
- Extensible Architecture

---

# Current Framework Modules

## logger.py

Responsible for:

- Logger creation
- Console logging
- File logging
- Log formatting

---

## config_reader.py

Responsible for:

- Reading JSON/YAML configuration
- Configuration validation
- Custom exceptions
- Returning configuration to the framework

---

## cluster.py

Demonstrates how framework modules consume configuration without knowing how it is loaded.

---

# Future Roadmap

Planned enhancements include:

- PyTest framework integration
- HTML reporting
- CAN utility modules
- Vehicle abstraction layer
- Test execution engine
- CI/CD integration
- Docker support
- AI-assisted automation utilities

---

# Learning Journey

This repository is both a learning project and an automation framework.

Instead of copying an existing framework, every component is implemented from scratch to understand:

- Why it exists
- How it works
- How it scales
- How to explain it confidently in technical interviews

---

# Author

**Manish Kumar**

Automotive Test Automation Engineer

Currently building a production-style Python automation framework for Automotive HMI validation while preparing for Senior SDET and Automotive Automation Engineer roles.

---