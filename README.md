# Description
## 20211213 version (new)
Recently I find that my colleagues and friends have many small demands to check something in the genome. These demands are not difficult to satisfy by several lines of codes, but may be obstacles for those who seldom write codes. Therefore I decide to store my codes for all kinds of interesting or boring small functions here. The name "Genome_counter" will be kept, as that's the first function in this package and I don't want to set a limitation of what the future functions could do.
## 20211203 version (old)
This repository is a small tool to count the frequency of a specific fragment in a genome. At the same time, this repository explains what `if __name__=="__main__":` is doing. This time I didn't make the codes into a installable package as the functions of the codes are very simple.

# 1. Fragment counter
This is a small tool to count the frequency of a specific fragment in a genome. It could be used to search for genome targeting probes.
## 1.1 If you just want to search for very few fragments in a genome
In this case, you don't need to make a modified genome file, as it will occupy a lot of storage. Run the following command directly
```bash
python count_the_fragment.py -r reference.fa -f ACGTACGT
```
Replace `reference.fa` with the name of your reference, which is supposed to be in the same folder as the script. Replace `ACGTACGT` with the fragment you want to search. It will take seconds to minutes to run depending on the size of the genome and the length of the fragment. The output is the frequency of the fragment in the genome. Both plus and minus strands are considered.

## 1.2 If you will search for many fragments in the same genome
In this case, a prepared genome file is supposed to be made in advance so that you don't need to make it every time you run the searching. Run the following command
```bash
python prepare_the_reference.py -r reference.fa -o out_put
```
Replace `reference.fa` with the name of your reference, which is supposed to be in the same folder as the script. Replace `out_put` with the name of the output file you want. A suffix is not needed for this file and it will be added automatically. This parameter is optional. It will take seconds to minutes to run depending on the size of the genome.

After the genome file is prepared. Run the following command
```bash
python count_the_fragment.py -p out_put.pkl -f ACGTACGT
```
Replace `out_put.pkl` with the name of the prepared genome file. Replace `ACGTACGT` with the fragment you want to search.

# 2. Sequence printer
This is a small tool to print the sequence in the genome, based on the range you provide. It could be used to print the flanking sequences of a gene, which may not be provided in the information of that gene. There are also two modes with/without a pre-treated genome reference file and they work exactly the same way as above. Therefore here we only show how to check the content of the sequence with a prepared reference file. Run the following command
```bash
python get_the_sequence.py -p out_put.pkl -g chr1:+:12345678:12345688 
```
Replace `out_put.pkl` with the name of the prepared genome file. Replace `chr1:+:12345678:12345688` with the region you are interested in. The argument contain the name of the chromosome, the strand, the starting base and the ending base separated by a colon.

# Explanation (nothing biology below)
When you run the `count_the_fragment.py` without a prepared genome file, the program will import the function `prepare_ref` from `prepare_the_reference.py`. In this case, the content after `if __name__=="__main__":` in `prepare_the_reference.py` will not run, as `__name__` will be the name of the file `prepare_the_reference` at that time. It only serves as a function provider. However, you may also run `prepare_the_reference.py` by itself directly. In this case the content after `if __name__=="__main__":` will run.

