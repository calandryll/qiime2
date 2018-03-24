# QIIME 1 Analysis
Adaptation of this [tutorial](https://github.com/BikLab/BITMaB-workshop/blob/master/QIIME-metabarcoding-tutorial-already-demultiplexed-fastqs.md) for samples produced by Novogene.  Samples were demultiplexed by them and not labelled.  ~~Reads were labelled using [renamer.py](https://github.com/calandryll/qiime2/blob/master/mothur/renamer.py).~~

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

## Remove Reverse Primers
```bash 
truncate_reverse_primer.py \
	-f data_clean/split_libraries/seqs.fna \ 
	-m mapping/mapping.txt \
	-o data_clean/trunc_primer
```

## Open Reference OTU picking
```bash
pick_open_reference_otus.py \
	-i data_clean/trunc_primer/seqs_rev_primer_truncated.fna \
	-o analysis/otus \
	-p parameters/otu.txt \
	-a \
	-O 24
```

## Diversity analysis

|Summarization of otu_table_mc2_w_tax_no_pynast_failures.biom||
|---|---|
|Num samples:| 91|
|Num observations: |241,524|
|Total count: |17,926,512|
|Table density (fraction of non-zero values): |0.076|
|Counts/sample summary:||
|Min: |113,754.000|
|Max: |211,538.000|
|Median: |199,144.000|
|Mean: |196,994.637|
|Std. dev.: |14,139.236|
|Sample Metadata Categories:| None provided|
|Observation Metadata Categories: |taxonomy|

### Core Diversity analysis
A sampling depth of 113,754 will be used for diversity anaylsis.

```bash
core_diversity_analyses.py \
	-o analysis/diversity \
	-i analysis/otus/otu_table_mc2_w_tax_no_pynast_failures.biom \
	-m mapping/mapping.txt \
	-t analysis/otus/rep_set.tre \
	-e 113754 \
	-a \
	-O 24 \
	--recover_from_failure
```

## Functional Analysis via [PICRUSt](https://picrust.github.io/picrust/index.html)

### Convert open reference OTU table to closed reference OTU table
```bash
filter_otus_from_otu_table.py \
	-i otus/otu_table_mc2_w_tax_no_pynast_failures.biom \
	-o picrust/closed_otu_table.biom \
	-e ~/qiime1/local/lib/python2.7/site-packages/qiime_default_reference/gg_13_8_otus/rep_set/97_otus.fasta
```

### Remove samples with 0 read counts
```bash
filter_samples_from_otu_table.py \
	-i picrust/closed_otu_table.biom \
	-o picrust/filtered_closed_otu_table.biom \
	-n 1
```

### Remove fecal samples
```bash
filter_samples_from_otu_table.py \
	-i picrust/filtered_closed_otu_table.biom \
	-o picrust/env_samples.biom \
	-m ../mapping/mapping.txt \
	-s 'Env:Water'
```

### Normalize copy number
```bash
normalize_by_copy_number.py \
	-i env_samples.biom \
	-o normalized_otus.biom
```