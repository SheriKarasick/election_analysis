# ELECTION ANALYSIS FOR COLORADO BOARD OF ELECTIONS

# Add our dependencies.
import csv
import os

# Establish input and output paths
file_to_load = os.path.join("Resources/election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Declare variables, lists, and dictionaries

# Candidate Variables
total_votes = 0
winning_count = 0
winning_percentage = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""

# County Variables
total_count = 0
highest_count = 0
highest_percentage = 0
election_counties = []
county_votes = {}
turnout_county = ""

# Load data file and prepare for analysis:
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:  # Count total votes
        total_votes += 1
        county_name = row[1]
        if county_name not in election_counties:  # Build a list of counties in election
            election_counties.append(county_name)
            county_votes[county_name] = 0  # Begin tracking the counties vote count.
        county_votes[county_name] += 1  # Add a vote for each occurrence of county name.   
# Load file for saving outputs  
with open(file_to_save, "w") as txt_file:
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")    
        print(election_results, end="")
        txt_file.write(election_results) 

        # Analyze data by what took place in each county
        print("\nVotes by County:")
        for county in county_votes:
            votes = county_votes[county]  # Retrieve vote count of a county.
            vote_percentage = (votes) / (total_votes) * 100 #Calculate % of votes.
            county_results = (
                f"{county}: {vote_percentage:.1f}% ({votes:,})\n") # Define results format. 
            print(county_results)
            txt_file.write(county_results)

        for county in county_votes:
            votes = county_votes[county]  # Retrieve vote count of a county.
            vote_percentage = (votes) / (total_votes) * 100 #Calculate % of votes.
            if (votes > highest_count) and (vote_percentage > highest_percentage):
                highest_count = votes
                highest_percentage = vote_percentage    
                turnout_county = county
                
        turnout_county = (
        f"\n-------------------------"
        f"\nLargest County Turnout: {turnout_county}\n"
        f"-------------------------\n")
        print(turnout_county)
        txt_file.write(turnout_county)

        #Analyze candidate results
        with open(file_to_load) as election_data:
            file_reader = csv.reader(election_data)
            headers = next(file_reader)
            for row in file_reader: #run looped script to create candidate list
                candidate_name = row[2] #candidate variable location
                if candidate_name not in candidate_options: # build list of candidates
                    candidate_options.append(candidate_name) # add candidate name to candidate list
                    candidate_votes[candidate_name] = 0 # start votes at zero
                candidate_votes[candidate_name] += 1 #count votes for each candidate    
            for candidate in candidate_votes: #run loop to add a vote for each occurence of a candidate name
                votes = candidate_votes[candidate] #name vote count
                vote_percentage = (votes) / (total_votes) * 100 #calculate vote percentage
                candidate_results = (
                    f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n") # Print each candidate, their voter count, and percentage to the terminal.
                print(candidate_results)    
                txt_file.write(candidate_results) #write results to text file

                if (votes > winning_count) and (vote_percentage > winning_percentage):  # Determine winning vote count and candidate and Determine if the votes are greater than the winning count.     
                            #If True then set winning_count = votes and winning_percent = vote_percentage.
                    winning_count = votes # name variables for output file
                    winning_percentage = vote_percentage    
                    winning_candidate = candidate
            winning_candidate_summary = (
                f"\n-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
            print(winning_candidate_summary, end="") # Print the winning candidate's results to the output files.   
            txt_file.write(winning_candidate_summary)

