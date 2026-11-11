import json
import subprocess
import sys
import time

rate = sys.argv[1] if len(sys.argv) > 1 else "50M"

cmd = ["iperf3", "-c", "127.0.0.1", "-u", "-b", rate, "-t", "3", "-J"]

losses = []
jitters = []
for run in range(1, 6):
    result = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(result.stdout)
    if "error" in data:
        print("Run", run, "ERROR:", data["error"])
        continue
    summary = data["end"]["sum"]
    losses.append(summary["lost_percent"])
    jitters.append(summary["jitter_ms"])
    print("Run", run, "- Loss (%):", summary["lost_percent"], "Jitter (ms):", summary["jitter_ms"])
    time.sleep(1)

print("Max loss (%):", max(losses))
print("Avg jitter (ms):", round(sum(jitters) / len(jitters), 4))
