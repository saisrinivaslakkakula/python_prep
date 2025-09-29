import argparse
import inspect
import sys
import time
import traceback
import exercise_2.test.test_calculator as test


def get_all_functions_in_module(module):
    functions = []
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj) and name.startswith("test_"):
            functions.append(obj)
    return functions


def run_test(fn):
    result = {"test_name": fn.__name__}
    start = time.time()
    try:
        fn()
        result["status"] = "PASS"
    except AssertionError as e:
        result["status"] = "FAIL"
        result["error"] = str(e)
    except Exception as e:
        result["status"] = "ERROR"
        result["error"] = str(e)
        result["traceback"] = traceback.format_exc()
    finally:
        result["duration"] = time.time() - start
    return result


def run_parameterized_test(fn, mark):
    arg_names = [x.strip() for x in mark.args[0].split(",")]
    param_sets = mark.args[1]
    results = []

    for params in param_sets:
        case_name = f"{fn.__name__}[{','.join(map(str, params))}]"
        result = {"test_name": case_name}
        start = time.time()
        try:
            fn(*params)
            result["status"] = "PASS"
        except AssertionError as e:
            result["status"] = "FAIL"
            result["error"] = str(e)
        except Exception as e:
            result["status"] = "ERROR"
            result["error"] = str(e)
            result["traceback"] = traceback.format_exc()
        finally:
            result["duration"] = time.time() - start
        results.append(result)

    return results


def run_all_tests():
    print("Running test cases...")
    all_results = []
    all_tests = get_all_functions_in_module(test)

    for test_function in all_tests:
        param_marks = [m for m in getattr(test_function, "pytestmark", []) if m.name == "parametrize"]

        if param_marks:
            for mark in param_marks:
                all_results.extend(run_parameterized_test(test_function, mark))
        else:
            all_results.append(run_test(test_function))

    return all_results


def run_tests_with_params():
    parser = argparse.ArgumentParser(prog="test runner")
    parser.add_argument("--r", help="generate report (yes/no)")
    args = parser.parse_args()

    results = run_all_tests()

    # Print report
    print("\n========== TEST REPORT ==========")
    passed = [r for r in results if r["status"] == "PASS"]
    failed = [r for r in results if r["status"] != "PASS"]

    for r in passed:
        print(f"✅ {r['test_name']} ({r['duration']:.4f}s)")
    for r in failed:
        print(f"❌ {r['test_name']} ({r['duration']:.4f}s) -> {r.get('error')}")
        if "traceback" in r:
            print(r["traceback"])

    print("\n=== SUMMARY ===")
    print(f"Total: {len(results)}, Passed: {len(passed)}, Failed: {len(failed)}")
    print(f"Total Duration: {sum(r['duration'] for r in results):.4f}s")

    if args.r == "yes":
        with open("test_report.log", "w") as f:
            for r in results:
                f.write(f"{r['status']} - {r['test_name']} - {r['duration']:.4f}s\n")
                if "error" in r:
                    f.write(f"   Error: {r['error']}\n")
        print("Report written to test_report.log")

    sys.exit(0 if len(failed) == 0 else 1)


if __name__ == "__main__":
    run_tests_with_params()
