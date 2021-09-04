import toml
import pathlib

pyproject_toml = pathlib.Path.cwd() / ".." / "pyproject.toml"
print(pyproject_toml.is_file())
