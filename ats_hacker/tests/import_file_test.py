"""Tests for the file_import function."""

import pytest
from api.import_file import import_file


def test_sucessful_file_open():
    filename = "ats_hacker/tests/test_data/simple-job.txt"
    got = import_file(filename)
    assert got is not None


def test_unsuccessful_file_open(capsys):
    filename = "ats_hacker/tests/test_data/doesnt-exist.txt"

    try:
        _ = import_file(filename)
    except (FileNotFoundError, SystemExit):
        pass
    _, err = capsys.readouterr()
    want = "ats_hacker: error: No such file or directory: 'ats_hacker/tests/test_data/doesnt-exist.txt'\n"
    assert err == want


def test_successful_file_import():
    filename = "ats_hacker/tests/test_data/simple-job.txt"
    got = import_file(filename)
    want = "Software Engineer\nSuper Cool Company\nBozeman, MT or Remote\n"
    assert got == want
