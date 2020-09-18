# Information-Storage-and-Retrieval
A short instruction on how to read your scripts and how to run your scripts, including environment configuration.

Environment configuration:

Windows 10 Home
Processor : Intel(R) Core(TM) i7-8750H CPU @ 2.20GHZ 2.21 GHZ
Installed Memore(RAM) : 16.0 GB
System Type : 64 - bits Operting System

1. Open Anaconda. open Spyder 3.3.6 (Python 3.7) and upload the folder 
2. Run the HW1Main.py file. This will run the whole code
3. After running the HWMain.py file, first it will read and process the docset.trectext file from the data.
4. After the docset.trectext file is read and processed completely, it will read and process docset.trecweb file
5. Processing of file include extracting the content and docno, word tokenizer, word normalizer that inclued converting the sting to lower case and then stemming the word, and in the end stopword removal.

The results of the processed data is stored in the folder data/output/result.trectext for input file docset.trectext and data/output/result.trecweb for input file docset.trectext
