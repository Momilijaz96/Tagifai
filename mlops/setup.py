from pathlib import Path
from platform import python_revision
from setuptools import find_namespace_packages, setup

# Load packages from requirements.txt
BASE_DIR = Path(__file__).parent
with open( Path(BASE_DIR, "requirements.txt") , "r") as file:
    required_packages = [ ln.strip() for ln in file.readlines() ]


# Heart of setup.py, the setup object
setup(
    name="tagifai",
    version=0.1,
    description = "Categorize the NL articles into respective cateogry",
    author = "Momal Ijaz",
    author_email = "momilijaz@gmail.com",
    url = "https://linkedin.com/momilijaz",
    python_requires = ">=3.7",
    install_requires = [required_packages]
)

