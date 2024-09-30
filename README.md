
Task: Sentiment Analysis API with LLM Integration


Objective:
Develop a Python-based API that processes customer reviews, performs sentiment analysis using a Large Language Model, and returns structured results. Document your approach and findings.


Requirements:


1. API Development:
   - Create a Flask-based API that accepts XLSX or CSV files containing 50 customer reviews.
   - Process the input file to extract review text.
   - Integrate with the Groq API (free to use) to perform sentiment analysis on the reviews.
   - Return a structured JSON response in the following format:


     {
       "positive": score,
       "negative": score,
       "neutral": score
     }



2. Technical Specifications:
   - Use Python and a web framework of your choice (e.g., Flask, FastAPI, Django).
   - Handle both CSV and XLSX file formats.
   - Implement basic error handling for common issues (e.g., invalid file formats, API errors).


3. Documentation:
   - Produce a PDF document detailing:
     - Your approach to solving the problem
     - How implemented structured response
     - Examples of API usage with sample inputs/outputs
     - Analysis of results, including limitations and potential improvements
     - Any additional insights or observations


Evaluation Criteria:
- Functionality and correctness of the API
- Code quality and organization
- Error handling and robustness
- Clarity and completeness of documentation
- Insights and analysis provided in the documentation


Submission:
Please submit your complete Python code for the API along with the PDF documentation of your process and findings.
