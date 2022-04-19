import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
DOCKER_FILES = ["Dockerfile", "docker-compose.yml", "run_tests_in_docker.sh", ".dockerignore"]


def remove(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    to_remove = []

    if '{{cookiecutter.add_test_dockerfile}}' != "y":
        to_remove.extend(DOCKER_FILES)

    for filename in to_remove:
        remove(filename)
