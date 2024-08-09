<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Movie Recommender System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 0 20px;
        }
        h1 {
            color: #5c85d6;
        }
        h2, h3 {
            color: #333;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        a {
            color: #5c85d6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Movie Recommender System</h1>

        <h2>Overview</h2>
        <p>This project is a Movie Recommendation System built using data from Kaggle. The system recommends movies similar to a user-specified movie based on various factors. The project also includes a user-friendly interface for seamless interaction.</p>

        <h3>Project Link</h3>
        <p>GitHub Repository: <a href="https://github.com/maushamkumar/Recommender-System/tree/main/Movie%20Recommender%20System" target="_blank">Movie Recommender System</a></p>

        <h2>Features</h2>
        <ul>
            <li><strong>Data Source:</strong> The movie dataset used in this project is sourced from Kaggle.</li>
            <li><strong>Exploratory Data Analysis (EDA):</strong> Conducted EDA to understand the data patterns and prepare the data for modeling.</li>
            <li><strong>Recommendation Algorithm:</strong> Implemented the Cosine Similarity algorithm to suggest five movies similar to the one provided by the user.</li>
            <li><strong>User Interface:</strong> Built with Streamlit, allowing users to input a movie name and get instant movie recommendations.</li>
        </ul>

        <h2>How It Works</h2>
        <ol>
            <li><strong>Data Ingestion:</strong> The dataset is imported and cleaned for further processing.</li>
            <li><strong>EDA:</strong> Various techniques are applied to understand the distribution, relationships, and patterns within the data.</li>
            <li><strong>Feature Selection:</strong> Relevant features are selected for the recommendation model.</li>
            <li><strong>Cosine Similarity:</strong> The system calculates the cosine similarity between movies to find and recommend similar movies.</li>
            <li><strong>Streamlit UI:</strong> A user interface where users can input a movie title and get a list of five recommended movies based on the input.</li>
        </ol>

        <h2>Installation and Usage</h2>
        <ol>
            <li>Clone the repository:
                <pre><code>git clone https://github.com/maushamkumar/Recommender-System</code></pre>
            </li>
            <li>Navigate to the project directory:
                <pre><code>cd Recommender-System/Movie Recommender System</code></pre>
            </li>
            <li>Install the required packages:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li>Run the Streamlit app:
                <pre><code>streamlit run app.py</code></pre>
            </li>
            <li>Enter a movie name in the input box, and the system will recommend five similar movies.</li>
        </ol>

        <h2>Conclusion</h2>
        <p>This Movie Recommender System efficiently suggests movies based on user input, leveraging data from Kaggle and employing the Cosine Similarity algorithm. The project also features an intuitive UI built with Streamlit for ease of use.</p>
    </div>
</body>
</html>
