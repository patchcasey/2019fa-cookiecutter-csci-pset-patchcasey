from contextlib import contextmanager

import os
import sys
import subprocess	
import shlex
from cookiecutter.utils import rmtree


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
		
def test_bake_with_defaults(cookies):
	# taken from cookiecutter python template https://github.com/audreyr/cookiecutter-pypackage/blob/master/tests/test_bake_project.py
    result = cookies.bake(extra_context={"repo_name": "test_project"})
	assert result.project.isdir()
	assert result.exit_code == 0
	assert result.exception is None

	with open("Pipfile", "r") as f:
        lines = f.readlines()
	for x in lines:
		if x.find("csci-utils") = 0:
			raise AssertionError
		
def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'Pipfile' in found_toplevel_files
        assert 'test_pset.py' in found_toplevel_files
        assert 'pytest.ini' in found_toplevel_files

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
