import argparse

import toml

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""
        Get dependencies from pyproject.toml because pip doesn't support it
        """
    )
    parser.add_argument("--dependency-group", type=str, nargs="*")

    args = parser.parse_args()

    pyproject = toml.load("pyproject.toml")

    requirements = {
        *pyproject["build-system"]["requires"],
        *pyproject["project"]["dependencies"]
    }

    if args.dependency_group:
        for dependency_group in args.dependency_group:
            requirements = {
                *requirements,
                *pyproject["project"]["optional-dependencies"][dependency_group]
            }

    with open("requirements.txt", "w") as f:
        f.writelines("\n".join(sorted(requirements)))
