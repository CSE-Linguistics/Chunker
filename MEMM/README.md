## MEMM Chunker
* We use MEMM model to perform B,I,O tagging of the sentences.
* The notebook contains all the code required to train the model, make predictions and perform error analysis.

### Options to run code

* Kaggle
  - Upload the dataset "CONLL2000" to "/kaggle/input/" directory in kaggle
  - Run the notebook
* Locally
  - Update path to load file for train data and test data. The code snippet is as follows:
  ```
        train_file = "/kaggle/input/conll2000/train.txt"
         test_file  = "/kaggle/input/conll2000/test.txt"
  ```
