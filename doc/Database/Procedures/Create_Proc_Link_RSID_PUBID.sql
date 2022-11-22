create or replace procedure PROC_LINK_RSID_PUBID(
	RSID text[], 
	PUBMEDID int[]
)
language plpgsql
as $$
begin

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