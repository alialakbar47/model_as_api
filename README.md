# Sentiment Analysis API

This Flask application provides a simple API endpoint for performing sentiment analysis on text using the `facebook/bart-large-mnli` pre-trained model from the `transformers` library.

## Prerequisites

Before running the application, ensure you have Python installed on your system. You will also need to install the required Python packages.

## Installation

1.  **Clone the repository (if you have the code in one):**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
    This command will install Flask, the `transformers` library, and PyTorch (which `transformers` relies on).

3.  **Download the sentiment analysis model:**
    Before running the Flask application, you need to download the `facebook/bart-large-mnli` model. Run the provided `download.py` script:
    ```bash
    python download.py
    ```
    This script will download the necessary model files.

## Running the Application

1.  **Navigate to the directory containing the Python scripts (`main.py` and `download.py`) in your terminal.**

2.  **Run the Flask development server:**
    ```bash
    python main.py
    ```
    This will start the server, and you should see output similar to:
    ```
    * Serving Flask app 'main'
    * Debug mode: off
    * Running on all addresses (0.0.0.0)
    * Running on [http://127.0.0.1:5000](https://www.google.com/search?q=http://127.0.0.1:5000)
    ```
    The application will be accessible at `http://0.0.0.0:5000`.

## Using the Sentiment Analysis Endpoint

You can send a POST request to the `/sentiment` endpoint with a JSON payload containing the text you want to analyze.

**Request:**

* **Method:** `POST`
* **Endpoint:** `/sentiment`
* **Headers:** `Content-Type: application/json`
* **Body (JSON):**
    ```json
    {
        "text": "This is a fantastic product and I love using it!"
    }
    ```
    Replace `"This is a fantastic product and I love using it!"` with the text you want to analyze.

**Example using `curl`:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text": "This movie was absolutely terrible."}' [http://0.0.0.0:5000/sentiment](http://0.0.0.0:5000/sentiment)
