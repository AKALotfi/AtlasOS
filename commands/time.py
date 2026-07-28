from datetime import datetime

def time_command():
    today = datetime.now()
    hour = today.strftime("%H:%M:%S")

    print("="*35)
    print("Current Hour:", hour)
    print("="*35)
