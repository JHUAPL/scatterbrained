from pathlib import Path

from setuptools import find_packages, setup

HERE = Path(__file__).parent
README = HERE.joinpath("README.md").read_text()
REQUIREMENTS = HERE.joinpath("requirements", "requirements.in").read_text().split()


def get_version(rel_path: Path):
    contents = HERE.joinpath(rel_path).read_text().splitlines()
    for line in contents:
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="scatterbrained",
    version=get_version(Path("src", "scatterbrained", "version.py")),
    author="Miller Wilt",
    author_email="miller.wilt@jhuapl.edu",
    description="Decentralized Federated Learning framework",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=REQUIREMENTS,
    python_requires=">=3.8.0",
)
