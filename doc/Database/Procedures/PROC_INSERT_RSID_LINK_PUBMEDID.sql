create or replace procedure PROC_INSERT_RSID_LINK_PUBMEDID(
	RSID text[],
	PUBMEDID int[],
	DOI text[],
	TITLE text[],
	CITATIONS int[],
	AUTHOR text[],
	YEAR int[],
	JOURNAL text[],
	TRUST_SCORE text[]
)
language plpgsql
as $$
begin





INSERT INTO article(pubmed_id, doi, title, citaties, author, year, journal, trust_score)
SELECT UNNEST(PUBMEDID), UNNEST(DOI), UNNEST(TITLE), UNNEST(CITATIONS), UNNEST(AUTHOR), UNNEST(YEAR), UNNEST(JOURNAL), UNNEST(TRUST_SCORE);

CALL PROC_LINK_RSID_PUBID(RSID, PUBMEDID);


commit; 
end;
$$;  




-- CALL PROC_INSERT_RSID_LINK_PUBMEDID('{1}', '{12345}', '{123}', '{testtiet}', '{6}', '{hans}', '{2016}', '{volksbuurt}', '{goed}')










