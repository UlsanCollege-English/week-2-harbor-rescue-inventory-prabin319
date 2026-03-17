# Week 2 Assignment — Harbor Rescue Inventory

## Story

You are helping build a tiny inventory system for a harbor rescue team.

Each boat stores its supplies in a Python list. Your job is to write helper
functions that inspect or update those lists correctly.

This week’s work practices:

* functions with clear return values
* list indexing and slicing
* simple searching
* off-by-one boundaries
* basic complexity explanations

## Standards Focus

* S1 — Python + Testing Fundamentals
* S2 — Array/List Cost Model
* S3 — Big-O Reasoning
* S4 — Searching (light preview)

## Files

Use this structure:

* `src/challenges.py`
* `tests/test_challenges.py`
* `README.md`

## Rules

* Python 3.11+
* stdlib only
* do not rename required functions
* write your code in `src/challenges.py`
* use `pytest -q`
* notebooks are demo-only, not graded
* follow PEP 8
* public functions need type hints
* public functions need docstrings

---

## Required Challenge 1 — `mission_snapshot`

```python
def mission_snapshot(items: list[object]) -> tuple[object | None, object | None]:
```

Return a tuple containing the **first** and **last** item in the supply list.

### Rules

* If the list is empty, return `(None, None)`

### Examples

```python
mission_snapshot(["rope", "radio", "water"]) == ("rope", "water")
mission_snapshot(["flare"]) == ("flare", "flare")
mission_snapshot([]) == (None, None)
```

### Why this is here

* carryover from Week 1: exact return contract
* Week 2 skill: indexing

---

## Required Challenge 2 — `cargo_window`

```python
def cargo_window(items: list[object], start: int, size: int) -> list[object]:
```

Return a **new list** containing up to `size` items starting at index `start`.

### Rules

* If `start` is out of range, return `[]`
* If `size <= 0`, return `[]`
* Do not crash on short lists

### Examples

```python
cargo_window(["rope", "radio", "water", "medkit"], 1, 2) == ["radio", "water"]
cargo_window(["rope", "radio"], 0, 5) == ["rope", "radio"]
cargo_window(["rope", "radio"], 5, 2) == []
cargo_window(["rope", "radio"], 1, 0) == []
```

### Why this is here

* carryover from Week 1: reading the function contract carefully
* Week 2 skill: slicing, `len`, boundaries, off-by-one thinking

---

## Required Challenge 3 — `first_supply_index`

```python
def first_supply_index(items: list[object], target: object) -> int:
```

Return the index of the **first** occurrence of `target`.

### Rules

* If `target` is not present, return `-1`
* Do not use `items.index(...)`

### Examples

```python
first_supply_index(["rope", "radio", "water"], "radio") == 1
first_supply_index(["rope", "rope", "water"], "rope") == 0
first_supply_index([], "radio") == -1
first_supply_index(["rope", "radio"], "medkit") == -1
```

### Why this is here

* carryover from Week 1: clean return value, not vague output
* Week 2 skill: searching a list

---

## Required Challenge 4 — `supply_report`

```python
def supply_report(items: list[object], target: object) -> tuple[int, int]:
```

Return a tuple of:

1. how many times `target` appears
2. the index of its **first** appearance

### Rules

* If `target` does not appear, return `(0, -1)`

### Examples

```python
supply_report(["medkit", "rope", "medkit"], "medkit") == (2, 0)
supply_report(["rope", "radio", "water"], "medkit") == (0, -1)
supply_report([], "medkit") == (0, -1)
```

### Why this is here

* carryover from Week 1: combining simple ideas into one clear function
* Week 2 skill: looping through a list, tracking count + first match

---

## Stretch Challenge — `priority_load`

```python
def priority_load(items: list[object], urgent_item: object) -> list[object]:
```

Return a **new list** with `urgent_item` added to the **front**.

### Rules

* Do not mutate the original list

### Examples

```python
priority_load(["rope", "radio"], "medkit") == ["medkit", "rope", "radio"]
priority_load([], "flare") == ["flare"]
```

### Stretch idea

In your README, explain why adding something at the front of a list is more expensive
than reading one item by index.

---

## README Requirements

Your `README.md` must include:

### 1) Summary

Write 3–6 lines explaining what the Harbor Rescue Inventory assignment does.

### 2) Approach

Use bullets to explain how each function works.

### 3) Complexity reasoning

Give the time complexity for each function and explain why in 1–3 lines.

Suggested targets:

* `mission_snapshot`
* `cargo_window`
* `first_supply_index`
* `supply_report`
* `priority_load` (stretch)

### 4) Edge-case checklist

Check the ones you tested:

* [ ] empty list
* [ ] one-item list
* [ ] target missing
* [ ] repeated values
* [ ] slice goes past end
* [ ] size is zero or negative
* [ ] original list unchanged in `priority_load`

### 5) Assistance / Sources

List:

* people
* websites
* AI tools
* notes

Also say what kind of help each source gave you.

---

## Submission Checklist

* [ ] `pytest -q` runs
* [ ] all required functions are implemented
* [ ] public functions have type hints
* [ ] public functions have docstrings
* [ ] README includes complexity reasoning
* [ ] README includes edge cases
* [ ] README includes assistance/sources

## Revision Policy

Revisions are accepted only with:

1. a GitHub Revision Request Issue
2. a linked PR

Only the standards named in the request will be re-graded.

Recommended cap: 2 revision requests per student per week.
