import json

with open('data/sources.json', encoding='utf-8') as f:
    sources = {s['id']: s for s in json.load(f)}

with open('data/kingdoms.json', encoding='utf-8') as f:
    kingdoms = {k['id']: k for k in json.load(f)}

with open('data/sultans.json', encoding='utf-8') as f:
    sultans = json.load(f)

print(f"Total kingdoms: {len(kingdoms)}")
print(f"Total sultans: {len(sultans)}")
print(f"Total sources: {len(sources)}")

# Check sources
missing_sources = set()
for k in kingdoms.values():
    for sid in k.get('sources_ids', []):
        if sid not in sources:
            missing_sources.add(sid)
print(f"Missing sources in kingdoms: {missing_sources}")

# Check sultans
missing_kingdoms = set()
for s in sultans:
    if s['kingdom_id'] not in kingdoms:
        missing_kingdoms.add(s['kingdom_id'])
print(f"Sultans with missing kingdom_id: {missing_kingdoms}")

# Check coordinates
for k_id, k in kingdoms.items():
    lat = k['coordinates']['lat']
    lng = k['coordinates']['lng']
    assert -11.5 <= lat <= 6.5, f"Lat out of bounds: {k_id} ({lat})"
    assert 94.0 <= lng <= 142.0, f"Lng out of bounds: {k_id} ({lng})"

# Update sultans_count in kingdoms.json to accurately reflect actual count of sultans in sultans.json
sultans_by_k = {}
for s in sultans:
    sultans_by_k[s['kingdom_id']] = sultans_by_k.get(s['kingdom_id'], 0) + 1

for k_id, k in kingdoms.items():
    actual_count = sultans_by_k.get(k_id, 0)
    k['sultans_count'] = actual_count

with open('data/kingdoms.json', 'w', encoding='utf-8') as f:
    json.dump(list(kingdoms.values()), f, ensure_ascii=False, indent=2)

print("Coordinates and sultans counts updated and verified: ALL PASSED!")
