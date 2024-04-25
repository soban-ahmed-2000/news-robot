import os
import logging

from RPA.Robocorp.WorkItems import WorkItems

from la_times.la_times import LATimes

OUTPUT_DIR = os.path.join(os.getcwd(), f"output/")
try:
    os.mkdir(OUTPUT_DIR)
except FileExistsError:
    pass

# Set up logging
log_file = os.path.join(OUTPUT_DIR, 'la_times.log')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler(log_file),
                        logging.StreamHandler()
                    ])

# Check if logging configuration is successful
if not logging.getLogger().handlers:
    raise RuntimeError("Logging configuration failed. No handlers found.")


if os.getenv("ROBOCORP_WORKER_ALIAS"):
    work_items = WorkItems()
    search_phrase = work_items.get_work_item_variable("PHRASE")
    category = work_items.get_work_item_variable("CATEGORY")
else:
    search_phrase = "pakistan"
    category = "World & Nation"


def task():
    try:
        logging.info("Initializing LA Times automation task.")
        la_times = LATimes()
        la_times.open_browser('https://www.latimes.com/')
        logging.info("Opened browser successfully.")
        la_times.search_phrase(search_phrase)
        logging.info("Search phrase entered successfully.")
        la_times.sort_by_latest()
        logging.info("Results sorted by latest.")
        la_times.select_category(category)
        logging.info("Category 'World & Nation' selected.")
        la_times.download_news_data_excel()
        logging.info("News data downloaded and saved to Excel.")
        la_times.browser.close_all_browsers()
        logging.info("Closed all browser windows.")
        logging.info("LA Times automation task completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during LA Times automation task: {e}", exc_info=True)


if __name__ == "__main__":
    task()
