# Exercise 1 – Python + Pytest Foundations

## 🎯 Goal
Practice unit testing in Python using **Pytest** by translating concepts. Target was **80–90% coverage** on a non-trivial module.

---

## 📦 Application Code
- `src/log_parser.py`  
  A simple log parser with methods to:
  - Load logs from CSV (`load`)  
  - Filter logs by status (`filter_by_status`)  
  - Compute average duration (`average_duration`)  
  - Find slowest test (`slowest_test`)  
  - Simulate external service call (`simulate_external_service`)  

---

## 🧪 Tests
- `test/test_log_parser.py`  
  Coverage includes:
  - ✅ Fixtures for temp log file setup/teardown  
  - ✅ Parametrized tests for PASS/FAIL cases  
  - ✅ Exception handling (`FileNotFoundError`, `RuntimeError`, `ValueError`)  
  - ✅ Mocking external service (`pytest-mock`)  
  - ✅ Call verification on mocks  

---

## 📊 Coverage Report
Command:
```bash
pytest --cov=. --cov-report=term-missing
