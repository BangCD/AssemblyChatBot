# AssemblyChatBot
Chatbot for Infive organization using OpenAI api

To generate the excel sheet with all the learned data and their ensembler
Run the crawler2.ipynb file completly
This will scrape through in5 website and save each website it goes through as a txt file .
The program then goes through all the txt files and combines them into a excel sheet called 
add all the information into an excel sheet called "scraped.csv", this is the raw format of the scrapped text.

The program uses scraped.csv to make another csv called "embeddings.csv" using OpenAI's text-embedding-ada-002 engine. 

With the embedding file created you can now call the answer_question function, provide it the embedding.csv as a dataframe and your question as a string.

To add more data to the model, you can edit the scraped.csv file where col2 (fname) should be the heading or the url name from where you are taking the information, col3(text) will the content/information.
After adding the new information rerun rest of the code from cell number 43 ( where it says - tokenizer = tiktoken.get_encoding("cl100k_base") ) to rebuild the embeddings.

Note 

You do not need to scrap or build embeddings everytime to ask a question, it is only a one time thing and should only be rebuilt incase more information has been added to scrapped. 

=======

To link the code to front end use crawler2.py which contains only the create_context and answer_question functions. ( Embeddings.csv needs to exist before running this code) 

I have created a flask app in CrawlerView.py which only takes questions as a string input and gives response as 
{  
  "status": "Success", 
  "message" : "the answer" 
} 
on success 
and
{
    "message": "Error O",
    "status": "Failed"
} 
on failed.
