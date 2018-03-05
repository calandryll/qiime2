# mothur Analysis
Analysis was carried out by using a mixture of [mothur's MiSeq SOP](https://www.mothur.org/wiki/MiSeq_SOP) and [this protocol](https://www.protocols.io/view/week-8-classifying-taxonomy-of-short-reads-with-mo-g7tbznn).  Raw files from [Novogene](https://en.novogene.com) were renamed and modified using the [renamer.py](https://github.com/calandryll/qiime2/blob/master/mothur/renamer.py) script to rename files and associated reads.


# New Analysis
Based more on the MiSeq SOP.
## Sequence Cleanup
### Make File and Contigs
```
make.file(inputdir=/media/science/microbiome/mothur, type=gz, prefix=stability)
make.contigs(file=stability.files, processors=24)
```
### Filter out oddball lengths
```
summary.seqs()
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

It took 23 secs to summarize 18923073 sequences.

```
screen.seqs(fasta=stability.trim.contigs.fasta, group=stability.contigs.groups, summary=stability.trim.contigs.summary, maxambig=0, maxlength=305, minlength=295)
summary.seqs()
```

Using 24 processors.

||Start|End|NBases|Ambigs|Polymer|NumSeqs|
|---|---|---|---|---|---|---|
|Minimum:|1|295|295|0|3|1|
|2.5%-tile:|1|303|303|0|4|441822|
|25%-tile:|1|304|304|0|4|4418216|
|Median: |1|304|304|0|4|8836432|
|75%-tile:|1|304|304|0|5|13254648|
|97.5%-tile:|1|305|305|0|6|17231042|
|Maximum:|1|305|305|0|18|17672863|
|Mean:|1|303.979|303.979|0|4.50458|
|# of Seqs:|17672863|

Output File Names: 
/media/science/microbiome/mothur/stability.trim.contigs.good.summary

```
unique.seqs(fasta=stability.trim.contigs.good.fasta)
summary.seqs()
```
Using 24 processors.

||Start|End|NBases|Ambigs|Polymer|NumSeqs|
|---|---|---|---|---|---|---|
|Minimum:|1|295|295|0|3|1|
|2.5%-tile:|1|303|303|0|4|242334|
|25%-tile:|1|304|304|0|4|2423333|
|Median: |1|304|304|0|4|4846665|
|75%-tile:|1|304|304|0|5|7269997|
|97.5%-tile:|1|305|305|0|6|9450996|
|Maximum:|1|305|305|0|18|9693329|
|Mean:|1|303.955|303.955|0|4.4989|
|# of Seqs:|9693329|

Output File Names: 
/media/science/microbiome/mothur/stability.trim.contigs.good.unique.summary

```
count.seqs(name=stability.trim.contigs.good.names, group=stability.contigs.good.groups)
summary.seqs(count=stability.trim.contigs.good.count_table)
```

Using 24 processors.

||Start|End|NBases|Ambigs|Polymer|NumSeqs|
|---|---|---|---|---|---|---|
|Minimum:|1|295|295|0|3|1|
|2.5%-tile:|1|303|303|0|4|441822|
|25%-tile:|1|304|304|0|4|4418216|
|Median: |1|304|304|0|4|8836432|
|75%-tile:|1|304|304|0|5|13254648|
|97.5%-tile:|1|305|305|0|6|17231042|
|Maximum:|1|305|305|0|18|17672863|
|Mean:|1|303.979|303.979|0|4.50458|
|# of unique seqs:|9693329|
|total # of seqs:|17672863|

Output File Names: 
/media/science/microbiome/mothur/stability.trim.contigs.good.unique.summary


## Align sequences to SILVA
```
align.seqs(fasta=stability.trim.contigs.good.unique.fasta, reference=silva.v4.fasta)
```


