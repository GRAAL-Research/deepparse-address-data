# Deepparse Address Dataset
This repository contains the address data used to train the models of our address parsing package 
[deepparse](https://deepparse.org).

The data present in this repository has been generated using data from the 
[lipbostal](https://github.com/openvenues/libpostal) project.

## Content of the Project
 - The script to merge all the countries' datasets into a single one (`make_dataset`).
 - A script to *decompress* LZMA archive into *normal* pickle format for Python (`lzma_decompress`).

## Download the Data
Our dataset is hosted on the address below in a `zip` format. 
You can manually download it by clicking [here](https://graal.ift.ulaval.ca/public/deepparse/dataset/) or you can use `wget` as follow:

```bash
wget https://graal.ift.ulaval.ca/public/deepparse/dataset/data.zip
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

### About the [`hyphen_unit_street_number.p`](https://graal.ift.ulaval.ca/public/deepparse/dataset/hyphen_unit_street_number.p) Data
Some countries use a hyphen to split the unit from the street number (e.g. 3-305 a street name, where 3 is the unit and 305 is the street number), and none were properly parsed in the training data. We have created a new dataset with such cases. The dataset consists of 3 012 automatically parsed addresses using regex where the hyphen has been removed, and tags have been adjusted. Namely, before the address '3-305 a street name' tags would have been `[StreetNumber, StreetName, StreetName, StreetName]`. In this dataset, the address is '3 305 a street name', and the tags are `[Unit, StreetNumber, StreetName, StreetName, StreetName]`.

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
Since the dataset is pretty large (especially for Github hosting), we have used the `LZMA` compressing algorithm using 
Python to make our files as small as possible. To do so, we used the convenient 
[`compress_pickle`](https://pypi.org/project/compress-pickle/) wrapper library to compress the data. Since `LZMA` 
is really slow to decompress, we provide a script to decompress it into standard pickle format. 

The script will decompress the data files into the `path_to_save` directory provided as an argument, and will create the same subdirectory as
described earlier (`clean_data` and `incomplete_data` plus the subdirectories `train`, `test` and `zero_shot`).

This script takes a couple of minutes to execute.

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

## License
This dataset is under [MIT License](https://mit-license.org/)

## Dataset Metadata
The following table is necessary for this dataset to be indexed by search
engines such as <a href="https://g.co/datasetsearch">Google Dataset Search</a>.

<div itemscope itemtype="http://schema.org/Dataset">
<table>
  <tr>
    <th>property</th>
    <th>value</th>
  </tr>
  <tr>
    <td>name</td>
    <td><code itemprop="name">Multinational Structured Address Dataset</code></td>
  </tr>
  <tr>
    <td>alternateName</td>
    <td><code itemprop="alternateName">Address Parser Dataset</code></td>
  </tr>
  <tr>
    <td>alternateName</td>
    <td><code itemprop="alternateName">deepparse-dataset</code></td>
  </tr>
  <tr>
    <td>url</td>
    <td><code itemprop="url">https://github.com/GRAAL-Research/deepparse-address-data</code></td>
  </tr>
  <tr>
    <td>description</td>
    <td><code itemprop="description">The Multinational Structured Address Dataset is a collection of addresses of 61 different countries. The addresses can either be "complete" (all the usual address components) or "incomplete" (missing some usual address components). \n Example of addresses 
        ![preview](https://rawcdn.githack.com/GRAAL-Research/deepparse-address-data/master/address_parsing_example.png)\n
    </code></td>
  </tr>
    <tr>
        <td>creator</td>
        <td>
          <div itemscope itemtype="http://schema.org/person" itemprop="creator">
            <table>
              <tr>
                <th>property</th>
                <th>value</th>
              </tr>
              <tr>
                <td>name</td>
                <td><code itemprop="name">Marouane Yassine</code></td>
              </tr>
              <tr>
                <td>sameAs</td>
                <td><code itemprop="sameAs">https://scholar.google.com/citations?user=EjZyhCAAAAAJ&hl=fr&oi=sra</code></td>
              </tr>
                <tr>
                <td>name</td>
                <td><code itemprop="name">David Beauchemin</code></td>
              </tr>
              <tr>
                <td>sameAs</td>
                <td><code itemprop="sameAs">https://scholar.google.com/citations?hl=fr&user=ntoPgSUAAAAJ</code></td>
              </tr>
            </table>
          </div>
        </td>
      </tr>
  <tr>
    <td>provider</td>
    <td>
      <div itemscope itemtype="http://schema.org/Organization" itemprop="provider">
        <table>
          <tr>
            <th>property</th>
            <th>value</th>
          </tr>
          <tr>
            <td>name</td>
            <td><code itemprop="name">GRAIL</code></td>
          </tr>
          <tr>
            <td>sameAs</td>
            <td><code itemprop="sameAs">https://grail.ift.ulaval.ca/</code></td>
          </tr>
        </table>
      </div>
    </td>
  </tr>
  <tr>
    <td>license</td>
    <td>
      <div itemscope itemtype="http://schema.org/CreativeWork" itemprop="license">
        <table>
          <tr>
            <th>property</th>
            <th>value</th>
          </tr>
          <tr>
            <td>name</td>
            <td><code itemprop="name">MIT</code></td>
          </tr>
          <tr>
            <td>url</td>
            <td><code itemprop="url">https://mit-license.org/</code></td>
          </tr>
        </table>
      </div>
    </td>
  </tr>
    <tr>
    <td>citation</td>
    <td><code itemprop="citation">https://arxiv.org/abs/2006.16152</code></td>
  </tr>
</table>
</div>
