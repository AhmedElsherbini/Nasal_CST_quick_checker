## CST_Picker

This script aims to classfiy nasal microbiome samples (**based on a literature defention not in an unsupervised fashion**). Therefore, in each sample the scripts see the most dominant species in each sample. 

**And if this dominat species is**

_S. aureus_  ---> we conclude CST1

Species belongs to Enterobacteriaceae family --> we conclude CST2

_S. epidermidis_ --> we conclude CST3

Species belong to Cutibacterium genus --> we conclude CST4

Species belong Corynebacterium genus --> we conclude CST5

Species belong Moraxella genus -->  we conclude CST6

Species belong Dolosigranulum genus -->  we conclude CST7

if something else, then we concluded that is unclassified

## Installation and Usage

Any case, You need Python3 with (pandas, seaborn, matplotlib and argparse packages)

>>> If you are qiime2 user 

Then, you just need the feature-table.qza and the taxonomy.qza (example attached) out of your analysis in the same dir of the bash and python script.

P.S. (This script was tested using qiime2 2021.11. However, I suppose it will work with other versions also)


```python
conda activate qiime2-2021.11

bash cst_picker.sh
```
that's it.

>>> If you are not qiime2 user

You need to prepare the relative abundace phyla table like the example one attached.

```python
python get_cst.py -i example_rel-phyla-table.tsv
```

## Contributing



## License

