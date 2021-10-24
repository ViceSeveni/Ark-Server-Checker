# arklist
An Ark Survival Evolved lobby checking program. Provides a list of who is online based on a csv file of the cluster's battlemetrics id's. Also has a friends list capability to notify you that a specific player is online , pulled from another csv file with your friends steam/epic name and your personal name for them.

Instructions:
-You must create 2 CSV files 

-The first CSV file provides the server list with map names and id's. The ID's will be the last 7 digits of the URL for your cluster's map from BattleMetrics.

Example:

The Island, 1111111
Ragnarok, 2222222
Crystal Isles, 3333333

-The second CSV file provides information for the friends list. Include your friends epic/steam id, and then a nickname.

Example:

AlphaBob27, Bob
BeastQueen1, Mei Yin
HLNAsucks69, Rockwell

Input the CSV file paths into their corresponding variables in the source code. Make certain that they are raw strings (r'Text Here') or that you double every slash (\) in the path name.
