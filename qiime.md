# QIIME 1 Analysis
Adaptation of this [tutorial](https://github.com/BikLab/BITMaB-workshop/blob/master/QIIME-metabarcoding-tutorial-already-demultiplexed-fastqs.md) for samples produced by Novogene.  Samples were demultiplexed by them and not labelled.  Reads were labelled using [renamer.py](https://github.com/calandryll/qiime2/blob/master/mothur/renamer.py).

## Paired End Joining
```bash
multiple_join_paired_ends.py \
	-i raw_data/ \
	-o data_clean/joined_fastq/ \
	--read1_indicator _1 \
	--read2_indicator _2 \
	-p parameters/join_pe.txt
```
Unjoined files were removed to prevent incorporation into the split libraries command.
```bash
find . -name \*.un1.fastq -type f -delete
find . -name \*.un2.fastq -type f -delete
```

## Quality filtering and joining of individuals samples into a single file
```bash
multiple_split_libraries_fastq.py \
	-i data_clean/joined_fastq/ \
	-o data_clean/split_libraries/ \
	--read_indicator _1 \
	-p parameters/split_libraries.txt
```