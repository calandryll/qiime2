# mothur Analysis
Analysis was carried out by using a mixture of [mothur's MiSeq SOP](https://www.mothur.org/wiki/MiSeq_SOP) and [this protocol](https://www.protocols.io/view/week-8-classifying-taxonomy-of-short-reads-with-mo-g7tbznn).  Raw files from [Novogene](https://en.novogene.com) were renamed and modified using the [renamer.py](https://github.com/calandryll/qiime2/blob/master/mothur/renamer.py) script to rename files and associated reads.

## Sequence Cleanup
### Make File and Contigs
```
make.file(inputdir=/media/science/microbiome/mothur, type=gz, prefix=stability)
make.contigs(file=stability.files, processors=24)
```
### Filter out oddball lengths
```
summary.seqs(fasta=stability.trim.contigs.fasta)
```
Using 24 processors.

||Start|End|NBases|Ambigs|Polymer|NumSeqs|
|---|---|---|---|---|---|---|
|Minimum:|1|244|244|0|3|1|
|2.5%-tile:|1|303|303|0|4|473077|
|25%-tile:|1|304|304|0|4|4730769|
|Median: |1|304|304|0|4|9461537|
|75%-tile:|1|304|304|0|5|14192305|
|97.5%-tile:|1|305|305|2|6|18449997|
|Maximum:|1|499|499|111|227|18923073|
|Mean:|1|304.417|304.417|0.23493|4.5084|
|# of Seqs:|18923073|

Output File Names: 
/media/science/microbiome/mothur/stability.trim.contigs.summary

It took 26 secs to summarize 18923073 sequences.
```
screen.seqs(fasta=stability.trim.contigs.fasta, group=stability.contigs.groups, summary=stability.trim.contigs.summary, maxambig=0, maxlength=305, minlength=295)
summary.seqs()
```

Using /media/science/microbiome/mothur/stability.trim.contigs.good.fasta as input file for the fasta parameter.

Using 24 processors.

| |Start| End| NBases| Ambigs| Polymer| NumSeqs|
|---|---|---|---|---|---|---|
| Minimum:| 1| | 295| 295| 0| 3| 1| 
| 2.5%-tile:|1| 303| 303| 0| 4| 446895|
| 25%-tile:| 1| 304| 304| 0| 4| 4468943|
| Median:| 1| 304| 304| 0| 4| 8937886|
| 75%-tile:| 1| 304| 304| 0| 5| 13406828|
|  97.5%-tile:| 1| 305| 305| 0| 6| 17428876| 
|  Maximum:| 1| 499| 499| 0| 227| 17875770| 
|  Mean:| 1| 304.372| 304.372| 0| 4.50755| 
|  # of Seqs:| 17875770| 

Output File Names:
/media/science/microbiome/mothur/stability.trim.contigs.good.summary

It took 23 secs to summarize 17875770 sequences.
### Remove duplicate sequences for easier analysis
```
unique.seqs(fasta=stability.trim.contigs.good.fasta)
count.seqs(name=stability.trim.contigs.good.names, group=stability.contigs.good.groups)
summary.seqs(count=stability.trim.contigs.good.count_table)
```
Using /media/science/microbiome/mothur/stability.trim.contigs.good.unique.fasta as input file for the fasta parameter.

Using 24 processors.

||Start|   End|     NBases|  Ambigs|  Polymer| NumSeqs|
|---|---|---|---|---|---|---|
|Minimum:|        1  |     295|     295|     0|       3  |     1|
|2.5%-tile:|      1  |     303|     303|     0|       4  |     446895|
|25%-tile:|       1  |     304|     304|     0|       4  |     4468943|
|Median:  |       1  |     304|     304|     0|       4  |     8937886|
|75%-tile: |      1  |     304|     304|     0|       5  |     13406828|
|97.5%-tile:|     1  |     305|     305|     0|       6 |      17428876|
|Maximum:    |    1  |     499|     499|     0       227|     17875770|
|Mean: |  1    |   304.372| 304.372| 0|       4.50755|
|# of unique seqs: |      9879082|
|total # of seqs:   |     17875770|

Output File Names:
/media/science/microbiome/mothur/stability.trim.contigs.good.unique.summary

It took 65 secs to summarize 17875770 sequences.


## Align sequences to SILVA v132
```
align.seqs(fasta=stability.trim.contigs.good.unique.fasta, reference=silva.seed_v132.align)
summary.seqs(fasta=stability.trim.contigs.good.unique.align, count=stability.trim.contigs.good.count_table)
```

Using 24 processors.

||Start|End|NBases|  Ambigs|  Polymer| NumSeqs|
|---|---|---|---|---|---|---|
|Minimum:|   0|  0|  0|  0|  1|  1|
|2.5%-tile:| 10368|25437|303|0|  4|  446895|
|25%-tile:|  10369|25438|304|0|  4|  4468943|
|Median:| 10369|25438|304|0|  4|  8937886|
|75%-tile:|  10369|25438|304|0|  5|  13406828|
|97.5%-tile:|10370|25440|305|0|  6|  17428876|
|Maximum:|   43116|43116|499|0|  227|17875770|
|Mean:|10377|25441.1| 304.233 0|  4.50498|
|# of unique seqs:|  9879082|
|total # of seqs:|   17875770|

Output File Names:
/media/science/microbiome/mothur/stability.trim.contigs.good.unique.summary

It took 8342 secs to summarize 17875770 sequences.



### Cleanup of aligned sequences
```
screen.seqs(fasta=stability.trim.contigs.good.unique.align, count=stability.trim.contigs.good.count_table, summary=stability.trim.contigs.good.unique.summary, start=10368, end=25440, maxhomop=8)
filter.seqs(fasta=stability.trim.contigs.good.unique.good.align, vertical=T, trump=.)
```