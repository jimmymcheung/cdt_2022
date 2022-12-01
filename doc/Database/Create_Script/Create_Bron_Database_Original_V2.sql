/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     30-11-2022 15:12:30                          */
/*==============================================================*/


drop index IF EXISTS ARTICLE_PK CASCADE;

drop table IF EXISTS ARTICLE CASCADE;

drop index IF EXISTS TRUST_ARTICLE_FK CASCADE;

drop index IF EXISTS ARTICLE_TRUST_CRITERIA_PK CASCADE;

drop table IF EXISTS ARTICLE_TRUST_CRITERIA CASCADE;

drop index IF EXISTS AUTHOR_PK CASCADE;

drop table IF EXISTS AUTHOR CASCADE;

drop index IF EXISTS GT_FILE_PK CASCADE;

drop table IF EXISTS GT_FILE CASCADE;

drop index IF EXISTS GT_DATA_FK CASCADE;

drop index IF EXISTS GT_FILE_DATA_PK CASCADE;

drop table IF EXISTS GT_FILE_DATA CASCADE;

drop index IF EXISTS ID_SEARCH_PK CASCADE;

drop table IF EXISTS ID_SEARCH CASCADE;

drop index IF EXISTS JOURNAL_PK CASCADE;

drop table IF EXISTS JOURNAL CASCADE;

drop index IF EXISTS ARTICLE_PROBABILITIES_FK CASCADE;

drop index IF EXISTS PROBABILITIES_PK CASCADE;

drop table IF EXISTS PROBABILITIES CASCADE;

drop index IF EXISTS RSID_ARTICLE_FK CASCADE;

drop index IF EXISTS ID_SEARCH_ARTICLES_FK CASCADE;

drop index IF EXISTS RSID_ARTICLE_PK CASCADE;

drop table IF EXISTS RSID_ARTICLE CASCADE;

drop table IF EXISTS TRUST_CRITERIA CASCADE;

/*==============================================================*/
/* Table: ARTICLE                                               */
/*==============================================================*/
create table ARTICLE (
   PUBMED_ID            INT4                 not null,
   DOI                  VARCHAR(1024)        null,
   TITLE                VARCHAR(1024)        not null,
   ABSTRACT             VARCHAR(2048)        null,
   CITATIES             INT4                 null,
   YEAR                 INT4                 null,
   TRUST_SCORE          VARCHAR(1024)        null,
   constraint PK_ARTICLE primary key (PUBMED_ID)
);

/*==============================================================*/
/* Index: ARTICLE_PK                                            */
/*==============================================================*/
create unique index ARTICLE_PK on ARTICLE (
PUBMED_ID
);

/*==============================================================*/
/* Table: ARTICLE_TRUST_CRITERIA                                */
/*==============================================================*/
create table ARTICLE_TRUST_CRITERIA (
   PUBMED_ID            INT4                 not null,
	criteria_id         VARCHAR(10)          not null,
   constraint PK_ARTICLE_TRUST_CRITERIA primary key (PUBMED_ID)
);

/*==============================================================*/
/* Index: ARTICLE_TRUST_CRITERIA_PK                             */
/*==============================================================*/
create unique index ARTICLE_TRUST_CRITERIA_PK on ARTICLE_TRUST_CRITERIA (
PUBMED_ID
);


/*==============================================================*/
/* Table: AUTHOR                                                */
/*==============================================================*/
create table AUTHOR (
   LASTNAME             VARCHAR(1024)        not null,
   FORENAME             VARCHAR(1024)        not null,
   INITIALS             VARCHAR(1024)        not null,
   PUBMED_ID            INT4                 null,
   constraint PK_AUTHOR primary key (LASTNAME, FORENAME, INITIALS)
);

/*==============================================================*/
/* Index: AUTHOR_PK                                             */
/*==============================================================*/
create unique index AUTHOR_PK on AUTHOR (
LASTNAME,
FORENAME,
INITIALS
);

/*==============================================================*/
/* Table: GT_FILE                                               */
/*==============================================================*/
create table GT_FILE (
   FILE_ID              VARCHAR(1024)        not null,
   DATE                 DATE                 null,
   constraint PK_GT_FILE primary key (FILE_ID)
);

/*==============================================================*/
/* Index: GT_FILE_PK                                            */
/*==============================================================*/
create unique index GT_FILE_PK on GT_FILE (
FILE_ID
);

/*==============================================================*/
/* Table: GT_FILE_DATA                                          */
/*==============================================================*/
create table GT_FILE_DATA (
   FILE_ID              VARCHAR(1024)        not null,
   FILE_RSID            VARCHAR(11)          not null,
   CHROMOSOME           VARCHAR(2)           null,
   "POSITION"           INT4                 null,
   GENOTYPE             VARCHAR(2)           null,
   constraint PK_GT_FILE_DATA primary key (FILE_ID, FILE_RSID),
   unique (FILE_RSID)
);

