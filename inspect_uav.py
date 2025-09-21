from datasets import load_dataset
ds = load_dataset("sijieaaa/UAVScenes", split="train[:5%]")

print("Number of samples:", len(ds))
print("Column names:", ds.column_names)
print("First sample keys:", list(ds[0].keys()))
# Print a small preview of types
for k in ds[0].keys():
    print(k, type(ds[0][k]))
