EDIT 1:

The index "TRUST_ARTICLE_FK" must be dropped

--------------------------------------------------
EDIT 2:

A constraint must be added to the table "GT_FILE_DATA", paste
the following line into the create script:

unique (FILE_RSID)

--------------------------------------------------
EDIT 3:

Add the correct column to the "FK_ARTICLE__TRUST_ART_TRUST_CR" 
forein key. For both child and parent table the column name is
"CRITERIA_ID"