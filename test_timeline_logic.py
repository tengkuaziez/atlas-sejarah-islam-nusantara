import json

with open('data/kingdoms.json', encoding='utf-8') as f:
    kingdoms = json.load(f)

with open('data/sultans.json', encoding='utf-8') as f:
    sultans = json.load(f)

def get_status(k, year):
    if year < k['year_founded']:
        return 'not_yet_founded'
    if k.get('year_ended') and year > k['year_ended']:
        if k.get('status_timeline_type') == 'integrated':
            return 'integrated'
        elif k.get('status_timeline_type') == 'cultural_continuation':
            return 'cultural_continuation'
        return 'ended'
    if k.get('golden_age'):
        if k['golden_age']['start_year'] <= year <= k['golden_age']['end_year']:
            return 'golden_age'
    if k.get('year_ended') and (k['year_ended'] - year <= 25) and k['year_ended'] > year:
        return 'declining'
    return 'active'

test_years = [1200, 1270, 1350, 1475, 1526, 1580, 1625, 1670, 1755, 1825, 1900, 1945]

print("Simulating chronologic states across centuries:")
for yr in test_years:
    active = 0
    golden = 0
    cultural = 0
    ended = 0
    not_founded = 0
    for k in kingdoms:
        st = get_status(k, yr)
        if st in ('active', 'golden_age', 'declining'):
            active += 1
        if st == 'golden_age':
            golden += 1
        if st in ('cultural_continuation', 'integrated'):
            cultural += 1
        if st == 'ended':
            ended += 1
        if st == 'not_yet_founded':
            not_founded += 1
    print(f"Year {yr} M: Active/Flourishing={active} (Golden Age={golden}), Cultural/Integrated={cultural}, Ended={ended}, Not Founded={not_founded}")

print("\nChecking sultan reign matching for year 1625 M:")
sultans_1625 = [s for s in sultans if s.get('reign_start') and s.get('reign_end') and s['reign_start'] <= 1625 <= s['reign_end']]
print(f"Found {len(sultans_1625)} sultans reigning in 1625 M, including:")
for s in sultans_1625[:5]:
    print(f" - {s['name']} ({s['reign_display']}) in {s['kingdom_id']}")
