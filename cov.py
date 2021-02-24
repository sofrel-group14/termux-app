"""
USAGE:

1) Add ID to each branch in the function, and execute:

	System.err.println("TEST_COVERAGE_getCodeFromTermcap:1");

for each branch (ID = 1 in example above).

2) Run tests with -i flag to get error printouts, save output to file.
$ ./gradlew test -i &> testlog.txt

3) Grep the file to get relevant lines about test coverage, and save them to file.
$ cat testlog.txt | grep -e "TEST_COVERAGE_getCodeFromTermcap" > coverage.txt

4) Run this file to get coverage printouts.
$ python3 cov.py

"""

func_name = "getSelectedText"
nr_of_branches = 52
branches = [0]*(nr_of_branches+1) # +1 because of 1-indexing

def calc_branch_counts():
	with open('coverage.txt', 'r') as f:
		d = f.read()

	for line in d.split("\n"):
		if (line == ""):
			break

		branch_id = int(line.split(":")[-1])
		branches[branch_id] += 1

def print_branch_counts():
	print("Branch counts:")
	for i in range(1,nr_of_branches+1): # +1 because of 1-indexing
		print(str(i) + ": " + str(branches[i]))

def print_branch_coverage():
	branches_not_taken = list()
	nr_of_taken_branches = 0

	for i in range(1,nr_of_branches+1): # +1 because of 1-indexing
		if (branches[i] == 0):
			branches_not_taken.append(i)
		else:
			nr_of_taken_branches += 1

	print("Manually instrumented function: " + func_name)
	print("Branches not taken (IDs): ", end="")
	for b in branches_not_taken:
		print(b, end=", ")
	print("\n")

	percentage = int(100*nr_of_taken_branches / nr_of_branches)
	print("Out of " + str(nr_of_branches) + " branches, " + str(nr_of_taken_branches)  + " were taken (~" + str(percentage) + "%)")

calc_branch_counts()
print_branch_counts()
print_branch_coverage()