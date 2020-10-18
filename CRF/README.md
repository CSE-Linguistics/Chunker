## CRF Chunker
* We use CRF model to perform B,I,O tagging of the sentences.
* The notebook contains all the code required to train the model, make predictions and perform error analysis.

### Options to run code

* Google colab
  - Upload the dataset "CONLL 2020" to "/content" directory in colab
  - Run the notebook
* Locally
  - Install requirements by running:
  ```pip install -r requirements.txt```
  - Update path to load file for train data and test data. The code snippet is as follows:
  ```train_sents = load_data('/content/train.txt') # change to relevant path```
  ```test_sents = load_data('/content/test.txt') # change to relevant path```
  - Run the notebook leaving the first cell
