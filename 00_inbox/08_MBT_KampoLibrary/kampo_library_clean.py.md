import json

with open("mbt_kampo_library_final_array.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("mbt_kampo_library_clean.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)