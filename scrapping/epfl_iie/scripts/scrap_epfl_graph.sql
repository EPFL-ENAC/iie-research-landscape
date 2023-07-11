# Get list of IIE keywords from Unit-Concept
SELECT UnitInitials, PageTitleDisplay, Score
FROM Edges_N_Unit_N_Concept_T_Research e
JOIN Nodes_N_Unit u USING (UnitID)
JOIN Nodes_N_Concept c USING (PageID)
WHERE u.UnitPath LIKE '%> IIE%';


# Get list of IIE keywords from Person-Concept while removing wrong SCIPERs
# (TODO: find a way to replace homonyms instead)
SELECT UnitInitials, PageTitleDisplay, Score
FROM Edges_N_Person_N_Concept_T_Research person_concept
JOIN Edges_N_Person_N_Unit_T_CurrentPosition person_unit USING (SCIPER)
JOIN Nodes_N_Unit u USING (UnitID)
JOIN Nodes_N_Concept c USING (PageID)
WHERE u.UnitPath LIKE '%> IIE%' AND SCIPER!=206119;


# List people in unit
SELECT SCIPER, FirstName, LastName
FROM Edges_N_Person_N_Unit_T_CurrentPosition
INNER JOIN Nodes_N_Person USING (SCIPER)
WHERE UnitID="CRYOS";


# List keywords of person
SELECT PageTitleDisplay, Score
FROM Edges_N_Person_N_Concept_T_Research person_concept
JOIN Nodes_N_Concept c USING (PageID)
WHERE SCIPER=206119;
