SELECT u.sigle, p.sciper, p.nom, p.prenom, p.nom_usuel, p.prenom_usuel, count(a.sciper) FROM CADI_ENAC_IT.Unites u
JOIN Persons p ON u.resp_unite=p.sciper
JOIN Accreds a ON u.id_unite=a.unite
WHERE level3=10265
GROUP BY u.id_unite
