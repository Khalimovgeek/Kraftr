# Kraftr

Kraftr is a lightweight CLI tool for generating backend code faster with minimal manual effort.

This project focuses on simplifying API development by automatically creating function templates for Python-based web frameworks, starting with view functions. The goal is to reduce repetitive boilerplate and improve development speed.

Kraftr is designed as a learning-driven project that explores:

* Code generation using templates
* CLI-based developer tooling
* Incremental file modification (append, not overwrite)
* Future integration with AI for smarter code generation

---

## 🚀 Features (Current)

* Generate API view function templates
* Append functions safely to existing files
* Automatically handle required imports
* Simple CLI interface

---

## 🧱 Project Vision

Kraftr aims to evolve into a full backend scaffolding tool capable of:

* Generating APIs (GET, POST, etc.)
* Building Django models interactively
* Managing imports and file structure intelligently
* Providing a minimal web UI for complex inputs
* Integrating AI/NLP for natural language-based generation

---

## 🛠️ Usage (Planned)

```bash
kraftr api get user crud1
```

This will:

* Generate a GET API function
* Append it to `views.py`
* Add required imports if missing

---

## 📁 Project Structure

```
kraftr/
  cli.py
  generator/
  templates/
  ui/
```

---

## ⚠️ Status

This project is currently in early development. Features are being built incrementally, and the structure may evolve over time.

---

## 💡 Why
