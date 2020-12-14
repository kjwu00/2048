"""
Use the printed output in the command line to create the
output file.
"""
import sys
import os

RESULTS_FOLDER = "../Experiment_Results/"

def main():
    in_file = sys.argv[1]
    out_file = sys.argv[2]

    # Read from the file
    f = open(in_file, "r")
    
    max_val_results = []
    total_sum_results = []
    total_merge_score = []

    i = 0
    for line in f:
        line.strip()
        parts = line.split(":")
        if i%3 == 0:
            max_val_results.append(int(parts[1]))
        elif i%3 == 1:
            total_sum_results.append(int(parts[1]))
        else: 
            total_merge_score.append(int(parts[1]))
        i+=1
    f.close()

    # Calculate the values
    if len(total_sum_results) == 0 or len(max_val_results) == 0 or  len(total_merge_score) == 0:
        print("Make sure there are values for all of the ")
        return 
    total_sum_avg = sum(total_sum_results) / len(total_sum_results)
    max_val_avg = sum(max_val_results) / len(max_val_results)
    total_merge_avg = sum(total_merge_score) / len(total_merge_score)

    # Write to the result file
    f = open(os.path.join(RESULTS_FOLDER, out_file), "w")
    f.write("avg max val: " + str(max_val_avg) + "\n") 
    f.write("avg total sum: " + str(total_sum_avg) + "\n")
    f.write("avg merge score: " + str(total_merge_avg) + "\n")
    f.write("max vals: " + str(max_val_results) + "\n") 
    f.write("total sums: " + str(total_sum_results) + "\n")
    f.write("total merge score: " + str(total_merge_score) + "\n")
    f.close()

if __name__ == '__main__':
    main()