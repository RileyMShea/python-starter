"""Actions to take before Rendering the cookiecutter template.

For reliability this should not import anything outside of the standard
library and the cookiecutter dependencies.
"""

import pathlib
import logging

# setup logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


path_files = list(pathlib.Path.cwd().glob("**/*"))
if path_files:
    raise Exception(f"Found files in current directory: {path_files}\nAborting!")

if __name__ == "__main__":
    logger.debug("END  PRE_HOOK")
