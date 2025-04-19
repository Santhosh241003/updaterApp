from packages import *

def process_data(file_path):

    session_info_path=file_path+'/session.info'

    df=pd.read_json(file_path+'/eeg_signal.signal')
    with open(session_info_path, 'r') as file:
        content = file.read()
    
    # Try to parse as JSON since the content appears to be in JSON format
    session_data = json.loads(content)
    eeg_data=[]
    for i in df['data']:
        if 'A' in i:
            eeg_data.append(i['A'])
    data={}
    data['Focus']=eeg_data #np.linspace(0,1,100)**2
    data['Cognitive load']=eeg_data #np.linspace(0,1,100)**3
    data['Relaxation']=eeg_data #np.linspace(0,1,100)**5
    data['SessionType']=session_data['sessionTypes']
    data['Duration']=convert_duration(session_data['duration'])
    return data

def convert_duration(duration_str):
    # Split the duration string into hours, minutes, seconds, and microseconds
    parts = duration_str.split(':')
    
    # Handle formats like '0:05:00.000000'
    if len(parts) == 3:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds_parts = parts[2].split('.')
        seconds = int(seconds_parts[0])
    # Handle formats like '05:00.000000'
    elif len(parts) == 2:
        hours = 0
        minutes = int(parts[0])
        seconds_parts = parts[1].split('.')
        seconds = int(seconds_parts[0]) 
    else:
        raise ValueError(f"Unexpected duration format: {duration_str}")
    
    # Calculate total minutes
    total_minutes = hours * 60 + minutes 
    
    # Calculate total hours
    total_hours = hours + minutes / 60 
    
    # Determine which format to return based on the duration
    if total_hours >= 1:
        return f"{total_hours:.2f} hours"
    else:
        return f"{total_minutes:.2f} minutes"
