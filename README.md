# Week 2 — Harbor Rescue Inventory

## Summary

The Harbor Rescue Inventory assignment implements five functions that simulate managing a cargo list for a rescue mission. The functions cover core list operations: inspecting endpoints, slicing a window of items, searching for a target, generating a combined count-and-index report, and prepending a high-priority item. Together they build familiarity with Python list indexing, iteration, and immutability. Every function handles edge cases such as empty lists, missing targets, and out-of-range parameters without raising errors.

---

## Approach

- **`mission_snapshot`**: Checks if the list is empty and returns `(None, None)`. Otherwise returns `(items[0], items[-1])` using direct index access — no loop needed.
- **`cargo_window`**: Validates that `start` is in range and `size > 0`, then returns `items[start : start+size]`. Python slicing naturally handles cases where the window extends past the end.
- **`first_supply_index`**: Iterates with `enumerate()`, returning the index immediately on the first match. Returns `-1` if the loop completes without finding the target. Avoids `list.index()` as required.
- **`supply_report`**: Single pass with `enumerate()`. Tracks a running count and records `first_index` only on the first match (when `first_index` is still `-1`). Returns `(0, -1)` if no match is found.
- **`priority_load` (stretch)**: Returns `[urgent_item] + items`, which constructs a brand-new list. The original list is never touched, satisfying the no-mutation requirement.

---

## Complexity Reasoning

| Function | Time Complexity | Why |
|---|---|---|
| `mission_snapshot` | O(1) | Directly accesses first and last index — no iteration needed. |
| `cargo_window` | O(k) | Slicing copies up to k elements (the window size), not the whole list. |
| `first_supply_index` | O(n) | Worst case scans every element once before finding target or reaching end. |
| `supply_report` | O(n) | Single pass through all items to count and record first index. |
| `priority_load` (stretch) | O(n) | Creating a new list copies all n existing items plus the new one. |

---

## Edge-Case Checklist

- [ ] Empty list
- [ ] One-item list
- [ ] Target missing
- [ ] Repeated values
- [ ] Slice goes past end
- [ ] `size` is zero
- [ ] `size` is negative
- [ ] Original list unchanged in `priority_load`

---

## Assistance / Sources

- **Person / tool / website:** Claude (claude.ai)
  - **Help received:** Explained the approach and complexity for each function; reviewed edge cases.
- **Person / tool / website:** Python Docs — docs.python.org
  - **Help received:** Reference for list slicing behaviour and `enumerate()` usage.