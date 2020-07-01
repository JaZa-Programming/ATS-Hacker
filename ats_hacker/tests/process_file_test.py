"""Tests for the file_processor function."""

import pytest
from ats_hacker.api.process_file import process_file


def test_sucessful_file_open():
    filename = "test_data/simple-job.txt"
    got = process_file(filename)
    assert got is not None


def test_unsuccessful_file_open():
    filename = "test_data/doesnt-exist.txt"
    with pytest.raises(IOError) as e:
        assert process_file(filename)
    assert str(e.value) == "File not found or inaccessable"


def test_successful_file_processing():
    filename = "test_data/simple-job.txt"
    got = process_file(filename)
    want = "Software Engineer\nSuper Cool Company\nBozeman, MT or Remote\n"
    assert got == want
