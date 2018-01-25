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