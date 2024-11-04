import requests
import json


api_url = "https://api.gemini.com/v1/resume/extract"  
api_key = "your_gemini_api_key"  

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Step 2: Prepare the Resume File
file_path = "resume.pdf"  

# Step 3: Send the File via a POST Request
with open(file_path, "rb") as file:
    files = {"file": file}
    response = requests.post(api_url, headers=headers, files=files)

# Step 4: Handle the Response
if response.status_code == 200:
    resume_data = response.json()
    print("Resume Data Extracted:", resume_data)

    # Step 5: Save the Extracted Data as JSON
    with open("resume_data.json", "w") as json_file:
        json.dump(resume_data, json_file, indent=4)
        print("Data successfully stored in resume_data.json")
else:
    print(f"Failed to extract data. Status Code: {response.status_code}")
    print("Error:", response.text)