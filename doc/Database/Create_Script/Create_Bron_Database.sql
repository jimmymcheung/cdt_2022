/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     15-11-2022 12:54:12                          */
/*==============================================================*/


drop index if exists ARTICLE_PK;

drop table if exists ARTICLE;

drop index if exists TRUST_ARTICLE_FK;

drop index if exists ARTICLE_TRUST_CRITERIA_PK;

drop table if exists ARTICLE_TRUST_CRITERIA;

drop index if exists GT_FILE_PK;

drop table if exists GT_FILE;

drop index if exists GT_DATA_FK;

drop index if exists GT_FILE_DATA_PK;

drop table if exists GT_FILE_DATA;

drop index if exists ID_SEARCH_PK;

drop table if exists ID_SEARCH;

drop index if exists ARTICLE_PROBABILITIES_FK;

drop index if exists PROBABILITIES_PK;

drop table if exists PROBABILITIES;

drop index if exists RSID_ARTICLE_FK;

drop index if exists ID_SEARCH_ARTICLES_FK;

drop index if exists RSID_ARTICLE_PK;

drop table if exists RSID_ARTICLE;

drop index if exists TRUST_CRITERIA_PK;

drop table if exists TRUST_CRITERIA;

/*==============================================================*/
/* Table: ARTICLE                                               */
/*==============================================================*/
create table ARTICLE (
   PUBMED_ID            INT4                 not null,
   DOI                  VARCHAR(1024)        null,
   TITLE                VARCHAR(1024)        not null,
   CITATIES             INT4                 null,
   AUTHOR               VARCHAR(1024)        null,
   YEAR                 INT4                 null,
   JOURNAL              VARCHAR(1024)        null,
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
/* Index: ID_SEARCH_ARTICLES_FK                                 */
/*==============================================================*/
create  index ID_SEARCH_ARTICLES_FK on RSID_ARTICLE (
RSID
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

alter table GT_FILE_DATA
   add constraint FK_GT_FILE__GT_DATA_GT_FILE foreign key (FILE_ID)
      references GT_FILE (FILE_ID)
      on delete restrict on update restrict;

alter table PROBABILITIES
   add constraint FK_PROBABIL_ARTICLE_P_ARTICLE foreign key (PUBMED_ID)
      references ARTICLE (PUBMED_ID)
      on delete restrict on update restrict;

alter table RSID_ARTICLE
   add constraint FK_RSID_ART_FILE_ID_A_GT_FILE_ foreign key (RSID)
      references GT_FILE_DATA (FILE_RSID)
      on delete restrict on update restrict;

alter table RSID_ARTICLE
   add constraint FK_RSID_ART_ID_SEARCH_ID_SEARC foreign key (RSID)
      references ID_SEARCH (SEARCH_RSID)
      on delete restrict on update restrict;

alter table RSID_ARTICLE
   add constraint FK_RSID_ART_RSID_ARTI_ARTICLE foreign key (PUBMED_ID)
      references ARTICLE (PUBMED_ID)
      on delete restrict on update restrict;

