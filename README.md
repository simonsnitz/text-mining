# Pubmed Text Mining Pipeline
The goal of this repository is to extract experimental data on protein interactions from research articles.

## Usage
** Create an excel file with relevant Pubmed IDs **

1. Clone this repo.

2. Within the "search-filter_pubmedIDs.py" file, specify (1) search terms for querying Pubmed, such as "TetR", (2) the maximum number of articles to search among, and (3) filter terms, which will be used to remove articles that do no contain relevant information.

3. The output file will be in the "/cache" directory

## Dependencies
- pymed
- pandas
- requests
- datetime
- bs4
- pathlib

## Notes
This is a collaborative project between Lakshmi Surada, of LASA, and Simon d'Oelsnitz, a Research Scientist at the University of Texas at Austin. Information retrieved from this pipeline will be manually validated and used to populate [The Biosensor Database](https://gbiosensors.com)

## License
Work in the `src` directory is licensed under the MIT License, found in the LICENSE.txt file
