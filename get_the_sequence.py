import os
import argparse
import pickle
from prepare_the_reference import prepare_ref

__author__ = "Sihao Huang"
__copyright__ = ""
__credits__ = []
__license__ = "GPL 2.0"
__version__ = "0.1"
__maintainer__ = "Sihao Huang"
__email__ = "sihaohuang1024@gmail.com"
__status__ = "Development"

def rev_comp(ref):
    rev_comp=[]
    # print(ref)
    for item in ref:
        if item=="A":
            rev_comp.append("T")
        elif item=="C":
            rev_comp.append("G")
        elif item=="G":
            rev_comp.append("C")
        elif item=="T":
            rev_comp.append("A")
        elif item=="N":
            rev_comp.append("N")
        else:
            print(item+": Wrong input!")
    rev_comp.reverse()
    return "".join(rev_comp)

def search_region(search_range,all_ref):
    elements=search_range.split(":")
    if not len(elements)==4:
        return "Search info in wrong format."
    chrom=elements[0]
    strand=elements[1]
    search_start=int(elements[2])
    search_end=int(elements[3])
    if not chrom in all_ref.keys():
        return "Chromosome name error."
    if not search_end>=search_start:
        return "Search indexes error."

    if strand=="+":
        return all_ref[chrom][(search_start-1):search_end]
    elif strand=="-":
        return rev_comp(all_ref[chrom][(search_start-1):search_end])
    else:
        return "Strand error."

if __name__=="__main__":
    working_path=os.getcwd()
    p=argparse.ArgumentParser(description="This file is used to print a given region in a given genome.")
    p.add_argument("--reference","-r",type=str,help="Your reference file. It is supposed to be a FASTA file in current folder.")
    p.add_argument("--region","-g",required=True,type=str,help="The chromosome, strand, start index and end index of the region you would like to print. Example: chr1:+:123456:123466. The start and end should be the index on the plus strand.")
    p.add_argument("--prepared_reference","-p",type=str,help="The file generated by 'prepare_the_reference.py'.")

    args=p.parse_args()

    if args.prepared_reference: # you may input a prepared ref dict here to save some time
        # it is prefered if a prepared genome file exists.
        in_file_name=args.prepared_reference
        search_range=args.region
        if in_file_name.split(".")[-1]=="pkl":
            in_anno=working_path+"/"+in_file_name
            all_ref=pickle.load(open(in_anno,"rb"))
            search_result=search_region(search_range,all_ref)
            print(search_result)
    elif args.reference: # you may make the ref dict here
        in_file_name=args.reference
        search_range=args.region # this argument is required
        if in_file_name.split(".")[-1] in ["fa","fasta","FA","FASTA"]:
            in_ref=working_path+"/"+in_file_name 
            all_ref=prepare_ref(in_ref)
            search_result=search_region(search_range,all_ref)
            print(search_result)
        else:
            print("Input reference in wrong format.")
    else:
        print("Missing or wrong parameters.")

        

            
