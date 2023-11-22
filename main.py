from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

import subprocess
import time


def empty_str(string) -> bool:
    return string is None or str.strip(string) == ""


def read_lines(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        result = file.readlines()

    if result is None:
        raise FileNotFoundError()

    return result


scheduler = BlockingScheduler()

bin_path = "/app/twitter-media-downloader"
user_path = "/config/users.txt"
save_path = "/downloads"

cmd = bin_path + " twmd -u $USER_NAME -o " + save_path + " -a -U\n"


def update_all(repeat=False) -> None:
    users = read_lines(user_path)

    for _ in range(10 if repeat else 3):
        time.sleep(1)
        for user in users:
            if empty_str(user):
                continue
            time.sleep(1)
            command = "(" + cmd.replace("$USER_NAME", user.replace("\n", "")) + ") > /dev/null"
            print(command)
            subprocess.call(command, shell=True)


def main() -> None:
    update_all(True)
    scheduler.add_job(update_all, 'interval', seconds=60 * 60 * 12, next_run_time=datetime.now())
    scheduler.start()


if __name__ == "__main__":
    main()
