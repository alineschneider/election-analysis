# Add our dependencies.
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.   
total_votes = 0

# Candidate options (list of unique candidate names) and candidate votes 
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# County list (list of unique counties) and vote count for each one
county_list = []
county_votes = {}

#County with largest turnout
top_county = ""
top_county_votes = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Get the county name from each row
        county_name = row[1]
        # If the county name does not match any existing county...
        if county_name not in county_list:
            # Add it to the list of counties
            county_list.append(county_name)
            # Begin tracking that county's vote count
            county_votes[county_name] = 0
        # Add a vote to that county's vote count (dictionary)
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Determine county with highest turnout, vote count and percents for each county
    #Iterate through county list
    for county in county_list:
        # Retrieve vote count for a specific county
        votes = county_votes[county]
        # Calculate percentage of votes from that county
        county_percentage = float(votes) / float(total_votes) * 100

        county_results = (f"{county}: {county_percentage:.2f}% ({votes:,})\n")
        # Print each county, their vote count and percentage to the terminal
        print(county_results)
        # Save the county results to the text file
        txt_file.write(county_results)

        #Determine county with highest turnout
        if votes > top_county_votes:
            top_county_votes = votes
            top_county = str(county)

    #Print county with highest turnout to the Terminal and to the text file
    largest_turnout = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {top_county}\n"
        f"-------------------------\n")
    print(largest_turnout)
    txt_file.write(largest_turnout)

    # Determine the percentage of votes for each candidate by looping through counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.    
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
    
