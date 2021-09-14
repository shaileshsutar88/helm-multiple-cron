from datetime import datetime
import time

print("Starting the job: ", datetime.now());
print("Running the cron");
time.sleep(15)
print("Stopping the job: ", datetime.now());
