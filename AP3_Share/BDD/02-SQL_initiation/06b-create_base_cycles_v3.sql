create  database cycle_v3 ;

use cycle_v3 ;

-- ============================================================
--   Table : FOURNISSEUR                                       
-- ============================================================
create table FOURNISSEUR
(
    RAISON_SOCIALE      VARCHAR(32)           not null ,
    NOM_DIRECTEUR  VARCHAR(32)                    ,
    primary key (RAISON_SOCIALE)
);


-- ============================================================
--   Table : TYPE_PIECE                                        
-- ============================================================
create table TYPE_PIECE
(
    REFERENCE_TYPE_PIECE  VARCHAR(10)           not null ,
    LIBELLE_TYPE_PIECE  VARCHAR(32)                    ,
    primary key (REFERENCE_TYPE_PIECE)
);


-- ============================================================
--   Table : COMMANDE                                          
-- ============================================================
create table COMMANDE
(
    REFERENCE_COMMANDE  INTEGER               not null ,
    RAISON_SOCIALE      VARCHAR(32)           not null ,
    DATE_COMMANDE       DATE                           ,
    DATE_LIVRAISON_SOUHAITEE  DATE                           ,
    primary key (REFERENCE_COMMANDE)
);

alter table COMMANDE add constraint CRS foreign key (RAISON_SOCIALE) references FOURNISSEUR (RAISON_SOCIALE) on delete restrict;

create index DESTINER_IDX on COMMANDE (RAISON_SOCIALE);


-- ============================================================
--   Table : LIGNE_COMMANDE                                    
-- ============================================================
create table LIGNE_COMMANDE
(
    REFERENCE_COMMANDE  INTEGER               not null ,
    NUMERO_LIGNE_COMMANDE  INTEGER               not null ,
    REFERENCE_TYPE_PIECE  VARCHAR(10)           not null ,
    QUANTITE_PIECES_COMMANDEES  INTEGER                        ,
    PRIX_PIECE          DECIMAL(7,2)                   ,
    primary key (REFERENCE_COMMANDE, NUMERO_LIGNE_COMMANDE)
);
alter table LIGNE_COMMANDE add constraint LCRTP foreign key (REFERENCE_TYPE_PIECE) references TYPE_PIECE (REFERENCE_TYPE_PIECE) on delete restrict;

alter table LIGNE_COMMANDE add constraint LCRC foreign key (REFERENCE_COMMANDE) references COMMANDE (REFERENCE_COMMANDE) on delete restrict;

create index COMMANDER_IDX on LIGNE_COMMANDE (REFERENCE_TYPE_PIECE);

create index DETAILLER_IDX on LIGNE_COMMANDE (REFERENCE_COMMANDE);


-- ============================================================
--   Table : PIECE                                             
-- ============================================================
create table PIECE
(
    REFERENCE_PIECE     INTEGER               not null ,
    REFERENCE_COMMANDE  INTEGER               not null ,
    NUMERO_LIGNE_COMMANDE  INTEGER               not null ,
    REFERENCE_TYPE_PIECE  VARCHAR(10)           not null ,
    primary key (REFERENCE_PIECE)
);

alter table PIECE add constraint PRC foreign key (REFERENCE_COMMANDE, NUMERO_LIGNE_COMMANDE) references LIGNE_COMMANDE (REFERENCE_COMMANDE, NUMERO_LIGNE_COMMANDE) on delete restrict;

alter table PIECE add constraint PRT foreign key (REFERENCE_TYPE_PIECE) references TYPE_PIECE (REFERENCE_TYPE_PIECE) on delete restrict;

create index APPARTENIR_IDX on PIECE (REFERENCE_COMMANDE, NUMERO_LIGNE_COMMANDE);

create index CARACTERISER_IDX on PIECE (REFERENCE_TYPE_PIECE);


-- ============================================================
--   Table : COMMERCIALISER                                    
-- ============================================================
create table COMMERCIALISER
(
    RAISON_SOCIALE      VARCHAR(32)           not null ,
    REFERENCE_TYPE_PIECE  VARCHAR(10)           not null ,
    primary key (RAISON_SOCIALE, REFERENCE_TYPE_PIECE)
);

alter table COMMERCIALISER add constraint CRC foreign key (RAISON_SOCIALE) references FOURNISSEUR (RAISON_SOCIALE) on delete restrict;

alter table COMMERCIALISER add constraint CRTP foreign key (REFERENCE_TYPE_PIECE) references TYPE_PIECE (REFERENCE_TYPE_PIECE) on delete restrict;

create index LIEN_12_IDX on COMMERCIALISER (RAISON_SOCIALE);

create index LIEN_13_IDX on COMMERCIALISER (REFERENCE_TYPE_PIECE);


