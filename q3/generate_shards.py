import csv 
from pathlib import Path
import random

random.seed(42)

Path("shards").mkdir(exist_ok=True)

for shard_id in range(8):
    filename = f"shards/shard_{shard_id}.csv"

    with open(filename,"w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames = ["name","email","age"]
        )
        writer.writeheader()

        for i in range(20):
            name = f"user_{shard_id}_{i}"
            email = f"user{i}@example.com"
            age = str(random.randint(18,60))

            if i % (shard_id + 3) == 0:
                email = "invalid-email"

            if i % (shard_id + 4) == 0:
                name = ""

            if i % (shard_id + 5) == 0:
                age = ""

            writer.writerow({
                "name": name,
                "email": email,
                "age": age
        })