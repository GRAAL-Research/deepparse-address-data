# Deepparse Address Dataset
This repository contains the address data used to train the models of our address parsing package 
[deepparse](https://deepparse.org).

The data present in this repository has been generated using data from the 
[lipbostal](https://github.com/openvenues/libpostal) project.

## Content of the Project
 - The script to merge all the countries' datasets into a single one (`make_dataset`).
 - A script to *decompress* LZMA archive into *normal* pickle format for Python (`lzma_decompress`).

## Download the Data
Since our dataset is too *large* for GitHub and we were stuck with bandwidth limits, the dataset is available in a
`zip` format on Google Drive. You can manually download it using this 
[link](https://drive.google.com/u/5/uc?id=1t6AZXO51PIKl5GIkD-bpwBBopQiyeAce&export=download) or use the following command

```python3
pip install gdown
gdown --id 1t6AZXO51PIKl5GIkD-bpwBBopQiyeAce --output data.zip
```

## About the Data
The data is split into two main categories:

- **clean data**: addresses containing elements from at least four categories, namely a street name, a municipality, a province and a postal code

- **incomplete data**: addresses missing at least one category amongst the aforementioned ones.

### Clean data
The `clean_data` directory contains three subdirectory `train`, `test` and `zero_shot`. The number of data samples per 
country for the `train` & `test` dataset. Each directory contains data for 20 countries, as described in Figure 1.

| Country     |   Number of samples in `train`   |   Number of samples in `test`   | Country         |  Number of samples in `train`   |   Number of samples in `test` |
|:------------|---------------------------------:|--------------------------------:|:----------------|--------------------------------:|--------------------------------:|
| Italy       |                          100,000 |                         178,848 | United States   |                         100,000 |                       8,000,000 |
| Germany     |                          100,000 |                       1,576,059 | Austria         |                         100,000 |                         335,800 |
| South Korea |                          100,000 |                       6,048,106 | Canada          |                         100,000 |                         910,891 |
| Mexico      |                          100,000 |                       4,853,349 | Australia       |                         100,000 |                       5,428,043 |
| Finland     |                          100,000 |                         280,219 | Netherlands     |                         100,000 |                       1,202,173 |
| France      |                          100,000 |                          20,050 | United Kingdom  |                         100,000 |                          14,338 |
| Russia      |                          100,000 |                           8,115 | Norway          |                         100,000 |                         405,649 |
| Switzerland |                          100,000 |                         474,240 | Poland          |                         100,000 |                         459,522 |
| Brazil      |                          100,000 |                       8,000,000 | Denmark         |                         100,000 |                         199,694 |
| Spain       |                          100,000 |                       1,395,758 | Czechia         |                         100,000 |                         195,269 |
> Figure 1. The number of data samples per country in the train and test datasets for **clean data**.

The `zero_shot` dataset contains data for an additional 41 countries. The number of data samples per country is described in Figure 2.

| Country                |   Number of samples | Country                           |   Number of samples |
|:-----------------------|--------------------:|:----------------------------------|--------------------:|
| Latvia                 |               1,325 | Faroe Islands                     |               2,982 |
| Colombia               |                 569 | Singapore                         |                 968 |
| Réunion                |               2,514 | Indonesia                         |               2,259 |
| Japan                  |              14,089 | Portugal                          |               4,637 |
| Algeria                |                 601 | Belgium                           |              66,182 |
| Malaysia               |               2,043 | Ukraine                           |               9,554 |
| Estonia                |               1,024 | Bangladesh                        |                 888 |
| Slovenia               |               9,773 | Hungary                           |              17,460 |
| Bermuda                |               2,065 | Romania                           |              19,420 |
| Philippines            |              10,471 | Belarus                           |               7,590 |
| Bosnia and Herzegovina |                 681 | Moldova, Republic of              |               2,376 |
| Lithuania              |               3,126 | Paraguay                          |                 839 |
| Croatia                |               5,671 | Argentina                         |              27,692 |
| Ireland                |                 638 | Kazakhstan                        |               1,087 |
| Greece                 |               4,974 | Bulgaria                          |               3,715 |
| Serbia                 |               6,792 | New Caledonia                     |               1,036 |
| Sweden                 |              32,291 | Venezuela, Bolivarian Republic of |              10,696 |
| New Zealand            |               4,678 | Iceland                           |              13,617 |
| India                  |              26,075 | Uzbekistan                        |                 505 |
| Cyprus                 |                 836 | Slovakia                          |              18,975 |
| South Africa           |               1,388 |
> Figure 2. The number of data samples per country in the zero shot dataset for **clean data**.

### About the Incomplete Data

The *incomplete* directory contains two subdirectories, each containing address data for the 20 countries listed in Figure 1. 
The `train` subdirectory contains 50,000 addresses per country, and the `test` subdirectory contains 25,000 per country.

## About the `make_dataset` Script

The `make_dataset` script merges all the individual files in a particular folder into one dataset. 
This script merges all the data so as to allow for balanced batches during training 
(when the batch size is greater than the number of files).

Run the following
```python
python3 make_dataset.py -h
```
to get information about the arguments needed to run the script.

## About the `lzma_decompress` Script
Since the dataset is pretty large (especially for Github hosting), we have used the `LZMA` compress algorithm using 
Python to make our files as smaller as possible. To do so, we used the convenient 
[`compress_pickle`](https://pypi.org/project/compress-pickle/) wrapper library to compress the data. Since `LZMA` 
is really slow to decompress, we provide a script to decompress it into standard pickle format. 

The script will decompress the data files into the `path_to_save` directory, and will create the same subdirectory as
described earlier (`clean_data` and `incomplete_data` plus the subdirectory `train`, `test` and `zero_shot`).

This script take a couple of minutes to execute.

## Cite the Dataset

If you use the data provided with this repository, please cite us using the following:

```
@misc{deepparse-address-data,
    author = {Marouane Yassine and David Beauchemin},
    title  = {{Structured Multinational Address Data}},
    year   = {2020},
    note   = {\url{https://github.com/GRAAL-Research/deepparse-address-data}}
}
```
