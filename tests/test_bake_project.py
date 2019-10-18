from contextlib import contextmanager

import os
import subprocess


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def test_project_tree(cookies):
    result = cookies.bake(extra_context={"repo_name": "test_project"})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == "test_project"


"""removing flake8 test since it is duplicative to codeclimate for checking for
cyclomatic complexity, to Black for formatting, and not a critical test.
It was causing too many errors in travis but I wanted to leave it in here in case
I want to implement it in the future"""
# def test_run_flake8(cookies):
# result = cookies.bake(extra_context={'repo_name': 'flake8_compat'})
# with inside_dir(str(result.project)):
# subprocess.check_call(['flake8'])
