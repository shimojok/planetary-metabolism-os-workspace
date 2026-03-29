import json

input_file = "mbt_kampo_library_master_v2.44.json"
output_file = "mbt_kampo_library_array.json"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

root = data["mbt_kampo_library"]

meta = {
    "version": root["version"],
    "last_updated": root["last_updated"],
    "total_formulas": root["total_formulas"],
    "fully_defined": root["fully_defined"],
    "classification_source": root["classification_source"],
    "mbt55_version": root["mbt55_version"]
}

formulas_list = []
for formula_id, formula_data in root["formulas"].items():
    formula_data["id"] = formula_id
    formulas_list.append(formula_data)

output_data = {**meta, "formulas": formulas_list}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"✅ 変換完了: {output_file}")
print(f"   → 処方数: {len(formulas_list)}")