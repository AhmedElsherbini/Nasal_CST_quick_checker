## CST_Picker

This script aims to classify nasal microbiome samples (**based on a literature definition in an supervised fashion**). Therefore, in each sample, the scripts see the most dominant species. 

**And if this dominant species is**

* _S. aureus_  ---> we conclude CST1

* Species belong to Enterobacteriaceae family --> we conclude CST2

* _S. epidermidis_ --> we conclude CST3

* Species belong to the Cutibacterium genus --> we conclude CST4

* Species belong to Corynebacterium genus --> we conclude CST5

* Species belong Moraxella genus -->  we conclude CST6

* Species belong to Dolosigranulum genus -->  we conclude CST7

* If something else, then we conclude that is an unclassified CST

## Installation and Usage

In any case, you need Python3 with (pandas, seaborn, matplotlib, and argparse packages)

>>> If you are qiime2 user 

Then, you just need the feature-table.qza and the taxonomy.qza (example attached) out of your analysis in the same dir of the bash and python script.

P.S. (This script was tested using qiime2 2021.11. However, I suppose it will work with other versions also)


```python
conda activate qiime2-2021.11

bash cst_picker.sh
```
that's it!

>>> If you are not qiime2 user

You need to prepare the relative abundance phyla table like the example attached.

```python
python get_cst.py -i example_rel-phyla-table.tsv
```

## Contributing

You are welcome, please open an issue (or Email me : drahmedsherbini@yahoo.com) to discuss what you would like to change.


## License
This tool is part of a paper XXX please cite us.
