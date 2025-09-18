Agent Modules

This folder contains shared modules designed for use across multiple agents. Each module is self-contained, with its own dependencies and logic, and is managed via `uv` and `pyproject.toml`.

How to Add a New Module

1. Ensure `uv` is installed

macOS (Homebrew):
```bash
brew install uv
```

Linux (install script):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows (winget):
```powershell
winget install astral-sh.uv
```

Windows (Chocolatey):
```powershell
choco install uv
```

Or via pipx (cross-platform):
```bash
pipx install uv
```

2. Ensure Poetry is installed

Check if Poetry is installed:
```bash
poetry --version
```

Install Poetry if not installed:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Verify the installation:
```bash
poetry --version
```

3. Create virtual environment

```bash
uv venv
source .venv/bin/activate
```

4. Create your module folder

Example:
```bash
mkdir -p shared/dataframes
```

5. Initialize the Python project using `uv`

```bash
cd shared/dataframes
uv init
```

6. Add dependencies to your module

To install a dependency like pandas:
```bash
poetry add pandas
```

7. Create the package files

```bash
touch __init__.py
```

8. Register your module in the root `pyproject.toml`

Add this to the `[tool.uv.workspace]` section:
```toml
"shared/dataframes"
```

9. Create example usage

Add your test script in the `examples/` folder

10. Test your module

```bash
python -m examples.dataframe
```