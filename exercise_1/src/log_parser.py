import csv
import random
from typing import List, Dict


class LogParser:
    def __init__(self, logfile: str):
        self.logfile = logfile
        self.logs: List[Dict] = []

    def load(self) -> List[Dict]:
        """Load logs from a CSV file with columns: test_name,status,duration"""
        try:
            with open(self.logfile, newline="") as f:
                reader = csv.DictReader(f)
                self.logs = [row for row in reader]
            return self.logs
        except FileNotFoundError:
            raise FileNotFoundError(f"Log file not found.")

    def filter_by_status(self, status: str) -> List[Dict]:
        """Filter logs by test status (PASS/FAIL)"""
        if not self.logs:
            raise RuntimeError("Logs not loaded. Call load() first.")
        return [row for row in self.logs if row["status"].upper() == status.upper()]

    def average_duration(self) -> float:
        """Return the average test duration"""
        if not self.logs:
            return 0.0
        durations = [float(row["duration"]) for row in self.logs]
        return sum(durations) / len(durations)

    def slowest_test(self) -> Dict:
        """Return the log entry with max duration"""
        if not self.logs:
            return {}
        return max(self.logs, key=lambda x: float(x["duration"]))

    def simulate_external_service(self, test_name: str) -> str:
        """
        Mock method: imagine calling an external API
        Returns a random status.
        """
        if not test_name:
            raise ValueError("Test name must not be empty")
        return random.choice(["PASS", "FAIL"])
