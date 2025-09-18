Agent Modules

This folder contains shared modules designed for use across multiple agents. Each module is self-contained, with its own dependencies and logic, and is managed via `uv` and `pyproject.toml`.

How to Add a New Module under shared/

1. Ensure `uv` is installed
   - macOS (Homebrew): brew install uv
   - Linux (install script): curl -LsSf https://astral.sh/uv/install.sh | sh
   - Windows (winget): winget install astral-sh.uv
   - Windows (Chocolatey): choco install uv
   - Or via pipx (cross-platform): pipx install uv

2. Create your module folder
   Example: mkdir -p `shared/dataframes`

3. Initialize the Python project using `uv`
   cd `shared/dataframes`
   `uv` init

4. Add dependencies to your module
   To install a dependency like pandas: `uv` pip install pandas

5. Create the package files
   touch `__init__.py`
   Add your module code (e.g., `shared/dataframes/main.py`)
