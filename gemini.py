import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
try:
    genai.configure(api_key=os.getenv("API_KEY"))
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)
    model = genai.GenerativeModel('gemini-pro')
except Exception:
    print(Exception)


def emailCreater(subject="", description=""):
    try:
        response = model.generate_content(
            f"Wirte a small email on this topic\'{subject}\' and with the description describing: {description}")
        print(response.text)
        return response.text
    except Exception:
        print(Exception)
        return ""


