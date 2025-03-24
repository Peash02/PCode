from flask import Flask, render_template, request, redirect, url_for, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Quiz questions
quiz_questions = [
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "23"],
        "correct_answer": "8"
    },
    {
        "question": "Which of the following is NOT a Python data type?",
        "options": ["List", "Dictionary", "Tuple", "Array"],
        "correct_answer": "Array"
    },
    {
        "question": "What does the 'len()' function do in Python?",
        "options": ["Returns the length of an object", "Converts to a list", "Calculates logarithm", "Creates a new line"],
        "correct_answer": "Returns the length of an object"
    },
    {
        "question": "Which method is used to add an element to a list in Python?",
        "options": ["insert()", "append()", "extend()", "add()"],
        "correct_answer": "append()"
    },
    {
        "question": "What is the correct way to create a function in Python?",
        "options": ["function myFunc():", "def myFunc():", "create myFunc():", "new myFunc():"],
        "correct_answer": "def myFunc():"
    },
    {
        "question": "Which of the following is used for comments in Python?",
        "options": ["//", "/* */", "#", "<!-- -->"],
        "correct_answer": "#"
    },
    {
        "question": "What will be the output of print(type(5.0))?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'num'>", "<class 'decimal'>"],
        "correct_answer": "<class 'float'>"
    },
    {
        "question": "How do you access the first element of a list named 'my_list'?",
        "options": ["my_list(0)", "my_list[0]", "my_list(1)", "my_list[1]"],
        "correct_answer": "my_list[0]"
    },
    {
        "question": "Which of these is NOT a valid way to create a list in Python?",
        "options": ["[]", "list()", "array()", "list([1, 2, 3])"],
        "correct_answer": "array()"
    },
    {
        "question": "What does the 'import' keyword do in Python?",
        "options": ["Exports functions", "Includes modules", "Creates new objects", "Defines interfaces"],
        "correct_answer": "Includes modules"
    }
]

@app.route('/')
def index():
    # Shuffle questions and select 10
    selected_questions = random.sample(quiz_questions, min(10, len(quiz_questions)))
    
    # Store the selected questions in the session
    # This ensures we know exactly which questions were presented to the user
    session['quiz_questions'] = selected_questions
    
    return render_template('quiz.html', questions=selected_questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    results = []
    
    # Get the questions that were presented to the user from the session
    presented_questions = session.get('quiz_questions', [])
    
    # Process each answer
    for i in range(len(presented_questions)):
        question_key = f'question_{i}'
        
        if question_key in request.form:
            user_answer = request.form[question_key]
            correct_answer = presented_questions[i]['correct_answer']
            
            is_correct = user_answer == correct_answer
            if is_correct:
                score += 1
            
            results.append({
                'question': presented_questions[i]['question'],
                'user_answer': user_answer,
                'correct_answer': correct_answer,
                'is_correct': is_correct
            })
    
    return render_template('results.html', results=results, score=score, total=len(results))

if __name__ == '__main__':
    app.run(debug=True)
