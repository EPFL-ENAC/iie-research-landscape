SELECT UnitInitials, PageTitleDisplay, Score
FROM Edges_N_Unit_N_Concept_T_Research e
JOIN Nodes_N_Unit u USING (UnitID)
JOIN Nodes_N_Concept c USING (PageID)
WHERE u.UnitPath LIKE '%> IIE%'