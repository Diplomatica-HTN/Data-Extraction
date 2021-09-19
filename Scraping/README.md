# Data Extraction Model 📝🤏🏻

Model that extracts relevant information about events internationally, regionally, locally, and globally, based on the user's desired political interests and location. 

 
# The Model 🤖

The web scraper was made in Python using Beautiful soup, and urllib. Essentially, given a desired inputted term, which would be a topic a user wants to learn, the algorithm will output the most relevant article links on Google based on the user’s location and relevance based on Google’s search query. At max there will be nine articles being outputted, which will be sent to our summarization model one-by-one (found under "ml-foundation" repo) to get summarized. 

There are no limitations to this scraper. However, there will be links with private servers that will be returned. Therfore, do note, that those edge cases have been taken care of in our summarization model with exception statements.

# Significance 🔮

All scraped links based on the inputted topic by the user will be sent to a list. That list will then be ran iteratively on the summarization model to summarize each article based on the user's desried complexity. This allows them to learn relevant and accurate articles based on Google's and our algorithms. 

# Extra Notes 

The full model is under `full_nlp.ipynb`. 

Do note that `link_model.py` is just a test file for the algorithm. 
