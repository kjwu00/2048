"""
Given a file in 'Experiment_Results', representing the results of a 
certain agent, calculate two additional evaluation metrics:
1) the number of games which reached 2048
2) the standard deviation of the merge scores.
"""
import statistics
import sys
import os

RESULTS_FOLDER = "../Experiment_Results/"

def main():
    file_name = NUM_ITERS = sys.argv[1]

    with open(os.path.join(RESULTS_FOLDER, file_name), 'r') as f:
        # Skip first three lines
        f.readline()
        f.readline()
        f.readline()

        # Get values
        max_vals = f.readline()
        total_sums = f.readline()
        merge_scores = f.readline()

    max_vals = max_vals.split(":")[1]
    max_vals = max_vals[2:-2]
    max_vals = max_vals.split(",")
    max_vals = [int(elem) for elem in max_vals]

    # Determine instances of 2048.
    count_2048 = 0
    for i in max_vals:
        if i >= 2048:
            count_2048 += 1
    print("2048 instances:", count_2048)

    # Calculate the standard deviation of the merge scores
    merge_scores = merge_scores.split(":")[1]
    merge_scores = merge_scores[2:-2]
    merge_scores = merge_scores.split(",")
    merge_scores = [int(elem) for elem in merge_scores]
    print("merge score std:", statistics.stdev(merge_scores))

if __name__ == '__main__':
    main()