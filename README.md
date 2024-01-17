# publication-date-extract

Simple script for extracting publication date from webpages.
Takes csv file input, where first column contains URL links to webpages.
Outputs `output.csv` file, which is the input file with an added column of publication date.

This script uses the [htmldate package](https://htmldate.readthedocs.io/en/latest/index.html)https://htmldate.readthedocs.io/en/latest/index.html.

## Usage

To use script, clone repo then make sure requirements are installed.

`git clone https://github.com/kwansupp/publication-date-extract.git`

`pip install -r requirements.txt`

Run script file on csv file:
`python extract_publication_date.py <csv_input>`
