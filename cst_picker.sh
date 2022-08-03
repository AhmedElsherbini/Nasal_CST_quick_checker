#cst_hunter
echo I hope you activated you qiime2 enviroment
#
qiime taxa collapse \
  --i-table feature-table.qza \
  --i-taxonomy taxonomy.qza \
  --p-level 7 \
  --o-collapsed-table phyla-table.qza
######################
qiime feature-table relative-frequency \
--i-table phyla-table.qza \
--o-relative-frequency-table rel-phyla-table.qza
#################
qiime tools export \
  --input-path rel-phyla-table.qza \
  --output-path rel-table
##################
cd rel-table
##################
biom convert -i feature-table.biom -o rel-phyla-table.tsv --to-tsv
#################
awk '{a[NR]=$0}END{for(i=2;i<=NR;i++)print a[i]>FILENAME}' rel-phyla-table.tsv
##################
cp ../get_cst.py ./
##################
python3 get_cst.py -i rel-phyla-table.tsv
##################
echo Can you check the folder rel-table for output ?
