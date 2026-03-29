import json

with open('data/core_500.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'総ノート: {len(data["core_notes"])}')
print(f'スコア範囲: {data["score_range"]["min"]}-{data["score_range"]["max"]} (平均 {data["score_range"]["avg"]:.1f})')
print('\n上位10件:')
for n in data['core_notes'][:10]:
    print(f'  {n["score"]}: {n["name"][:60]}')