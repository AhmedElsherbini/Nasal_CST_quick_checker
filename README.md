## CST_Picker

This script aims to classify nasal microbiome samples (**based on the reductive literature definition in an supervised fashion**). Therefore, in each sample, the scripts extracts the most dominant species. 

**And based on relative abundance, if the  top/most prevalent species is**

* _S. aureus_  ---> we conclude CST1

* Species belong to Enterobacteriaceae family --> we conclude CST2

* _S. epidermidis_ --> we conclude CST3

* Species belong to the Cutibacterium genus --> we conclude CST4

* Species belong to Corynebacterium genus --> we conclude CST5

* Species belong Moraxella genus -->  we conclude CST6

* Species belong to Dolosigranulum genus -->  we conclude CST7

* If something else, then we conclude that is an unclassified CST

## Installation and Usage

>>> If you are qiime2 user 

Then, you just need the feature-table.qza and the taxonomy.qza (examples attached) out of your analysis in the same dir of the bash and python script.

P.S. (This tool was tested using different qiime2 versions  (2021.11 , 2021.8 and 2020.02) versions. However, I suppose it will work with other versions also). Of note, it was designed to run on Linux .but it also worked on the terminal of linux subsystem windows.


```
conda activate qiime2-2021.11

bash cst_picker.sh
```
that's it!

>>> If you are not qiime2 user

Then nou need Python3 with (pandas, seaborn, matplotlib, and argparse packages). 

You need to prepare the relative abundance phyla table the same as the example attached. Then, use it with this python script.

```python
python get_cst.py -i example_rel-phyla-table.tsv
```

The output in output folder (named rel-table) is 3 files in output dir. 1, CSV file with each sample with it is predicted CST. 2, CSV file with CST composition. 3, barplot with the relative abundance of CST.

(P.S, if you are qiime2 user you will also get the rel-phyla-table.tsv for relative abundance)

Anyhow, an example of the output folder (rel-table) is attached.


## Contributing

You are welcome, please open an issue (or mail me : drahmedsherbini@yahoo.com) to discuss what you would like to change.


## License
This tool is part of a paper XXX please cite us.
