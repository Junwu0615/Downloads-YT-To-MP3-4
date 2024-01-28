import json

with open('Downloads-YT-To-MP3-4_clone.json', 'r') as fh:
    now = json.load(fh)

with open('Downloads-YT-To-MP3-4_clone_before.json', 'r') as fh:
    before = json.load(fh)

latest = dict(before)

if 'count_past_to_last_2_weeks_ago' not in latest.keys():
    latest['count_past_to_last_2_weeks_ago'] = 0

if 'uniques_past_to_last_2_weeks_ago' not in latest.keys():
    latest['uniques_past_to_last_2_weeks_ago'] = 0

if 'count_total' not in latest.keys():
    latest['count_total'] = 0

if 'uniques_total' not in latest.keys():
    latest['uniques_total'] = 0 

# 具有唯一性
timestamps = {latest['clones'][i]['timestamp']: i for i in range(len(latest['clones']))}

for i in range(len(now['clones'])):
    # 從最新抓取訊息中的時間戳來判斷該筆是否存在過去的資料當中
    timestamp = now['clones'][i]['timestamp']
    if timestamp in timestamps:
        # 若在裡面，更新資料
        latest['clones'][timestamps[timestamp]] = now['clones'][i]
    else:
        # 不在裡面，新增該筆資料
        latest['clones'].append(now['clones'][i])

if len(latest["clones"]) > 14:
    temp_list = latest["clones"][:-14]
    latest["clones"] = latest["clones"][-14:]

    for i in temp_list:
        latest['count_past_to_last_2_weeks_ago'] += i['count']
        latest['uniques_past_to_last_2_weeks_ago'] += i['uniques']

# 如此一來，根據 17-22 行的過濾判斷，加總的內容也就只局限於最近2周(14天)的內容
# 避免時間拉長後，json 紀錄內容過於龐大
latest['count'] = sum(map(lambda x: int(x['count']), latest['clones']))
latest['uniques'] = sum(map(lambda x: int(x['uniques']), latest['clones']))
latest['count_total'] = latest['count_past_to_last_2_weeks_ago'] + latest['count']
latest['uniques_total'] = latest['uniques_past_to_last_2_weeks_ago'] + latest['uniques']

with open('Downloads-YT-To-MP3-4_clone.json', 'w', encoding='utf-8') as fh:
    json.dump(latest, fh, ensure_ascii=False, indent=4)