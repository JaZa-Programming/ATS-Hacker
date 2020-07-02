"""Tests for the file_import function."""

import pytest
from ats_hacker.api.import_file import import_file


def test_sucessful_file_open():
    filename = "test_data/simple-job.txt"
    got = import_file(filename)
    assert got is not None


def test_unsuccessful_file_open():
    filename = "test_data/doesnt-exist.txt"
    with pytest.raises(IOError) as e:
        assert import_file(filename)
    assert str(e.value) == "File not found or inaccessable"


def test_successful_file_import():
    filename = "test_data/simple-job.txt"
    got = import_file(filename)
    want = "Software Engineer\nSuper Cool Company\nBozeman, MT or Remote\n"
    assert got == want
