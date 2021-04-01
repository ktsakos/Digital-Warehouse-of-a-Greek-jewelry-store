CREATE TABLE public."Categories"
(
  "Name" character varying(30) NOT NULL,
  CONSTRAINT "Categorie_pkey" PRIMARY KEY ("Name")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."Categories"
  OWNER TO postgres;

CREATE TABLE public."Supplier"
(
  "Company" character varying(30) NOT NULL,
  "Name" character varying(30),
  "Surname" character varying(30),
  "Address" character varying(30),
  "Phone" character varying(15),
  "Mobile Phone" character varying(15),
  "Bank Account" character varying(50),
  "Bank Account2" character varying(50),
  CONSTRAINT pkey_supplier PRIMARY KEY ("Company")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."Supplier"
  OWNER TO postgres;

CREATE TABLE public."Gold Product"
(
  "Categorie" character varying(30) NOT NULL,
  "Date" date,
  "Price" double precision,
  "Color" character varying(15),
  "Company" character varying(30) NOT NULL,
  "Quality" character varying(10) NOT NULL,
  "Weight" double precision NOT NULL,
  CONSTRAINT "fk1_GP" FOREIGN KEY ("Categorie")
      REFERENCES public."Categories" ("Name") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT "fk2_GP" FOREIGN KEY ("Company")
      REFERENCES public."Supplier" ("Company") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=TRUE
);
ALTER TABLE public."Gold Product"
  OWNER TO postgres;

-- Index: public."fki_fk1_GP"

-- DROP INDEX public."fki_fk1_GP";

CREATE INDEX "fki_fk1_GP"
  ON public."Gold Product"
  USING btree
  ("Categorie" COLLATE pg_catalog."default");

-- Index: public."fki_fk2_GP"

-- DROP INDEX public."fki_fk2_GP";

CREATE INDEX "fki_fk2_GP"
  ON public."Gold Product"
  USING btree
  ("Company" COLLATE pg_catalog."default");



CREATE TABLE public."Silver Product"
(
  "Categorie" character varying(30) NOT NULL,
  "Date" date,
  "Price" double precision NOT NULL,
  "Color" character varying(15),
  "Company" character varying(30) NOT NULL,
  CONSTRAINT fk1 FOREIGN KEY ("Categorie")
      REFERENCES public."Categories" ("Name") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT fk2 FOREIGN KEY ("Company")
      REFERENCES public."Supplier" ("Company") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=TRUE
);
ALTER TABLE public."Silver Product"
  OWNER TO postgres;

-- Index: public.fki_fk1

-- DROP INDEX public.fki_fk1;

CREATE INDEX fki_fk1
  ON public."Silver Product"
  USING btree
  ("Categorie" COLLATE pg_catalog."default");

-- Index: public.fki_fk2

-- DROP INDEX public.fki_fk2;

CREATE INDEX fki_fk2
  ON public."Silver Product"
  USING btree
  ("Company" COLLATE pg_catalog."default");

