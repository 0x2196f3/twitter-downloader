import os
import random
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

import subprocess
import time
import shutil


def empty_str(string) -> bool:
    return string is None or str.strip(string) == ""


def read_lines(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        result = file.readlines()

    if result is None:
        raise FileNotFoundError()

    return result


def copy_file(src_file_path: str, dst_folder_path: str):
    shutil.copy(src_file_path, dst_folder_path)


scheduler = BlockingScheduler()

bin_path = "/app"
config_path = "/config"
save_path = "/downloads"

cmd = bin_path + "/twitter-media-downloader twmd -u $USER_NAME -o " + save_path + " -a -U -L\n"


def update_all(repeat=False) -> None:
    os.chdir(bin_path)

    users = read_lines(config_path + "/users.txt")

    copy_file(config_path + "/twmd_cookies.json", bin_path + "/twmd_cookies.json")

    for _ in range(10 if repeat else 3):
        random.shuffle(users)
        time.sleep(1)
        for user in users[:]:
            if empty_str(user):
                continue
            time.sleep(1)
            command = cmd.replace("$USER_NAME", user.replace("\n", ""))
            print(command)
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print(result.stdout)
            print(result.stderr)

            if result.returncode == 0:
                users.remove(user)
            


def main() -> None:
    update_all(True)
    interval = os.environ.get('INTERVAL')
    if interval is None or not interval.isdigit():
        interval = 60*60*12
    else:
        interval = int(interval)

    scheduler.add_job(update_all, 'interval', seconds=interval)
    scheduler.start()


if __name__ == "__main__":
    main()
