# Love Creek Microbiome Analysis
Samples collected monthly at stations within the Love Creek watershed were sequenced by Novogene.  Samples arrived demultiplexed and can be imported without issue.

## Reads import
``` bash
qiime tools import \
--type 'SampleData[PairedEndSequencesWithQuality]' \
--input-path love_creek_manifest \
--output-path love_creek_demux.qza \
--source-format PairedEndFastqManifestPhred33

qiime demux summarize \
--i-data love_creek_demux.qza \
--o-visualization love_creek_demux.qzv
```


## Sequence QC and Table Construction
Examination of the data (love_creek_demux.qzv) suggests that no truncation is needed on either forward or reverse reads.

``` bash
qiime dada2 denoise-paired \
--i-demultiplexed-seqs love_creek_demux.qza \
--p-trunc-len-f 0 \
--p-trunc-len-r 0 \
--p-n-threads 0 \
--o-table love_creek_table_dada2.qza \
--o-representative-sequences love_creek_rep_seqs_dada2.qza
```

### Summary of Table and Data
```bash
qiime feature-table summarize \
--i-table love_creek_table_dada2.qza \
--o-visualization love_creek_table_dada2.qzv \
--m-sample-metadata-file mapping.tsv

qiime feature-table tabulate-seqs \
--i-data love_creek_rep_seqs_dada2.qza \
--o-visualization love_creek_rep_seqs_dada2.qzv
```

## Phylogentic Diversity Analysis
```bash
qiime alignment mafft \
--i-sequences love_creek_rep_seqs_dada2.qza \
--o-alignment love_creek_rep_seqs_aligned.qza

qiime alignment mask \
--i-alignment love_creek_rep_seqs_aligned.qza \
--o-masked-alignment masked_aligned_rep_seqs.qza \
--p-n-threads -1

qiime phylogeny midpoint-root \
--i-tree unrooted_tree.qza \
--o-rooted-tree rooted_tree.qza
```

## Alpha and Beta Diversity Analysis
A sampling depth of 29815 is approximately the highest sampling depth for all samples and will be used for rarefaction analysis.

```bash
qiime diversity core-metrics-phylogenetic \
--i-phylogeny rooted_tree.qza \
--i-table love_creek_table_dada2.qza \
--p-sampling-depth 29815 \
--m-metadata-file mapping.tsv \
--output-dir dada2_core

qiime diversity alpha-group-significance \
--i-alpha-diversity dada2_core/faith_pd_vector.qza \
--m-metadata-file mapping.tsv \
--o-visualization dada2_core/faith_pd_group_significance.qza

qiime diversity beta-group-significance \
--i-distance-matrix dada2_core/unweighted_unifrac_distance_matrix.qza \
--m-metadata-file mapping.tsv \
--m-metadata-category Site \
--o-visualization dada2_core/unweighted_unifrac_site_significance.qvz \
--p-pairwise
```

### Alpha Rarefaction
```bash
qiime diversity alpha-rarefaction \
--i-table love_creek_table_dada2.qza \
--i-phylogeny rooted_tree.qza \
--p-max-depth 40000 \
--m-metadata-file mapping.tsv \
--o-visualization alpha_rarefaction.qzv
```

## Taxonomic Analysis
All taxonomic analysis is done with the 515-806 data (V4 region), as this was the primer set used to generate the data.
### Green Genes Data
```bash
qiime feature-classifier classify-sklearn \
--i-classifier reference_sets/gg-13-8-99-515-806-nb-classifier.qza \
--i-reads love_creek_rep_seqs_dada2.qza \
--o-classification gg_taxonomy.qza

qiime feature-classifier classify-sklearn \
--i-classifier reference_sets/gg-13-8-99-nb-classifier.qza \
--i-reads love_creek_rep_seqs_dada2.qza \
--o-classification gg_all_taxonomy.qza
```

## Export OTU Table for Sourcetracker Analysis

```bash
qiime tools export \
love_creek_table_dada2.qza \
--output-dir otus

biom convert -i feature-table.biom -o feature_table.txt --to-tsv
```
This does not combine frequencies of OTUs into a singular line item for downstream analysis.

```bash
qiime taxa collapse \
--i-table love_creek_table_dada2.qza \
--i-taxonomy gg_taxonomy.qza \
--p-level 7 \
--o-collapsed-table collapsed_table.qza


```


Rscript ~/bin/sourcetracker/sourcetracker_for_qiime.r -i otus/feature_table.txt -m mapping.txt -o sourcetracker
```bash
qiime dada2 denoise-paired \
--i-demultiplexed-seqs love_creek_demux.qza \
--p-trunc-len-f 240 \
--p-trunc-len-r 240 \
--p-n-threads 0 \
--o-table love_creek_table_dada2.qza \
--o-representative-sequences love_creek_rep_seqs_dada2.qza
```

## Open reference clustering ala QIIME 1
97 otus from SILVA are used to cluster via open reference dada2 sequences.

```bash
qiime tools import \
--input-path reference_sets/SILVA_128_QIIME_release/rep_set/rep_set_16S_only/97/97_otus_16S.fasta \
--output-path silva_97_otus.qza \
--type 'FeatureData[Sequence]'

qiime vsearch cluster-features-open-reference \
--i-sequences love_creek_rep_seqs_dada2.qza \
--i-table love_creek_table_dada2.qza \
--i-reference-sequences silva_97_otus.qza \
--p-perc-identity 1 \
--p-threads 0 \
--o-clustered-table silva_open_table.qza \
--o-clustered-sequences silva_open_seq.qza \
--o-new-reference-sequences silva_open_ref_seq.qza
```

qiime vsearch cluster-features-open-reference \
--i-table derep_table.qza \
--i-sequences derep_seq.qza \
--i-reference-sequences ../silva_97_otus.qza \
--p-perc-identity 1 \
--p-threads 0 \
--o-clustered-table silva_open_table.qza \
--o-clustered-sequences silva_open_seq.qza \
--o-new-reference-sequences silva_open_ref_seq.qza

```bash
qiime vsearch join-pairs \
--i-demultiplexed-seqs ../love_creek_demux.qza \
--o-joined-sequences demux_joined.qza

qiime demux summarize \
--i-data demux_joined.qza \
--o-visualization demux_joined.qzv

qiime vsearch dereplicate-sequences \
--i-sequences demux_joined.qza \
--o-dereplicated-table derep_table.qza \
--o-dereplicated-sequences derep_seq.qza
```

```bash
qiime tools export derep_seq.qza --output-dir seq
pick_open_reference_otus.py -i seq.fa -o otus -a -O 20
biom convert -i otus/otu_table_mc2_w_tax_no_pynast_failures.biom -o nonfiltered.txt --to-tsv
Rscript ~/bin/sourcetracker/sourcetracker_for_qiime.r -i otus/feature_table.txt -m mapping.txt -o sourcetracker
```

```bash
multiple_join_paired_ends.py -i ../raw_data/ -o joined --read1_indicator _1. --read2_indicator _2.
multiple_split_libraries_fastq.py -i fastq/ -o split
pick_open_reference_otus.py -i split/final.fna -o otus -a -O 20
```

Filter for a minimum of 3 samples
```bash
filter_otus_from_otu_table.py -i otus/otu_table_mc2_w_tax_no_pynast_failures.biom -o filter_otu_table.biom -s 3
```
Run sourcetracker on the filtered OTU table from QIIME and QIIME2
```bash
Rscript /opt/sourcetracker/sourcetracker_for_qiime.r -i filtered_otu_table.txt -m ../mapping.txt -o sourcetracker
```