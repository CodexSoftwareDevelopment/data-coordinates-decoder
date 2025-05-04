# Data Coordinates Decoder

This project takes a Google Doc containing positional Unicode data and renders a hidden message from it in a text-based grid. It was created as part of a certification assessment for Data Annotation.

## 🧠 How It Works

- The program takes a public Google Doc URL as input.
- It fetches the document content using `requests` and `BeautifulSoup`.
- It parses 2D coordinates and their associated characters using regular expressions.
- It builds a dictionary of characters at each coordinate.
- It prints a visual grid showing the decoded message.

## 🛠️ Technologies Used

- Python 3
- `requests`
- `BeautifulSoup`
- `re` (Regular Expressions)

## 📁 Files

- `main.py`: Main program logic
- `README.md`: Project documentation

## 🚀 How to Run
1. Clone this repository:

        git clone https://github.com/CodexSoftwareDevelopment/data-coordinates-decoder.git

2. Install dependencies:
    
        pip install requests beautifulsoup4

3. Run the script:

        python main.py

## ✍️ Author
Deidra Clay
Founder of Codex Software Development