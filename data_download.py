import os
import time
import requests
import pandas as pd
from datetime import datetime, timedelta
import argparse

def generate_date_range(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    present_date = start
    date_list = []

    while present_date <= end:
        date_list.append(present_date.strftime("%Y-%m-%d"))
        #"%Y-%m-%dT%HH:%MM:%SZ"
        present_date += timedelta(days=1)
        #print(date_list)

    return date_list

def get_data(url, business_day, api_key):
    params = {'app_name': 'selforder', 'api_key': api_key}
    data = {
        "selector": {
            "businessDay": business_day
        },
        "options": {
            "skip": "0",
            "limit": "998"
        }
    }

    try:
        print(f"API call triggered time in ISO format : {datetime.now().isoformat()}")
        response = requests.post(url=url, params=params, json=data)
        response.raise_for_status()
        return response.json()['data']
    except Exception as e:
        print(f"Error fetching data for {business_day}: {e}")
        return None


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Extract data from API and save as CSV")
    parser.add_argument('-a', '--apikey', type=str, required=True, help="API key for authentication")
    parser.add_argument('-s', '--startdate', type=str, required=True, help="Start date in YYYY-MM-DD format")
    parser.add_argument('-e', '--enddate', type=str, required=True, help="End date in YYYY-MM-DD format")
    parser.add_argument('-t', '--tab', type=str, required=True, help="Table name to fetch data from")

    args = parser.parse_args()

    host = 'https://api.mrwinston.com/api'
    start_date = args.startdate
    end_date = args.enddate
    tab = args.tab
    api_key = args.apikey

    dates = generate_date_range(start_date, end_date)

    normal_dates = []
    missing_dates = []
    
    start = time.time() 

    for date in dates:
        file_date = date.replace('-', '')
        folder = f"{tab}/{file_date[:6]}"
        
        if not os.path.exists(os.path.join(os.getcwd(), folder)):
            os.mkdir(folder)
            
        print(f"Getting data for business day {date}")
        #data = None
        
        data = get_data(url=f"{host}/{tab}", business_day=date, api_key=api_key)
        
        if data is not None:
            df = pd.DataFrame(data)
            filename = f"{folder}/{tab}_{file_date}_bday.csv"
            df.to_csv(filename, index=False)
            normal_dates.append(date)
            print(f"Data for {date} saved to {filename}")
        else:
            missing_dates.append(date)

    print(f"\nTotal dates attempted: {len(dates)}")
    print(f"Successful dates: {len(normal_dates)}")
    print(f"Failed dates: {len(missing_dates)}")

    success = pd.DataFrame(normal_dates, columns=['success'])
    success.to_csv(f"{tab}_{start_date.replace('-', '')}_{end_date.replace('-', '')}_normal_dates.csv", index=False)

    failed = pd.DataFrame(missing_dates, columns=['failed'])
    failed.to_csv(f"{tab}_{start_date.replace('-', '')}_{end_date.replace('-', '')}_missing_dates.csv", index=False)
    end = time.time() 
    print(f"Time taken to get data: {end - start} seconds")


   
