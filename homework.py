import pandas as pd

sensor_id = "ZONE-A-99"

print(f"first character  = {sensor_id[0]}, last character  = {sensor_id[-1]}")
print("--------")

pipeline = 1245
amount_in_batch = 100

full_batches = pipeline // amount_in_batch
remaining_values = pipeline % amount_in_batch
print(f"Full batches: {full_batches}, Remaining values: {remaining_values}")
print("--------")

raw_data = "0"
integer_data = int(raw_data)

print(bool(raw_data), bool(integer_data))