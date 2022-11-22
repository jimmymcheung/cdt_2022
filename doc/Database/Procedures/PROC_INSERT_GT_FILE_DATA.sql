create or replace procedure PROC_INSERT_GT_FILE_DATA(
	FILE_ID text[],
	RSID text[],
	CHROMOSOME text[],
	POSITION int[],
	GENOTYPE text[],
	PUBMEDID int[],
	DOI text[],
	TITLE text[],
	CITATIONS int[],
	AUTHOR text[],
	YEAR int[],
	JOURNA text[],
	TRUST_SCORE text[]
)
language plpgsql
as $$
begin

INSERT INTO gt_file_data(file_id, file_rsid, chromosome, "POSITION", genotype)
VALUES()

	IF EXISTS (
		SELECT FROM gt_file_data g WHERE g.file_rsid in (SELECT unnest(RSID))
	) OR EXISTS (
		SELECT FROM id_search i WHERE i.search_rsid in (SELECT unnest(RSID))
	)
	THEN
	
  	INSERT INTO rsid_article(rsid, pubmed_id)
   	SELECT unnest(RSID), unnest(PUBMEDID);
	
  	ELSE
	
	raise notice 'Foreign key violation, RSID was not present in table gt_file_data or id_search';
	
	END IF;

    
    commit; 
    end;
    $$;  