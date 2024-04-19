import os
import datetime
from pathlib import Path
import random
import decimal
import json

THIS_SCRIT_DIR = Path(__file__).resolve().parent
source_data_files_path = f"{THIS_SCRIT_DIR}/source_data_files"

print(f"THIS_SCRIT_DIR {THIS_SCRIT_DIR}")
print(f"source_data_files_path {source_data_files_path}")

folder_paths_list = []


def daterange(start_date_input, end_date_input):
    for n in range(int((end_date_input - start_date_input).days)):
        yield start_date_input + datetime.timedelta(n)


def create_data_folders():
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2020, 1, 16)

    for single_date in daterange(start_date, end_date):
        date_folder_name = single_date.strftime("%Y-%m-%d")
        folder_path = f"{source_data_files_path}/{date_folder_name}"
        folder_paths_list.append((folder_path, date_folder_name))

        print(f"Creating (if not exists) source_data_files_path {folder_path}")
        Path(f"{folder_path}").mkdir(parents=True, exist_ok=True)


FROM_TO_CURRENCY_LIST = [("USD", "GBP"), ("USD", "INR"), ("USD", "JPY")]


def generate_trade_feeds_forex(folder_paths_list_val: list[str]):
    for folder_path, date_folder_name in folder_paths_list_val:
        # 100 files per day and each file having 100 feeds
        for a_date_trade_feed_file_no in range(1, 100):
            a_date_trade_feed_filename = f"{folder_path}/000_{a_date_trade_feed_file_no}.txt"
            with open(a_date_trade_feed_filename, 'w') as fp:
                for a_trade_feed_ctr in range(1, 100):
                    from_currency, to_currency = FROM_TO_CURRENCY_LIST[
                        random.randint(1, len(FROM_TO_CURRENCY_LIST) - 1)]
                    a_trade_feed = {
                        "customer_id": str(random.randint(1, 100)),
                        "trade_date": date_folder_name,
                        "trade_value": str(decimal.Decimal(random.randrange(155, 389)) / 100),
                        "from_currency": from_currency,
                        "to_currency": to_currency,
                    }
                    fp.write(json.dumps(a_trade_feed) + "\n")


create_data_folders()
generate_trade_feeds_forex(folder_paths_list)
