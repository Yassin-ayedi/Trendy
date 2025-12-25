import logging
import azure.functions as func
from github_fetch import fetch_github
from stackoverflow_fetch import fetch_stackoverflow
from reddit_fetch import fetch_reddit

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */7 * * * *", arg_name="myTimer", run_on_startup=False, # 0 */6 * * * *
                   use_monitor=False)
def ingestion_pipeline(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info("The timer is past due!")

    stages = [
        ("StackOverflow", fetch_stackoverflow),
        ("GitHub", fetch_github),
        ("Reddit", fetch_reddit),
    ]

    for stage_name, func_call in stages:
        logging.info("="*50)
        logging.info(f"🚀 Starting stage: {stage_name}")
        logging.info("="*50)

        try:
            func_call()
            logging.info(f"Finished stage: {stage_name}")
        except Exception as e:
            logging.error(f"Error in stage {stage_name}: {e}")
