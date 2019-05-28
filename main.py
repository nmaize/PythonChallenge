#Dependencies
import csv
import os

#Load and output files
Loadfile = os.path.join("Resources", "election_data.csv")
Outputfile = os.path.join("Resources", "election.txt")

#Create variables for calculations
votes = 0
candidate_options = []
c_votes = {}
winning_candidate = ""
counter = 0

# Read the csv and convert into list of dictionaries
with open(Loadfile) as raw_data:
    readfile = csv.reader(raw_data)

    headrow = next(readfile)

    for row in readfile:

        votes = votes + 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            c_votes[candidate_name] = 0
            c_votes[candidate_name] = c_votes[candidate_name] + 1

#Print
with open(Outputfile, "w") as txt_file:

    # Print vote
    results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {votes}\n"
        f"-------------------------\n")
    print(results, end="")

    # Save
    txt_file.write(results)

    # Loop through the counts
    for candidate in c_votes:

        #Cal
        votes = c_votes.get(candidate)
        vote_percentage = float(votes) / float(votes) * 100

        #Win cal
        if (votes > counter):
            counter = votes
            winning_candidate = candidate

        # Print and format
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save text file
        txt_file.write(voter_output)

    #Print results
    winning = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning)

    # Save text file
    txt_file.write(winning)
    