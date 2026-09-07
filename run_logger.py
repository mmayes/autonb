import os
from datetime import datetime

def log_run_to_file(run_name, run_type, status, settings):
    """
    Logs the settings of a run to run_history.txt in the workspace directory.
    """
    log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'run_history.txt')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_file_path, "a") as f:
        f.write("=" * 60 + "\n")
        f.write(f"Timestamp:   {timestamp}\n")
        f.write(f"Run Name:    {run_name}\n")
        f.write(f"Run Type:    {run_type}\n")
        f.write(f"Status:      {status}\n")
        f.write("-" * 60 + "\n")
        f.write("Settings:\n")
        for key, value in settings.items():
            f.write(f"  {key}: {value}\n")
        f.write("=" * 60 + "\n\n")
