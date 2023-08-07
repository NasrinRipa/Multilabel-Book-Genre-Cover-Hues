# Multilabel-Book-Genre-Cover-Hues

A text classification model from data collection, model training, and deployment. <br/>
The model can classify 58 book cover colors for 7575 numbers of different book genres <br/>The keys of `deployment\color_types_encoded50.json` shows the book cover colors for top 10 genres of each book.

 ## Data Collection

Data was collected from the Website: https://www.smashwords.com <br/>
The data collection process is divided into 3 steps:

1. **Book URL Scraping:** The book urls were scraped with `scraper\smashbook_title_urls.py` and the urls are stored along with book title in `scraper\smashbook_urls_1001.csv` and `scraper\smashbook_urls_2001.csv`.
2. **Book Details Scraping:** Using the urls, book description and genres are scraped with `scraper\smashbook_details.py` and they are stored in `scraper\smashbook_detils1.csv` and `scraper\smashbook_detils_2.csv`.
3. Finally, I joined the above 2 csv files (smashbook_details1.csv and smashbook_details_2.csv) by using another Python code `scraper/joining.py` and the merged csv file is in scraper/book_details_merged_tables.csv.

In total, I scraped 21200+ book details

## Data Preprocessing

At this stage, I first cleaned the data and find out the top 10 genres of each book titles and saved them in a new column and the code is in scraper/'cleaned_book_detail_with top10genres.py' and output is saved in 'scraper/book-details_10common_genres.csv'. <br>
After that, I assigned colors for the top 10 genres of each titles in the rows. The code is in 'scraper/assigning_colors_for_top10genres.py' and the output file is saved in 'data/book_details_with_50colors.csv'. 

## Model Training

Finetuned a `distilrobera-base` model from HuggingFace Transformers using Fastai and Blurr. The model training notebook can be viewed [here](https://github.com/NasrinRipa/Multilabel-Book-Genre-Cover-Hues/blob/main/notebooks/multilabel_text_classification.ipynb)

## Model Compression and ONNX Inference

The trained model has a memory of 300+MB. I compressed this model using ONNX quantization and brought it under 80MB. 

## Model Deployment

The compressed model is deployed to HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [here](https://huggingface.co/spaces/nasrin2023ripa/rainbow-genres-cover-ml-classifier)) 

![Gradio App](deployment/for_gradio_app.png)


## Web Deployment
Deployed a Flask App built to take descprition and genres, and recommends the book-cover colors as output. Check `flask ` branch. The website is live [here](https://multilabel-book-genre-cover-hues.onrender.com/) 

<img src = "deployment/flask_app_home.PNG" width="800" height="400">
<img src = "deployment/flask_app_results.PNG" width="800" height="200">

### Acknowledgments

I would like to express my heartfelt gratitude to Mohammad Sabik Irbaz, MasterCourse Bangladesh, who played a pivotal role in the success of this 3rd capstone project. Their expertise, guidance, and unwavering support were instrumental in shaping my skills and enabling me to complete this repository. I am truly grateful for their mentorship and valuable insights throughout this journey.


