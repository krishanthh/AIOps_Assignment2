import csv 
import os 
import re
import time

shard_id  = int(os.environ["JOB_COMPLETION_INDEX"])

filename = f"/data/shard_{shard_id}.csv"

email_pattern = re.compile(r"^[^S\s]+a[^S\s]+\.[^S\s]+$")

invalid = 0

with open(filename, newline = "") as f:
    reader = csv.DictReader(f)

    for row in reader:
        if not row["name"]:
            invalid += 1
            continue

        if not email_pattern.match(row["email"]):
            invalid += 1
            continue

        if not row["age"]:
            invalid += 1

print(f"Shard_{shard_id} invalid_rows = {invalid}")

time.sleep(20)