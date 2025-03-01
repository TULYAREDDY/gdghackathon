import google.generativeai as genai

# Hardcode API Key (replace with your actual key)
API_KEY = "AIzaSyAKwRbZ6AHUo73bU37au8gJbs82R2nlSoM"  # Replace with your actual API key

# Configure the API
genai.configure(api_key=API_KEY)

# Initialize Model
model = genai.GenerativeModel(
    "gemini-1.5-pro-latest",
    system_instruction="You are a financial assistant. Answer only finance-related questions."
)

# Function to check if the question is finance-related
def is_finance_question(question):
    finance_keywords = [
        "investment", "stocks", "bonds", "mutual fund", "inflation", "finance",
        "banking", "trading", "portfolio", "wealth", "loans", "insurance", "crypto",
        "dividends", "interest rates", "tax", "budget", "savings"
    ]
    return any(keyword in question.lower() for keyword in finance_keywords)

# Function to ask the financial assistant
def ask_financial_bot(question):
    if is_finance_question(question):
        # Try removing file ID directly from tools, it might be handled separately by the system
        response = model.generate_content([question], stream=False)  # Direct question input only
        return response.text
    else:
        return "❌ Sorry, I can only answer finance-related questions."

# Test Queries
print(ask_financial_bot("Explain stocks"))  # Should answer using file content  
print(ask_financial_bot("what is milk"))  # Should answer using file  
print(ask_financial_bot("Who is the President of India?"))  # Should reject  
print(ask_financial_bot("Tell me a joke."))  # Should reject
