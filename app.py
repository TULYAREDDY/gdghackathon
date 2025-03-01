from flask import Flask, render_template, request
import finetune  # Import your finetune.py logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['question']
    answer = finetune.ask_financial_bot(user_input)  # Call the finetune.py function
    return render_template('index.html', question=user_input, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)