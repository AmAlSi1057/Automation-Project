import json
import pandas as pd
from pathlib import Path

# Directory where Playwright test results are stored
results_dir = Path("test-results")
test_data = []

# Iterate through JSON result files
for result_file in results_dir.glob("*.json"):
    with open(result_file, "r") as f:
        data = json.load(f)
        for test in data["tests"]:
            test_data.append({
                "test_name": test["title"],
                "status": test["status"],
                "duration": test["duration"],
                "error": test.get("error", None)
            })

df = pd.DataFrame(test_data)

# Calculate metrics
avg_response_time = df["duration"].mean()
error_rate = (df[df["status"] == "failed"].shape[0] / df.shape[0]) * 100

# Generate HTML report
report = f"""
<html>
  <body>
    <h1>Ad-Bidding Test Report</h1>
    <p>Average Response Time: {avg_response_time:.2f} ms</p>
    <p>Error Rate: {error_rate:.2f}%</p>
  </body>
</html>
"""

with open("report.html", "w") as f:
    f.write(report)
