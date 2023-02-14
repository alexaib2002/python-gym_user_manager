-- Clients
CREATE TABLE IF NOT EXISTS public.clients
(
    nid character varying(9) COLLATE pg_catalog."default" NOT NULL,
    name character varying(40) COLLATE pg_catalog."default" NOT NULL,
    birth_date date NOT NULL,
    phone numeric NOT NULL,
    CONSTRAINT clients_pkey PRIMARY KEY (nid)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.clients
    OWNER to postgres;

-- Sport
CREATE TABLE IF NOT EXISTS public.sports
(
    name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    price numeric(4,0) NOT NULL,
    CONSTRAINT sports_pkey PRIMARY KEY (name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.sports
    OWNER to postgres;

-- Client-Sport
CREATE TABLE IF NOT EXISTS public.clients_sports
(
    client_nid character varying(9) COLLATE pg_catalog."default" NOT NULL,
    sport_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    sport_time character varying(5) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT client_nid_fk FOREIGN KEY (client_nid)
        REFERENCES public.clients (nid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT sport_name_fk FOREIGN KEY (sport_name)
        REFERENCES public.sports (name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.clients_sports
    OWNER to postgres;
