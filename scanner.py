import os

# 1. SETTINGS
target_site = "GTGCTTT" 
file_path = r"E:\miRNA target prediction\mart_export.txt"

print("--- PIPELINE STARTING ---")

# 2. CHECK FILE
if not os.path.exists(file_path):
    print(f"ERROR: Cannot find file at {file_path}")
else:
    print(f"File found. Scanning for {target_site}...")
    
    found_genes = set()
    current_header = ""
    current_sequence = ""
    total_processed = 0

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                # Check the sequence we just finished collecting
                if target_site in current_sequence:
                    # Extract gene name
                    parts = current_header.split('|')
                    gene_name = parts[2] if len(parts) > 2 else current_header
                    
                    if gene_name not in found_genes:
                        pos = current_sequence.find(target_site)
                        print(f"\n[!] MATCH: {gene_name} at index {pos}")
                        found_genes.add(gene_name)
                
                # Start fresh for the next gene
                current_header = line
                current_sequence = ""
                total_processed += 1
            else:
                current_sequence += line

    # Final check for the last gene in the file
    if target_site in current_sequence:
        parts = current_header.split('|')
        gene_name = parts[2] if len(parts) > 2 else current_header
        if gene_name not in found_genes:
            print(f"\n[!] MATCH: {gene_name}")

    print(f"\n--- SCAN FINISHED ---")
    print(f"Genes scanned: {total_processed}")
    print(f"Unique targets found: {len(found_genes)}")