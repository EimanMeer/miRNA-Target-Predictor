# The context you found for BDNF: "CTTGGA CCTCGTGCTTT AAGTGCCTAC"
# The binding site part: "CGTGCTTT"

site = "CGTGCTTT"
gc_count = site.count("G") + site.count("C")
gc_percent = (gc_count / len(site)) * 100

print(f"Binding Site GC Content: {gc_percent:.2f}%")