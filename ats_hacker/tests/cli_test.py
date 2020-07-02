"""Tests for the command line interface for ats_hacker."""

from ats_hacker.cli.cli import CLI


def test_cli_class_instantiation():
    cli = CLI()
    assert cli.document == ""
    assert cli.keyword_counts == {}


def test_set_document():
    cli = CLI()
    document = "This is a test document."
    cli.process_document(document)
    assert cli.document == document


def test_keyword_counts():
    cli = CLI()
    document = "This is a test document."
    keyword_counts = {"this": 1, "is": 1, "a": 1, "test": 1, "document": 1}
    cli.process_document(document)
    assert cli.keyword_counts == keyword_counts
