#!/usr/bin/python

import os, glob, subprocess
from pathlib import Path

raw_dir = '/media/science/microbiome/raw_data'
out_dir = '/media/science/microbiome/mothur'

fastq_files = sorted(glob.glob(raw_dir + "/*.fq.gz"))

trim = len(list(fastq_files))

for files in range(trim):
	sample_name = Path(fastq_files[files]).stem.rsplit('.', 1)[0]
	sample_name2 = sample_name.rsplit('_', 1)[0]
	sample_out = os.path.basename(fastq_files[files])
	print('Analyzing %s...' % (sample_name))
	file_out = out_dir + '/' + sample_out
	zcatstr = 'zcat ' + fastq_files[files]
	awk1 = '''awk \'{print (NR%4 == 1) ? "@'''
	awk2 = '''_" ++i : $0}\''''
	awkstr = awk1 + sample_name2 + awk2
	gzipstr = 'gzip -c > ' + file_out
	combined = zcatstr + ' | '  + awkstr + ' | '  + gzipstr
	subprocess.call(combined, shell = True)
