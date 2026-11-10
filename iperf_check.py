import json
import subprocess

cmd = ["iperf3", "-c", "127.0.0.1", "-u", "-b", "50M", "-t", "3", "-J"]
result = subprocess.run(cmd, capture_output=True, text=True)

data = json.loads(result.stdout)
summary = data["end"]["sum"]

print("Jitter (ms):", summary["jitter_ms"])
print("Lost packets:", summary["lost_packets"], "of", summary["packets"])
print("Loss (%):", summary["lost_percent"])
