import sys
import gzip
import os
#infile = "1000genomes_vcfs/ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz"
#outfile = "1000genomes_vcfs/ALL.chr22.phase1_release_v3.20101123.snps_indels_svs.genotypes.chr_notation.vcf.gz"


infile = "/mnt/storage/harrietd/Melbourne_Genomics_Health_Alliance/compare_variants/filtered_15.75011883-75017951.ALL.chr15.integrated_phase1_v3.20101123.snps_indels_svs.genotypes.vcf.gz"
outfile = "/mnt/storage/harrietd/Melbourne_Genomics_Health_Alliance/compare_variants/VariantEval/filtered_15.75011883-75017951.ALL.chr15.integrated_phase1_v3.20101123.snps_indels_svs.genotypes.chr_notation.vcf.gz"

out_filetype = ""

if infile.endswith('.vcf.gzip') or infile.endswith('.vcf.gz'):
    vcf_in = gzip.open(infile, 'rb')
    out_filetype = '.vcf.gzip'
elif infile.endswith('.vcf'):
    vcf_in = open(infile)
    out_filetype = '.vcf'
else:
    print infile + " doesn't have a .vcf or .vcf.gz file extension. Are you sure it is a vcf file? Exiting."
    sys.exit()

if out_filetype == '.vcf.gzip':
    vcf_out = gzip.open(outfile, 'wb')
elif out_filetype == '.vcf':
    vcf_out = open(outfile, 'w')

for line in vcf_in:
    if not line.startswith("#"):
        vcf_out.write("chr"+line)
    else:
        vcf_out.write(line)

vcf_out.close()
vcf_in.close()
