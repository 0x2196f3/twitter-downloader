import datetime
import os
import subprocess
import sys
import shutil

from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

bin_path = "/app/twitter_download"
config_path = "/config"
save_path = "/downloads"

retry_times = 3

def update_all():
    os.chdir(bin_path)

    config_file = config_path + '/settings.json'
    dest_file = bin_path + '/settings.json'

    if os.path.exists(config_file):
        shutil.copy(config_file, dest_file)
        print(f"Copied {config_file} to {dest_file}")
    else:
        print(f"Config file {config_file} not found")

    command = ["python3", "./main.py"]

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=bin_path)
    while True:
        line = process.stdout.readline()
        if not line:
            break
        try:
            sys.stdout.write(line.decode())
            sys.stdout.flush()
        except:
            pass

    return_code = process.wait()

    print("return " + str(return_code))

    return return_code

def task():
    for _ in range(retry_times):
        try:
            return_code = update_all()
        except:
            return_code = -1
        
        if return_code == 0:
            break

if __name__ == "__main__":
    interval = os.environ.get('INTERVAL')
    if interval is None or not interval.isdigit():
        interval = 60 * 60 * 6
    else:
        interval = int(interval)

    scheduler.add_job(task, 'interval', seconds=interval, next_run_time=datetime.datetime.now())
    scheduler.start()
