## CST_Picker

This script aims to classify nasal microbiome samples (**based on the literature definition [(Liu et al. Sci. Adv. 2015)](https://www.science.org/doi/10.1126/sciadv.1400216) in a supervised fashion**). Therefore, in each sample, the scripts extract the most dominant species. 

**And based on relative abundance, if the  top/most prevalent species is**

* _S. aureus_  ---> we conclude CST1

* Species belong to Enterobacteriaceae family --> we conclude CST2

* _S. epidermidis_ --> we conclude CST3

* Species belong to the Cutibacterium genus --> we conclude CST4

* Species belong to Corynebacterium genus --> we conclude CST5

* Species belong to Moraxella genus -->  we conclude CST6

* Species belong to Dolosigranulum genus -->  we conclude CST7

* If something else, then we conclude that is an unclassified CST (in this case, it is important to look how they cluster in unsupervised fashion).

**As mentioned before,it is important beside this tool, to look at the beta-diversity metric Weighted Unifrac using QIIME 2 ([not phyloseq](https://github.com/joey711/phyloseq/issues/956)!) or using Vegan package in R.**

## Installation and Usage

This tool was tested using different QIIME 2 (2021.11, 2021.8, and 2020.02) versions. However, I suppose it will work with other versions also. Of note, it was designed to run on Linux. But, it worked also on the terminal of Windows Subsystems Linux (WSL).

>>> If you are QIIME 2 user 

Then, you just need the feature-table.qza and the taxonomy.qza (examples attached) out of your analysis. And put them in the same dir of the bash and python script.


```
conda activate qiime2-2021.11

bash cst_picker.sh
```
that's it!

>>> If you are not QIIME 2 user

Then you need Python3 with (pandas, seaborn, matplotlib, and argparse packages). 

You need to prepare the relative abundance phyla table the same as the example tab seperated file attached. Then, use it with this python script.

```python
python get_cst.py -i example_rel-phyla-table.tsv
```

The output is a folder (named rel-table) within this folder you have 3 files. Those files are  1, CSV file with each sample with it is predicted CST. 2, CSV file with CST composition. 3, barplot with the relative abundance of CST.

(P.S, if you are QIIME 2 user you will also get the rel-phyla-table.tsv for relative abundance)

Anyhow, an example of the output folder (rel-table) is attached.


## Contributing

You are welcome, please open an issue (or mail me : drahmedsherbini@yahoo.com) to discuss what you would like to change.


## License

This work is part of paper named **Targeting of the human nasal microbiota by secretory IgA antibodies**

If you find this work useful, please [cite us](https://www.biorxiv.org/content/10.1101/2022.08.31.505993v1.full).

## The code for other parts of the paper ?

[Here](https://github.com/AhmedElsherbini/R-code-for-RVD-et-al.-2022)


