from datetime import datetime

def date_command():
    today = datetime.now()
    date = today.strftime("%d/%m/%Y")

    print("="*35)
    print("Current Date:", date)
    print("="*35)