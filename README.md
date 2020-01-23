# gwas
This project aims to create a Python script that can be used directly on files downloaded from the GWAS Catalog website (https://www.ebi.ac.uk/gwas/).
The goal of the tool available here (gwas.py) is to return quick analysis results as the output based on an input consisting of a given GWAS Catalog file (specifically, a .tsv file, the file type automatically downloaded from the Catalog website).
Key statistics intended to be included in these results include the number and percent of reported associations that are consistent, replicated, or statistically significant below a given p-value threshold.

Note: This script is not complete yet; you can try to use it, but there is no guarantee that it will work in its current form. The way you are supposed to use it is through the command line with the following command:

python gwas.py [name of .tsv file]
