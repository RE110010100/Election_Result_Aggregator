-- Aggregating national results
INSERT INTO national_results (year, party, total_votes)
SELECT year, party_simplified, SUM(candidatevotes)
FROM election_data
GROUP BY year, party_simplified;

-- Aggregating state results
INSERT INTO state_results (year, state, party, total_votes)
SELECT year, state, party_simplified, SUM(candidatevotes)
FROM election_data
GROUP BY year, state, party_simplified;
