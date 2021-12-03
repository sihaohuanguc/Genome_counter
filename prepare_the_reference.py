import os
import pickle
import argparse

def prepare_ref(in_ref):
    with open(in_ref,"r") as f:
        all_ref={}
        chrom_name="delete_this"
        all_sequence=[]
        for line in f:
            if line[0]==">":
                all_sequence="".join(all_sequence)
                all_ref[chrom_name]=all_sequence
                chrom_name=line.strip(">").split(" ")[0]
                all_sequence=[]
            else:
                all_sequence.append(line.strip("\n"))
        all_sequence="".join(all_sequence)
        all_ref[chrom_name]=all_sequence
        del all_ref["delete_this"]
    # for key in all_ref.keys():
    #     print(key)
    #     print(all_ref[key][:100])  
    return all_ref

if __name__=="__main__":
    working_path=os.getcwd()
    p=argparse.ArgumentParser(description="This file is used to make a prepared genome.")
    p.add_argument("--reference","-r",required=True,type=str,help="Your reference file. It is supposed to be a FASTA file in current folder.")
    p.add_argument("--output_name","-o",type=str,help="The name of the output file. A suffix is not necessary.")

    args=p.parse_args()

    in_ref=working_path+"/"+args.reference
    if args.output_name:
        out_file=working_path+"/"+args.output_name
    else:
        out_file=working_path+"/"+".".join(args.reference.split(".")[:-1])+".pkl"
    all_ref=prepare_ref(in_ref)
    with open(out_file,"wb+") as out_f:
        out_f.write(pickle.dumps(all_ref))
        

            
