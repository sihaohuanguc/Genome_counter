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

def search_count(frag,all_ref):
    count=0
    for key in all_ref.keys():
        count+=all_ref[key].count(frag)
    return count

if __name__=="__main__":
    working_path=os.getcwd()
    p=argparse.ArgumentParser(description="This file is used to count the frequency of a certain fragment in a given genome.")
    p.add_argument("--reference","-r",type=str,help="Your reference file. It is supposed to be a FASTA file in current folder.")
    p.add_argument("--fragment","-f",required=True,type=str,help="The fragment you're going to search for. It should contain only A, C, G or T.")
    p.add_argument("--prepared_reference","-p",type=str,help="The file generated by 'prepare_the_reference.py'.")

    args=p.parse_args()

    if args.prepared_reference: # you may input a prepared ref dict here to save some time
        # it is prefered if a prepared genome file exists.
        in_file_name=args.prepared_reference
        search_fragment=args.fragment
        if in_file_name.split(".")[-1]=="pkl":
            in_anno=working_path+"/"+in_file_name
            all_ref=pickle.load(open(in_anno,"rb"))
            total_count=search_count(search_fragment,all_ref)+search_count(rev_comp(search_fragment),all_ref) # the genome has two strands
            print(total_count)
    elif args.reference: # you may make the ref dict here
        in_file_name=args.reference
        search_fragment=args.fragment # this argument is required
        if in_file_name.split(".")[-1] in ["fa","fasta","FA","FASTA"]:
            in_ref=working_path+"/"+in_file_name 
            all_ref=prepare_ref(in_ref)
            total_count=search_count(search_fragment,all_ref)+search_count(rev_comp(search_fragment),all_ref) # the genome has two strands
            print(total_count)
        else:
            print("Input reference in wrong format.")
    else:
        print("Missing or wrong parameters.")

        

            
