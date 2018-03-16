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
summary.seqs(fasta=stability.trim.contigs.good.unique.align, count=stability.trim.contigs.good.count_table)
```

Using 24 processors.

||Start|End|NBases|Ambigs|Polymer|NumSeqs|
|---|---|---|---|---|---|---|
|Minimum:|0|0|0|0|1|1|
|2.5%-tile:|1|13425|292|0|4|441822|
|25%-tile:|1|13425|293|0|4|4418216|
|Median: |1|13425|293|0|4|8836432|
|75%-tile:|1|13425|293|0|5|13254648|
|97.5%-tile:|1|13425|294|0|6|17231042|
|Maximum:|13425|13425|299|0|18|17672863|
|Mean:|1.3175|13424.2|292.988|0|4.50204|
|# of unique seqs:|9693329|
|total # of seqs:|17672863|

Output File Names: 
/media/science/microbiome/mothur/stability.trim.contigs.good.unique.summary

It took 1713 secs to summarize 17672863 sequences.

```
screen.seqs(fasta=stability.trim.contigs.good.unique.align, count=stability.trim.contigs.good.count_table, summary=stability.trim.contigs.good.unique.summary, start=1, end=13425, maxhomop=8)
summary.seqs(fasta=current, count=current)
```

Using 24 processors.

||Start|End|NBases|Ambigs|Polymer|NumSeqs|
|---|---|---|---|---|---|---|
|Minimum:|1|13425|273|0|3|1|
|2.5%-tile:|1|13425|292|0|4|441635|
|25%-tile:|1|13425|293|0|4|4416347|
|Median: |1|13425|293|0|4|8832694|
|75%-tile:|1|13425|293|0|5|13249040|
|97.5%-tile:|1|13425|294|0|6|17223752|
|Maximum:|1|13425|299|0|8|17665386|
|Mean:|1|13425|293.001|0|4.50118|
|# of unique seqs:|9686064|
|total # of seqs:|17665386|

Output File Names: 
/media/science/microbiome/mothur/stability.trim.contigs.good.unique.good.summary

It took 1657 secs to summarize 17665386 sequences.

```
filter.seqs(fasta=stability.trim.contigs.good.unique.good.align, vertical=T, trump=.)
```

Length of filtered alignment: 674
Number of columns removed: 12751
Length of the original alignment: 13425
Number of sequences used to construct filter: 9686064

```
unique.seqs(fasta=stability.trim.contigs.good.unique.good.filter.fasta, count=stability.trim.contigs.good.good.count_table)
pre.cluster(fasta=stability.trim.contigs.good.unique.good.filter.unique.fasta, count=stability.trim.contigs.good.unique.good.filter.count_table, diffs=2)
summary.seqs()
```
Using 24 processors.
[WARNING]: This command can take a namefile and you did not provide one. The current namefile is /media/science/microbiome/mothur/stability.trim.contigs.good.names which seems to match /media/science/microbiome/mothur/stability.trim.contigs.good.unique.good.filter.unique.precluster.fasta.

||Start|End|NBases|Ambigs|Polymer|NumSeqs|
|---|---|---|---|---|---|---|
|Minimum:|1|674|273|0|3|1|
|2.5%-tile:|1|674|292|0|4|78424|
|25%-tile:|1|674|293|0|4|784236|
|Median: |1|674|293|0|4|1568472|
|75%-tile:|1|674|293|0|5|2352708|
|97.5%-tile:|1|674|294|0|6|3058520|
|Maximum:|1|674|299|0|8|3136943|
|Mean:|1|674|293.009|0|4.47774|
|# of Seqs:|3136943|

Output File Names: 
/media/science/microbiome/mothur/stability.trim.contigs.good.unique.good.filter.unique.precluster.summary

It took 16 secs to summarize 3136943 sequences.
###Cleanup and remove any chimeric sequences
```
chimera.vsearch(fasta=stability.trim.contigs.good.unique.good.filter.unique.precluster.fasta, count=stability.trim.contigs.good.unique.good.filter.unique.precluster.count_table, dereplicate=t)
remove.seqs(fasta=stability.trim.contigs.good.unique.good.filter.unique.precluster.fasta, accnos=stability.trim.contigs.good.unique.good.filter.unique.precluster.denovo.vsearch.accnos)
```
##Classification of sequences
```
classify.seqs(fasta=stability.trim.contigs.good.unique.good.filter.unique.precluster.pick.fasta, count=stability.trim.contigs.good.unique.good.filter.unique.precluster.denovo.vsearch.pick.count_table, reference=trainset9_032012.pds.fasta, taxonomy=trainset9_032012.pds.tax, cutoff=80)
remove.lineage(fasta=stability.trim.contigs.good.unique.good.filter.unique.precluster.pick.fasta, count=stability.trim.contigs.good.unique.good.filter.unique.precluster.denovo.vsearch.pick.count_table, taxonomy=stability.trim.contigs.good.unique.good.filter.unique.precluster.pick.pds.wang.taxonomy, taxon=Chloroplast-Mitochondria-unknown-Archaea-Eukaryota)
summary.tax(taxonomy=current, count=current)
```

##OTU Analysis
###Distance Analysis
```
cluster.split(fasta=stability.trim.contigs.good.unique.good.filter.unique.precluster.pick.pick.fasta, count=stability.trim.contigs.good.unique.good.filter.unique.precluster.denovo.vsearch.pick.pick.count_table, taxonomy=stability.trim.contigs.good.unique.good.filter.unique.precluster.pick.pds.wang.pick.taxonomy, splitmethod=classify, taxlevel=4, cutoff=0.03)
```