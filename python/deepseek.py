import requests
import json

API_URL = "https://api.deepseek.com/v1"
API_KEY = "sk-53bb8b20232944c3a0e3aa8b96dcf1d2"  # Make sure this is valid

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": "မင်္ဂလာပါ၊ DeepSeek API က ဘာတွေလုပ်ပေးနိုင်လဲ?"}
    ],
    "temperature": 0.7
}

try:
    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()  # Raises an exception for HTTP errors
    result = response.json()
    
    print("Full API Response:", json.dumps(result, indent=2))  # Debug print
    
    if "choices" in result:
        print("\nDeepSeek AI မှ အဖြေ:")
        print(result["choices"][0]["message"]["content"])
    else:
        print("Error: Unexpected response format. Missing 'choices' key.")
        if "error" in result:
            print("API Error:", result["error"])

except requests.exceptions.RequestException as e:
    print("Request Failed:", e)
except Exception as e:
    print("Error:", e)