# HTX xData Take Home Assessment

This repository contains the solutions for HTX xData technical test. 

## Question 1

To install all dependencies, from the main directory, run the following command:  
```
pip install --upgrade -r requirements.txt
```

The .gitignore file is in the main repository.

## Question 2

The solutions can be found in asr/asr_api.py. 

To run the API server:

1. From the main directory, open a terminal and run the command:

```
uvicorn asr.asr_api:app --reload --host 0.0.0.0 --port 8001
```

This command will serve the API on http://localhost:8001.

2. For 2d, run the following command:

```
python asr/cv-decode.py 
```

Make sure to update the file paths in the code if the relative location of the datasets is different. 
The output csv can be found in asr/cv-valid-dev-updated.csv.

3. From the parent directory, build the docker image using the following:
```
docker build . -t asr-api
```
To start a container, use the following command:
```
docker run -p 8001:8001 --name <container name> -d asr-api
```

## Question 3

Q3(a) and Q3(c) solution is provided in asr-train/cv-train-2a.ipynb. 

Modify the file paths to datasets (CV_DIRECTORY) accordingly.

## Question 4

Solution to question 4 is in the main repository, found in training-report.pdf.

## Question 5

Solution to 5(a) is in hotword-detection/cv-hotword-5a.ipynb. The output text file is in hotword-detection/detected.txt.

Solution to 5(b) is in hotword-detection/cv-hotword-similarity-5b.ipynb. The input csv file is in hotword-detection/cv-valid-dev.csv. The output csv file which includes the boolean similarity values is in hotword-detection/cv-valid-dev-results.csv. 

## Question 6

Solution to question 6 is in the main repository, found in essay-ssl.pdf.

