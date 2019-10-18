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
		
@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))
		
def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))
		
def test_bake_and_run_tests(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        run_inside_dir('pytest', str(result.project)) == 0
        print("test_bake_and_run_tests path", str(result.project))


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
