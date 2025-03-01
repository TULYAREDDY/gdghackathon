import google.generativeai as genai

# ✅ Set API Key
API_KEY = "AIzaSyAKwRbZ6AHUo73bU37au8gJbs82R2nlSoM"
genai.configure(api_key=API_KEY)

# ✅ Initialize Model
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# ✅ First API Call (Mutual Funds)
try:
    response = model.generate_content("Explain mutual funds in simple terms.")
    print("\n✅ Mutual Funds Response:")
    print(response.text)  # Checking the output
except Exception as e:
    print(f"❌ API ERROR: {e}")

# ✅ Next API Calls (Ensure No Exit)
questions = [
    "Should I invest in gold ETFs?",
    "Tell me a joke."  # Should be rejected
]

for question in questions:
    try:
        print(f"\n💬 Asking: {question}")
        response = model.generate_content(question)

        if response is None:
            print("⚠️ No response received.")
        elif hasattr(response, 'text'):
            print(f"🤖 Answer: {response.text}")
        else:
            print("⚠️ Unexpected response format.")

    except Exception as e:
        print(f"❌ API ERROR: {e}")

# ✅ Prevent Auto-Exit
input("\nPress ENTER to exit...")
