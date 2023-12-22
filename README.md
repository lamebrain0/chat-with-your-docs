Ask questions to your documents using the power of openai api key and langchain.


                            ENVIRONMENT SETUP
       step1 :- after cloning this repository ..run pip install -r requirements.txt.

       step2:- keep as many pdfs u want to keep in the docs folder..

       step3:- Run python pdf_to_text.py (it wiill extract all the tetxs from the pdfs and store it in a single .txt file)

       step3:- Run python index.py (it will convert the  texts from the .txt file into a faiss store .which will be later used for asking questions).

       step4:- Run python chat.py( dont forget to set the correct index store name before running.it is give u the answer of your question .i have set a prompt such 
               that i should answer only the question which is available in the pdfs ..not from the ooutside).

       Note:- dont forget to use openai api key.and keep the size of single pdf less than 15 mb.you can keep 100s of pdf but single pdf should not be more than 15mb 
              for more accuracy.
