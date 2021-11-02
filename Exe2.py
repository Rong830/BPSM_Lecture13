dna="ATGCATCATG"
k=2 # kmer size
n=2 # more than this number found
segment_starts = list(range(0,len(dna),1))
#basic_fasta_header = '_window' + str(k) + '_offset' + str(n)
#segments_made = []
count = []
#fileswanted = 1
for seg_bits in segment_starts :
    tempseq = dna[seg_bits :seg_bits+k].upper()
#     segments_made = segments_made + [tempseq]
# the k-mers (e.g. 4-mers) that occur more than some number of times n 
    count.append(tempseq)
#count = count[(len(i) for i in count)==k]
for i in set(count) :
# the k-mers (e.g. 4-mers) that occur more than some number of times n 
    if count.count(i) > n:
        print(f'{i} appeaed more than {n} times')
# percentage GC content, convert float to integer value
#     tempGC = int(100 * (tempseq.count('G') + tempseq.count('C'))/len(tempseq) )
# make a fasta header line
#     descriptionline = 'dna'+str(len(segments_made))+'_'+tempseq+basic_fasta_header
#     fastaheader = '>'+descriptionline
#     print(len(segments_made),'\t',tempseq,'\t',tempGC)
# Question : do we want files written? Answer will be either True or False ('maybe' is NOT an option!)
#     if fileswanted == 1 :
# open the segment fastafiles
#        with open(descriptionline+'.fasta', 'w') as segmentfile :
# output to files
#          segmentfile.write(fastaheader+'\n'+tempseq)
#          allsegments.write(fastaheader+'\n'+tempseq+'\n\n')
#     else :
#        allsegments.close()

