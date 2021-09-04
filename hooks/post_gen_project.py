import re
import sys
from dataclasses import dataclass
import sys

from dataclasses import dataclass
import pathlib
import logging
import shlex
import subprocess
import asyncio

# setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hooks/post_gen_project")


@dataclass
class CookieCutterContext:
    """Rendered Cookiecutter variables from Jinja2 templates."""

    repo_name: str = "{{ cookiecutter.repo_name }}"


def validate_python_module_name(project_name: str) -> None:
    """
    Validate the project name is a valid Python module name.

    Extracts the module name the jinja2 template in project_name

    :param project_name: The project name to validate.
    :return: None
    """
    if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", project_name):
        print(
            'Error: Invalid project name "{}". Names must begin with a letter and contain only letters, numbers and underscores.'.format(
                project_name
            )
        )
        sys.exit(1)


async def main():
    cookie_context = CookieCutterContext()
    validate_python_module_name(cookie_context.repo_name)
    await asyncio.gather(
        asyncio.create_subprocess_shell(
            "docker build . -t {{cookiecutter.repo_name}}:v0.1.0"
        ),
        asyncio.create_subprocess_shell(
            "git init && git add --all && git commit -m 'initial commit'"
        ),
        asyncio.create_subprocess_shell(
            "virtualenv -p python3.10 .venv && . .venv/bin/activate && poetry install"
        ),
    )


if __name__ == "__main__":
    asyncio.run(main(), debug=True)

    print("POST DONE")
