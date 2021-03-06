"""Tests for the command line interface for ats_hacker."""

import sys
from cli.cli import CLI


def test_cli_class_instantiation():
    cli = CLI()
    assert cli.document == ""
    assert cli.keyword_counts == {}


def test_set_document():
    cli = CLI()
    document = "This is a test document."
    cli._process_document(document)
    assert cli.document == document


def test_keyword_counts():
    cli = CLI()
    document = "This is a test document."
    keyword_counts = {"this": 1, "is": 1, "a": 1, "test": 1, "document": 1}
    cli._process_document(document)
    assert cli.keyword_counts == keyword_counts


def test_command_line_with_no_filename(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ['ats_hacker'])
    try:
        cli = CLI()
        cli.start()
    except SystemExit:
        pass
    _, err = capsys.readouterr()
    want = "usage: ats_hacker [-h] [-o [json]] [-r [filename]] filename\n" \
        "ats_hacker: error: the following arguments are required: filename\n"
    assert want == err


def test_command_line_print_help_with_dash_h_arg(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ['ats_hacker', '-h'])
    try:
        cli = CLI()
        cli.start()
    except SystemExit:
        pass
    out, _ = capsys.readouterr()
    want = "usage: ats_hacker [-h] [-o [json]] [-r [filename]] filename\n\n" \
        "Keyword aggregator for ATS optimization.\n\n" \
        "positional arguments:\n" \
        "  filename       txt filename for keyword aggregation\n\n" \
        "optional arguments:\n" \
        "  -h, --help     show this help message and exit\n" \
        "  -o [json]      output in raw JSON format\n" \
        "  -r [filename]  txt filename for words to remove\n"
    assert want == out


def test_command_line_run_successful_pretty(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ['ats_hacker',
                                      'ats_hacker/tests/test_data/simple-job.txt'])
    try:
        cli = CLI()
        cli.start()
    except SystemExit:
        pass
    out, _ = capsys.readouterr()
    output_words = out.split()
    print(output_words)
    for word in ["Document:", "Word", "Occurances"]:
        assert output_words.index(word)


def test_command_line_run_successful_json(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ['ats_hacker',
                                      'ats_hacker/tests/test_data/simple-job.txt', '-o', 'json'])
    cli = CLI()
    cli.start()
    out, _ = capsys.readouterr()
    want = '{"software": 1, "engineer": 1, "super": 1, "cool": 1, ' \
        '"company": 1, "bozeman": 1, "mt": 1, "or": 1, "remote": 1}\n'
    assert want == out


def test_command_line_run_successful_remove_words_json(capsys, monkeypatch):
    monkeypatch.setattr(sys, "argv", ['ats_hacker',
                                      'ats_hacker/tests/test_data/simple-job.txt',
                                      '-o', 'json',
                                      '-r', 'ats_hacker/tests/test_data/words-to-remove.txt'])
    cli = CLI()
    cli.start()
    out, _ = capsys.readouterr()
    want = '{"software": 1, "engineer": 1, "super": 1, "cool": 1, ' \
        '"company": 1, "bozeman": 1, "mt": 1, "remote": 1}\n'
    assert want == out
