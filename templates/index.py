INDEX = """
<!DOCTYPE html>
<html>
<head>
    <title>Quiz</title>
    <style>
        body {
            position: relative;
            min-height: 100vh;
        }

        footer {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            text-align: center;
        }
    </style>
</head>
<body>
    <div>
        <h1>Quiz</h1>

        {% if result is not none %}
            <div>
                <p>Hi {{ username }}! Thank you for playing!</p>
                {% if score == 2 %}
                    <p>Perfect score! You got {{ score }}/4 - 100%!</p>
                {% else %}
                    <p>Your score: {{ score }}/4 - {{percentage}}%</p>
                    <p>Try again to beat the score!</p>
                {% endif %}
            </div>
        {% endif %}
    </div>
    <form action="/submit" method="post">
        <!-- Question about the user's name -->
        <h2>Question 1: What is your name?</h2>
        <input type="text" name="username" value="{% if username is not none %} {{ username }} {% endif %}" required>

        <!-- First question with multiple choice -->
        <h2>Question 2: Which library is currently the most popular for building and training neural networks in Python?</h2>
        <input type="radio" name="question1" value="Scikit"> Scikit-learn<br>
        <input type="radio" name="question1" value="yflow"> TensorFlow + Keras<br>
        <input type="radio" name="question1" value="pytorch"> PyTorch<br>
        <input type="radio" name="question1" value="All"> All are equally popular<br>

        <!-- Second question with multiple choice -->
        <h2>Question 3: Which of the following libraries is primarily used for classical (non-deep) machine learning?</h2>
        <input type="radio" name="question2" value="HGF"> Hugging Face Transformers<br>
        <input type="radio" name="question2" value="Scikit"> Scikit-learn<br>
        <input type="radio" name="question2" value="LChain"> LangChain<br>
        <input type="radio" name="question2" value="FAPI"> FastAPI<br>

        <h2>Question 4: Which popular Python library is commonly used for data manipulation and analysis in the initial stages of an AI project?</h2>
        <input type="radio" name="question3" value="numpy"> NumPy <br>
        <input type="radio" name="question3" value="django"> Django<br>
        <input type="radio" name="question3" value="flask"> Flask<br>
        <input type="radio" name="question3" value="pygame"> Pygame<br>

        <!-- Third question with a text input -->
        <h2>Question 5: Which function from the sklearn (scikit-learn) library is used to split a dataset into training and testing sets?</h2>
        <textarea name="question4" rows="1" cols="50"></textarea>

        <br>
        <input type="submit" value="Submit Answers">

        <!-- User's best score in the top right corner -->
        <div style="position: absolute; top: 10px; right: 10px;">
            <p>Best Score: {{ best_score }}%</p>
        </div>
    </form>

    <!-- Footer with information about the author -->
    <footer>
        Oliwer Urbaniak
    </footer>
</body>
</html>
"""
