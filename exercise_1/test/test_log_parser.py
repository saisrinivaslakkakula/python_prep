import pytest
import tempfile
import os
import csv

from exercise_1.src import log_parser


def parser():
    # Get path to test_logs.csv relative to this test file
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "test_logs.csv")
    return file_path


def test_load_log_file_when_file_is_passed():
    log_parser_obj = log_parser.LogParser(parser())
    res = log_parser_obj.load()
    assert res is not None


def test_load_log_file_when_file_is_not_passed():
    log_parser_obj = log_parser.LogParser("/dummy/path")
    with pytest.raises(FileNotFoundError) as exec:
        log_parser_obj.load()
    assert str(exec.value) == "Log file not found."


def test_filter_by_status_when_log_file_passed_but_not_loaded():
    log_parser_obj = log_parser.LogParser(parser())
    with pytest.raises(RuntimeError) as exec:
        log_parser_obj.filter_by_status("PASS")
    assert str(exec.value) == "Logs not loaded. Call load() first."


def test_filter_by_status_when_log_file_passed_and_status_passed():
    log_parser_obj = log_parser.LogParser(parser())
    log_parser_obj.load()
    res = log_parser_obj.filter_by_status("PASS")
    assert len(res) > 0


def test_filter_by_status_when_log_file_passed_and_status_failed():
    log_parser_obj = log_parser.LogParser(parser())
    log_parser_obj.load()
    res = log_parser_obj.filter_by_status("FAIL")
    assert len(res) > 0


def test_filter_by_status_when_log_file_passed_and_status_invalid():
    log_parser_obj = log_parser.LogParser(parser())
    log_parser_obj.load()
    res = log_parser_obj.filter_by_status("some invalid status")
    assert len(res) == 0


def test_average_duration_returns_zero_when_log_file_not_loaded():
    log_parser_obj = log_parser.LogParser(parser())
    avg_duration = log_parser_obj.average_duration()
    assert avg_duration == 0.0


def test_average_duration_returns_happy_case():
    log_parser_obj = log_parser.LogParser(parser())
    log_parser_obj.load()
    avg_duration = log_parser_obj.average_duration()
    assert avg_duration is not None
    assert avg_duration > 0.0


def test_slowest_test_returns_empty_dict_when_log_file_not_loaded():
    log_parser_obj = log_parser.LogParser(parser())
    slowest_test = log_parser_obj.slowest_test()
    assert slowest_test is not None
    assert len(slowest_test) == 0


def test_slowest_test_returns_happyCase():
    log_parser_obj = log_parser.LogParser(parser())
    log_parser_obj.load()
    slowest_test = log_parser_obj.slowest_test()
    assert slowest_test is not None
    assert len(slowest_test) > 0


def test_simulate_external_service_when_test_name_is_empty():
    log_parser_obj = log_parser.LogParser(parser())
    log_parser_obj.load()
    with pytest.raises(ValueError) as exec:
        log_parser_obj.simulate_external_service(None)
    assert str(exec.value) == "Test name must not be empty"


def test_simulate_external_service_happy_case():
    log_parser_obj = log_parser.LogParser(parser())
    log_parser_obj.load()
    result = log_parser_obj.simulate_external_service("test_name")
    assert result is not None
    assert (result == "PASS" or result == "FAIL")