/*==============================================================*/
/* Index: GT_FILE_DATA_PK                                       */
/*==============================================================*/
create unique index GT_FILE_DATA_PK on GT_FILE_DATA (
FILE_ID,
FILE_RSID
);

/*==============================================================*/
/* Index: GT_DATA_FK                                            */
/*==============================================================*/
create  index GT_DATA_FK on GT_FILE_DATA (
FILE_ID
);

/*==============================================================*/
/* Table: ID_SEARCH                                             */
/*==============================================================*/
create table ID_SEARCH (
   SEARCH_RSID          VARCHAR(11)          not null,
   DATE                 DATE                 not null,
   constraint PK_ID_SEARCH primary key (SEARCH_RSID)
);

/*==============================================================*/
/* Index: ID_SEARCH_PK                                          */
/*==============================================================*/
create unique index ID_SEARCH_PK on ID_SEARCH (
SEARCH_RSID
);

/*==============================================================*/
/* Table: JOURNAL                                               */
/*==============================================================*/
create table JOURNAL (
   ISSN                 VARCHAR(10)          not null,
   PUBMED_ID            INT4                 null,
   TITLE                VARCHAR(1024)        not null,
   PEER_REVIEWED        BOOL                 null,
   constraint PK_JOURNAL primary key (ISSN)
);

/*==============================================================*/
/* Index: JOURNAL_PK                                            */
/*==============================================================*/
create unique index JOURNAL_PK on JOURNAL (
ISSN
);

/*==============================================================*/
/* Table: PROBABILITIES                                         */
/*==============================================================*/
create table PROBABILITIES (
   PUBMED_ID            INT4                 not null,
   DISEASE              VARCHAR(1024)        not null,
   COUNT                INT4                 null,
   constraint PK_PROBABILITIES primary key (PUBMED_ID, DISEASE)
);

/*==============================================================*/
/* Index: PROBABILITIES_PK                                      */
/*==============================================================*/
create unique index PROBABILITIES_PK on PROBABILITIES (
PUBMED_ID,
DISEASE
);

/*==============================================================*/
/* Index: ARTICLE_PROBABILITIES_FK                              */
/*==============================================================*/
create  index ARTICLE_PROBABILITIES_FK on PROBABILITIES (
PUBMED_ID
);

/*==============================================================*/
/* Table: RSID_ARTICLE                                          */
/*==============================================================*/
create table RSID_ARTICLE (
   RSID                 VARCHAR(11)          not null,
   PUBMED_ID            INT4                 not null,
   constraint PK_RSID_ARTICLE primary key (RSID, PUBMED_ID)
);

/*==============================================================*/
/* Index: RSID_ARTICLE_PK                                       */
/*==============================================================*/
create unique index RSID_ARTICLE_PK on RSID_ARTICLE (
RSID,
PUBMED_ID
);

/*==============================================================*/
/* Index: RSID_ARTICLE_FK                                       */
/*==============================================================*/
create  index RSID_ARTICLE_FK on RSID_ARTICLE (
PUBMED_ID
);

/*==============================================================*/
/* Table: TRUST_CRITERIA                                        */
/*==============================================================*/
create table TRUST_CRITERIA (
   CRITERIA_ID          VARCHAR(1024)        null,
   MEANING              VARCHAR(1024)        null,
   SCORE_WEIGHT         INT4                 null
);

alter table ARTICLE_TRUST_CRITERIA
   add constraint FK_ARTICLE__ARTICLE_T_ARTICLE foreign key (PUBMED_ID)
      references ARTICLE (PUBMED_ID)
      on delete restrict on update restrict;

alter table ARTICLE_TRUST_CRITERIA
   add constraint FK_ARTICLE__TRUST_ART_TRUST_CR foreign key (CRITERIA_ID)
      references TRUST_CRITERIA (CRITERIA_ID)
      on delete restrict on update restrict;

alter table AUTHOR
   add constraint FK_AUTHOR_ARTICLE_A_ARTICLE foreign key (PUBMED_ID)
      references ARTICLE (PUBMED_ID)
      on delete restrict on update restrict;

alter table GT_FILE_DATA
   add constraint FK_GT_FILE__GT_DATA_GT_FILE foreign key (FILE_ID)
      references GT_FILE (FILE_ID)
      on delete restrict on update restrict;

alter table JOURNAL
   add constraint FK_JOURNAL_ARTICLE_J_ARTICLE foreign key (PUBMED_ID)
      references ARTICLE (PUBMED_ID)
      on delete restrict on update restrict;

alter table PROBABILITIES
   add constraint FK_PROBABIL_ARTICLE_P_ARTICLE foreign key (PUBMED_ID)
      references ARTICLE (PUBMED_ID)
      on delete restrict on update restrict;

alter table RSID_ARTICLE
   add constraint FK_RSID_ART_RSID_ARTI_ARTICLE foreign key (PUBMED_ID)
      references ARTICLE (PUBMED_ID)
      on delete restrict on update restrict;

