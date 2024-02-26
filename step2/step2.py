import subprocess

def extract_hashes(input_file, output_file):
    # awk command to just read a file
    # and only give the second colon delimited string
    # this will be the hash, all of them starting with $1$
    awk_command = f"awk -F: '{{print $2}}' {input_file}"

    subprocess.run(awk_command, shell=True, check=True, stdout=open(output_file, 'w'))

input_file = "crackme_shadow"
output_file = "step2_crackme_hashes_nodollar.txt"

extract_hashes(input_file, output_file)
