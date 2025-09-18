# Agent Modules

This folder contains shared modules designed for use across multiple agents. Each module is self-contained, with its own dependencies and logic, and is managed via `uv` and `pyproject.toml`.

## How to add a new module

1. Ensure `uv` is installed

    `uv` is the workspace and package manager used to manage environments and local modules in this repository.

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

    Some modules use Poetry for dependency management; having it installed lets you add and lock dependencies inside a module.

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

3. Create a virtual environment

    Use an isolated environment so module dependencies don't conflict with system Python or other projects.

    ```bash
    uv venv
    source .venv/bin/activate
    ```

4. Create your module folder

    Place new shared modules under `shared/`. Use a descriptive, pluralized name if it contains multiple utilities.

    Example:
    ```bash
    mkdir -p shared/dataframes
    ```

5. Initialize the Python project with `uv`

    This scaffolds the module (e.g., creates `pyproject.toml`) so it can be managed and published as a package.

    ```bash
    cd shared/dataframes
    uv init
    ```

6. Add dependencies to your module

    Add libraries your module needs. Do this from within the module folder so they are recorded in that module's lockfile.

    To install a dependency like pandas:
    ```bash
    poetry add pandas
    ```

7. Create the package files

    Ensure the directory is a proper Python package so other projects can import it.

    ```bash
    touch __init__.py
    ```

8. Register the module in the root `pyproject.toml`

    Registering the module as a workspace member lets `uv` discover, build, and link it locally.

    Add this to the `members` array:
    ```toml
    [tool.uv.workspace]
    members = ["shared/dataframes"]
    ```

9. Create an example usage script

    A small example in `examples/` helps validate the module's API and provides documentation.

    Add your test script in the `examples/` folder

10. Test your module

    Run the example to confirm the module imports correctly and behaves as expected.

    ```bash
    python -m examples.dataframe
    ```