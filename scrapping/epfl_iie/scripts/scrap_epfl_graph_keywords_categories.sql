# Find unique keywords (concepts) and parent categories (~2500)
SELECT DISTINCT concept.PageTitle, category.CategoryName
FROM Edges_N_Unit_N_Concept_T_Research edge
JOIN Nodes_N_Unit unit USING (UnitID) # For filtering
JOIN Edges_N_Category_N_Concept_T_Original concept USING (PageID)
JOIN Nodes_N_Category category USING (CategoryID)
WHERE unit.UnitPath LIKE '%> IIE%';


# Same but unfiltered (~26000)
SELECT DISTINCT concept.PageTitle, category.CategoryName
FROM Edges_N_Category_N_Concept_T_Original concept
JOIN Nodes_N_Category category USING (CategoryID);


# List all categories (filtered in IIE) and their parents (430 entries)
WITH RECURSIVE filtered_categories AS (
	# For testing:
	# SELECT ChildCategoryID, ParentCategoryID
	# FROM Edges_N_Category_N_Category category_edge
	# WHERE category_edge.ChildCategoryID = "1000"

	SELECT DISTINCT ChildCategoryID, ParentCategoryID
	FROM Edges_N_Unit_N_Concept_T_Research edge
	JOIN Nodes_N_Unit unit USING (UnitID) # For filtering
	JOIN Edges_N_Category_N_Concept_T_Original concept USING (PageID)
	JOIN Edges_N_Category_N_Category category_edge on concept.CategoryID = category_edge.ChildCategoryID
	WHERE unit.UnitPath LIKE '%> IIE%'

	UNION ALL

	SELECT category_edge.ChildCategoryID, category_edge.ParentCategoryID
	FROM Edges_N_Category_N_Category category_edge
	JOIN filtered_categories ON filtered_categories.ParentCategoryID = category_edge.ChildCategoryID
)
# Convert IDs to names
SELECT DISTINCT category.CategoryName, parent.CategoryName
FROM filtered_categories edge
JOIN Nodes_N_Category category ON edge.ChildCategoryID = category.CategoryID
JOIN Nodes_N_Category parent ON edge.ParentCategoryID = parent.CategoryID;


# Same but unfiltered (1267 entries)
SELECT DISTINCT category.CategoryName, parent.CategoryName
FROM Edges_N_Category_N_Category edge
JOIN Nodes_N_Category category ON edge.ChildCategoryID = category.CategoryID
JOIN Nodes_N_Category parent ON edge.ParentCategoryID = parent.CategoryID;
