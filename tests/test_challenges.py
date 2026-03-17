"""Tests for Week 2 Harbor Rescue Inventory challenges."""

from src.challenges import (
    cargo_window,
    first_supply_index,
    mission_snapshot,
    priority_load,
    supply_report,
)


def test_mission_snapshot_normal() -> None:
    assert mission_snapshot(["rope", "radio", "water"]) == ("rope", "water")


def test_mission_snapshot_one_item() -> None:
    assert mission_snapshot(["flare"]) == ("flare", "flare")


def test_mission_snapshot_empty() -> None:
    assert mission_snapshot([]) == (None, None)


def test_cargo_window_normal() -> None:
    assert cargo_window(["rope", "radio", "water", "medkit"], 1, 2) == [
        "radio",
        "water",
    ]


def test_cargo_window_long_size() -> None:
    assert cargo_window(["rope", "radio"], 0, 5) == ["rope", "radio"]


def test_cargo_window_start_out_of_range() -> None:
    assert cargo_window(["rope", "radio"], 5, 2) == []


def test_cargo_window_zero_size() -> None:
    assert cargo_window(["rope", "radio"], 1, 0) == []


def test_cargo_window_negative_size() -> None:
    assert cargo_window(["rope", "radio"], 1, -3) == []


def test_first_supply_index_found() -> None:
    assert first_supply_index(["rope", "radio", "water"], "radio") == 1


def test_first_supply_index_first_match() -> None:
    assert first_supply_index(["rope", "rope", "water"], "rope") == 0


def test_first_supply_index_missing() -> None:
    assert first_supply_index(["rope", "radio"], "medkit") == -1


def test_first_supply_index_empty() -> None:
    assert first_supply_index([], "radio") == -1


def test_supply_report_found_multiple() -> None:
    assert supply_report(["medkit", "rope", "medkit"], "medkit") == (2, 0)


def test_supply_report_missing() -> None:
    assert supply_report(["rope", "radio", "water"], "medkit") == (0, -1)


def test_supply_report_empty() -> None:
    assert supply_report([], "medkit") == (0, -1)


def test_priority_load_normal() -> None:
    original = ["rope", "radio"]
    result = priority_load(original, "medkit")

    assert result == ["medkit", "rope", "radio"]
    assert original == ["rope", "radio"]


def test_priority_load_empty() -> None:
    assert priority_load([], "flare") == ["flare"]