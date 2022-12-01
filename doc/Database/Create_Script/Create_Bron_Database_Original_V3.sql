/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     1-12-2022 13:17:59                           */
/*==============================================================*/


drop index if exists ARTICLE_PK cascade;

drop table if exists ARTICLE cascade;

drop index if exists TRUST_ARTICLE_FK cascade;

drop index if exists ARTICLE_TRUST_FK cascade;

drop index if exists ARTICLE_TRUST_CRITERIA_PK cascade;

drop table if exists ARTICLE_TRUST_CRITERIA cascade;

drop index if exists ARTICLE_AUTHOR_FK cascade;

drop index if exists AUTHOR_PK cascade;

drop table if exists AUTHOR cascade;

drop index if exists GT_FILE_PK cascade;

drop table if exists GT_FILE cascade;

drop index if exists GT_DATA_FK cascade;

drop index if exists GT_FILE_DATA_PK cascade;

drop table if exists GT_FILE_DATA cascade;

drop index if exists ID_SEARCH_PK cascade;

drop table if exists ID_SEARCH cascade;

drop index if exists ARTICLE_JOURNAL_FK cascade;

drop index if exists JOURNAL_PK cascade;

drop table if exists JOURNAL cascade;

drop index if exists ARTICLE_PROBABILITIES_FK cascade;

drop index if exists PROBABILITIES_PK cascade;

drop table if exists PROBABILITIES cascade;

drop index if exists RSID_ARTICLE_FK cascade;

drop index if exists FILE_ID_ARTICLES_FK cascade;

drop index if exists ID_SEARCH_ARTICLES_FK cascade;

drop index if exists RSID_ARTICLE_PK cascade;

drop table if exists RSID_ARTICLE cascade;

drop index if exists TRUST_CRITERIA_PK cascade;

drop table if exists TRUST_CRITERIA cascade;

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
   CRITERIA_ID          VARCHAR(1024)        not null,
   constraint PK_ARTICLE_TRUST_CRITERIA primary key (PUBMED_ID, CRITERIA_ID)
);

/*==============================================================*/
/* Index: ARTICLE_TRUST_CRITERIA_PK                             */
/*==============================================================*/
create unique index ARTICLE_TRUST_CRITERIA_PK on ARTICLE_TRUST_CRITERIA (
PUBMED_ID,
CRITERIA_ID
);

/*==============================================================*/
/* Index: ARTICLE_TRUST_FK                                      */
/*==============================================================*/
create  index ARTICLE_TRUST_FK on ARTICLE_TRUST_CRITERIA (
PUBMED_ID
);

/*==============================================================*/
/* Index: TRUST_ARTICLE_FK                                      */
/*==============================================================*/
create  index TRUST_ARTICLE_FK on ARTICLE_TRUST_CRITERIA (
CRITERIA_ID
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
/* Index: ARTICLE_AUTHOR_FK                                     */
/*==============================================================*/
create  index ARTICLE_AUTHOR_FK on AUTHOR (
PUBMED_ID
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
   constraint PK_GT_FILE_DATA primary key (FILE_ID, FILE_RSID)
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
/* Index: ARTICLE_JOURNAL_FK                                    */
/*==============================================================*/
create  index ARTICLE_JOURNAL_FK on JOURNAL (
PUBMED_ID
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
   SEARCH_RSID          VARCHAR(11)          not null,
   FILE_ID              VARCHAR(1024)        not null,
   FILE_RSID            VARCHAR(11)          not null,
   PUBMED_ID            INT4                 not null,
   constraint PK_RSID_ARTICLE primary key (FILE_ID, SEARCH_RSID, FILE_RSID, PUBMED_ID)
);

/*==============================================================*/
/* Index: RSID_ARTICLE_PK                                       */
/*==============================================================*/
create unique index RSID_ARTICLE_PK on RSID_ARTICLE (
FILE_ID,
SEARCH_RSID,
FILE_RSID,
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
   CRITERIA_ID          VARCHAR(1024)        not null,
   MEANING              VARCHAR(1024)        null,
   SCORE_WEIGHT         INT4                 null,
   constraint PK_TRUST_CRITERIA primary key (CRITERIA_ID)
);

/*==============================================================*/
/* Index: TRUST_CRITERIA_PK                                     */
/*==============================================================*/
create unique index TRUST_CRITERIA_PK on TRUST_CRITERIA (
CRITERIA_ID
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

