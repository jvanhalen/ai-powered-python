import requests
from datetime import datetime, timedelta

# Define your API key and base URL
api_key = 'set-your-wakatime-api-key-here'
base_url = 'https://wakatime.com/api/v1/'

def fetch_wakatime_data(endpoint, params=None):
    headers = {
        'Authorization': f'Basic {api_key}',
        'Content-Type': 'application/json'
    }
    
    print(f"Requesting endpoint: {endpoint}")
    print(f"Headers: {headers}")
    print(f"Parameters: {params}")
    
    response = requests.get(f'{base_url}{endpoint}', headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

# Define the start and end dates for the summary
today = datetime.now()
start_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

params = {
    'start': start_date,
    'end': end_date
}

# Fetch summary data
summary_data = fetch_wakatime_data('users/current/summaries', params=params)
if summary_data:
    for day in summary_data['data']:
        date = day['range']['date']
        total_seconds = day['grand_total']['total_seconds']
        print(f"Date: {date}, Total Time Spent: {total_seconds} seconds")
        
        for project in day['projects']:
            project_name = project['name']
            project_time = project['total_seconds']
            print(f"  Project: {project_name}, Time Spent: {project_time} seconds")