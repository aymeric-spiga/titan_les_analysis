# titan_les_analysis
Python tools to analyze outputs from Titan LES

reduce files
find ../initial -name "wrfout*" -exec ncrcat -d Time,,,3 {} {}_red \;
