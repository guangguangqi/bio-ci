# Snakefile

# The target output we want to generate
rule all:
    input:
        "results/sample1_gc.txt"

# The data processing rule
rule calculate_gc:
    input:
        fasta = "data/sample1.fasta"
    output:
        report = "results/sample1_gc.txt"
    shell:
        # Snakemake automatically replaces {input.fasta} and {output.report} with paths
        "python count_bases.py {input.fasta} {output.report}"

