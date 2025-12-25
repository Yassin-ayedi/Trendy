# import pandas as pd
# import os
# from utils import upload_to_datalake

# local_folder = "jobs_data"

# for file_name in os.listdir(local_folder):
#     if file_name.endswith(".csv"):
#         file_path = os.path.join(local_folder, file_name)
#         with open(file_path, "rb") as f:
#             file_content = f.read()
#         # Use your function
#         upload_to_datalake(file_content, f"jobs/{file_name}", filesystem_name="bronze")




# NOTE: This is under construction
# Currently uploads data directly to the Bronze layer in the Data Lake.