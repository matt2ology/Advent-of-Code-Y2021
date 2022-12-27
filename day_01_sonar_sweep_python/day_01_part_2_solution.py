#!/usr/bin/python3

def main():
    sonar_sweep_report_file = open("./../input_files/day_01/input.txt", "r")
    list_of_sonar_sweeps = []

    list_of_sonar_sweeps = sonar_sweep_report_file.readlines()

    print(list_of_sonar_sweeps)

    # depth measurement detector
    increased_depth_counter = 1
    print(
        "{} - (N/A - no previous measurement)".format(list_of_sonar_sweeps[0]))
    next_sweep = 0
    for sonar_depth in range(len(list_of_sonar_sweeps)-1):
        next_sweep = list_of_sonar_sweeps[sonar_depth + 1]
        if next_sweep > list_of_sonar_sweeps[sonar_depth]:
            print("{} - (increased)".format(next_sweep))
            increased_depth_counter += 1
        elif next_sweep < list_of_sonar_sweeps[sonar_depth]:
            print("{} - (decreased)".format(next_sweep))
        else:
            print("{} - (No Change)".format(next_sweep))

    print("there are {} measurements that are larger than the previous measurement".format(
        increased_depth_counter))


def count_increased_depth(list_of_sonar_sweeps):
    increased_depth_counter = 1
    next_sweep = 0
    for sonar_depth in range(len(list_of_sonar_sweeps)-1):
        next_sweep = list_of_sonar_sweeps[sonar_depth + 1]
        if next_sweep > list_of_sonar_sweeps[sonar_depth]:
            increased_depth_counter += 1
    return increased_depth_counter


if __name__ == "__main__":
    main()
