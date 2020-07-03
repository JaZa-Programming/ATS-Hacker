"""Tests for the command line interface for ats_hacker."""

from cli.cli import CLI


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


# def test_command_line_print_help_with_no_args(capsys):
#     CLI.start()
#     out, err = capsys.readouterr()
#     want = "Usage: python3 ats_hacker <filename>"
#     assert want == out


def test_command_line_print_help_with_dashdash_h_arg(capsys):
    pass


def test_command_line_run_successful_simple():
    pass


def test_command_line_run_successful_complex():
    pass


def test_command_line_run_without_filename():
    pass
