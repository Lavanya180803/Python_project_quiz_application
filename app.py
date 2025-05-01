from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session management

# Computer Applications Questions
all_questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Control Processing Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which one is an Operating System?",
        "options": ["Python", "Linux", "HTML", "MySQL"],
        "answer": "Linux"
    },
    {
        "question": "What is the full form of HTML?",
        "options": ["Hyper Trainer Marking Language", "Hyper Text Markup Language", "Hyper Text Marketing Language", "Hyper Tool Markup Language"],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "Which application is used to create spreadsheets?",
        "options": ["MS Word", "MS Excel", "PowerPoint", "Notepad"],
        "answer": "MS Excel"
    },
    {
        "question": "What is RAM used for?",
        "options": ["Permanent storage", "Temporary memory", "File compression", "Email service"],
        "answer": "Temporary memory"
    },
    {
        "question": "Which device is used for input?",
        "options": ["Monitor", "Printer", "Keyboard", "Speaker"],
        "answer": "Keyboard"
    }
]

@app.route('/')
def start_quiz():
    # Randomize questions and reset session
    questions = random.sample(all_questions, len(all_questions))
    session['questions'] = questions
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit_quiz():
    questions = session.get('questions', [])
    user_answers = []
    score = 0

    for i, q in enumerate(questions):
        selected = request.form.get(f'q{i}')
        correct = q['answer']
        user_answers.append({
            'question': q['question'],
            'selected': selected,
            'correct': correct,
            'is_correct': selected == correct
        })
        if selected == correct:
            score += 1

    percentage = round((score / len(questions)) * 100, 2)
    return render_template('result.html', user_answers=user_answers, score=score, total=len(questions), percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True)
