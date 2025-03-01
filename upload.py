import google.generativeai as genai
import os

# ✅ Set API Key
API_KEY = "AIzaSyAKwRbZ6AHUo73bU37au8gJbs82R2nlSoM"  # Replace with your API Key
genai.configure(api_key=API_KEY)

# ✅ File to Upload
file_path = "fine_tune_data.jsonl"  # Ensure this file exists in your directory

try:
    # ✅ Upload the fine-tuning data
    uploaded_file = genai.upload_file(path=file_path, mime_type="application/json")

    # ✅ Print the File ID (VERY IMPORTANT for fine-tuning)
    print(f"✅ File uploaded successfully! File ID: {uploaded_file.name}")

except Exception as e:
    print(f"❌ Error during upload: {e}")
