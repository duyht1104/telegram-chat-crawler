# Telegram chat crawl in real time

- Create Telegram Application in my.telegram.org
- Fill in your chat name
- Enjoy

```
import os
import pandas as pd
import random
from faker import Faker
import datetime
import json
```
- Faker data

```
faker = Faker()

data = []

for _ in range(1000):
    rand_sec = random.randint(0, 60*60*24)
    rand_day = random.randint(-1000,1000)
    time = datetime.datetime.now() + datetime.timedelta(seconds=rand_sec) + datetime.timedelta(days=rand_day)
    rand_num = range(random.randint(1,4))

    data.append({
        "date": time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-4],
        "news": [faker.sentence() for _ in rand_num],
        "sentiments": [faker.random_element(elements = ("Positive", "Neutral", "Negative")) for _ in rand_num],
        "title": faker.sentence(),
        "url": faker.url()
    })
```

- export data
```
def export_data(data, period):
    
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    if period == "year_month":
        df["year_month"] = df["date"].dt.strftime("%Y-%m")
    if period == "year_month_week":
        df["year_month_week"] = df["date"].dt.strftime("%Y-%m-") + "W" + df["date"].dt.strftime("%V") 
    if period == "year_month_day":
        df["year_month_day"] = df["date"].dt.strftime("%Y-%m-%d")
    if period != "year_month" and period != "year_month_week" and period != "year_month_day":
        return "select correct period"
    df = df.sort_values(["date"], ascending=False).reset_index(drop=True)
    df = df.explode(["news", "sentiments"])
    df = df.groupby(by = period).agg({"title": list, "url": list, "news": list, "sentiments": list})

    df = df.reset_index()
    df.head()

    for index, row in df.iterrows():
        input_period = row[period]
        folder_path = f"D:\copy_trade\\testfolder\{input_period}"
        os.makedirs(folder_path, exist_ok=True)
        data = {
            row[period]: row[period],
            "title": row["title"],
            "url": row["url"],
            "news": row["news"],
            "sentiments": row["sentiments"]
        }
        with open(os.path.join(folder_path, 'data.json'), 'w') as f:
            json.dump(data, f)
```
