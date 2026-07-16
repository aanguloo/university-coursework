--
-- PostgreSQL database dump
--

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

-- Started on 2026-04-12 23:19:26

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 886 (class 1247 OID 24586)
-- Name: fase_torneo; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.fase_torneo AS ENUM (
    'fase de grupos',
    'cuartos de final',
    'semifinal',
    'final'
);


ALTER TYPE public.fase_torneo OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 227 (class 1259 OID 32768)
-- Name: Capitanes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Capitanes" (
    id_jugador integer,
    id_equipo integer NOT NULL
);


ALTER TABLE public."Capitanes" OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16399)
-- Name: EQUIPO; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."EQUIPO" (
    id_equipo integer NOT NULL,
    nombre character varying,
    fecha_creacion date
);


ALTER TABLE public."EQUIPO" OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 40966)
-- Name: ESTADISTICA_id_estadistica_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."ESTADISTICA_id_estadistica_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."ESTADISTICA_id_estadistica_seq" OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16485)
-- Name: ESTADISTICA; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."ESTADISTICA" (
    id_estadistica integer DEFAULT nextval('public."ESTADISTICA_id_estadistica_seq"'::regclass) NOT NULL,
    id_partida integer,
    id_jugador integer,
    kos integer,
    restarts integer,
    assists integer
);


ALTER TABLE public."ESTADISTICA" OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16441)
-- Name: INSCRIPCION; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."INSCRIPCION" (
    id_inscripcion integer NOT NULL,
    id_equipo integer,
    id_torneo integer,
    fecha_inscripcion date
);


ALTER TABLE public."INSCRIPCION" OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16391)
-- Name: JUGADOR; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."JUGADOR" (
    id_jugador integer NOT NULL,
    gamertag character varying,
    nombre_real character varying,
    email character varying,
    fecha_nacimiento date,
    pais character varying,
    id_equipo integer
);


ALTER TABLE public."JUGADOR" OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 40964)
-- Name: PARTIDA_id_partida_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."PARTIDA_id_partida_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."PARTIDA_id_partida_seq" OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16462)
-- Name: PARTIDA; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."PARTIDA" (
    id_partida integer DEFAULT nextval('public."PARTIDA_id_partida_seq"'::regclass) NOT NULL,
    id_torneo integer,
    "id_equipo_A" integer,
    "id_equipo_B" integer,
    fecha_hora time with time zone,
    "puntaje_equipo_A" integer,
    puntaje_equipo_b integer,
    fase public.fase_torneo
);


ALTER TABLE public."PARTIDA" OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16501)
-- Name: PATROCINIO; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."PATROCINIO" (
    id_patrocinio integer NOT NULL,
    id_sponsor integer,
    id_torneo integer,
    monto_usd numeric
);


ALTER TABLE public."PATROCINIO" OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 16514)
-- Name: SPONSOR; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."SPONSOR" (
    id_sponsor integer NOT NULL,
    nombre character varying,
    industria character varying
);


ALTER TABLE public."SPONSOR" OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16421)
-- Name: TORNEO; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."TORNEO" (
    id_torneo integer NOT NULL,
    nombre character varying,
    videojuego character varying,
    fecha_inicio date,
    fecha_fin date,
    price_pool_usd numeric,
    max_equipos integer
);


ALTER TABLE public."TORNEO" OWNER TO postgres;

--
-- TOC entry 4915 (class 2606 OID 32775)
-- Name: Capitanes Capitanes_id_jugador_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Capitanes"
    ADD CONSTRAINT "Capitanes_id_jugador_key" UNIQUE (id_jugador);


--
-- TOC entry 4917 (class 2606 OID 32773)
-- Name: Capitanes Capitanes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Capitanes"
    ADD CONSTRAINT "Capitanes_pkey" PRIMARY KEY (id_equipo);


--
-- TOC entry 4899 (class 2606 OID 16420)
-- Name: EQUIPO EQUIPO_nombre_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."EQUIPO"
    ADD CONSTRAINT "EQUIPO_nombre_key" UNIQUE (nombre);


--
-- TOC entry 4901 (class 2606 OID 16406)
-- Name: EQUIPO EQUIPO_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."EQUIPO"
    ADD CONSTRAINT "EQUIPO_pkey" PRIMARY KEY (id_equipo);


--
-- TOC entry 4909 (class 2606 OID 16490)
-- Name: ESTADISTICA ESTADISTICA_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."ESTADISTICA"
    ADD CONSTRAINT "ESTADISTICA_pkey" PRIMARY KEY (id_estadistica);


--
-- TOC entry 4905 (class 2606 OID 16446)
-- Name: INSCRIPCION INSCRIPCION_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."INSCRIPCION"
    ADD CONSTRAINT "INSCRIPCION_pkey" PRIMARY KEY (id_inscripcion);


--
-- TOC entry 4895 (class 2606 OID 16418)
-- Name: JUGADOR JUGADOR_gamertag_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."JUGADOR"
    ADD CONSTRAINT "JUGADOR_gamertag_email_key" UNIQUE (gamertag, email);


--
-- TOC entry 4897 (class 2606 OID 16398)
-- Name: JUGADOR JUGADOR_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."JUGADOR"
    ADD CONSTRAINT "JUGADOR_pkey" PRIMARY KEY (id_jugador);


--
-- TOC entry 4907 (class 2606 OID 16469)
-- Name: PARTIDA PARTIDA_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PARTIDA"
    ADD CONSTRAINT "PARTIDA_pkey" PRIMARY KEY (id_partida);


--
-- TOC entry 4911 (class 2606 OID 16508)
-- Name: PATROCINIO PATROCINIO_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PATROCINIO"
    ADD CONSTRAINT "PATROCINIO_pkey" PRIMARY KEY (id_patrocinio);


--
-- TOC entry 4913 (class 2606 OID 16521)
-- Name: SPONSOR SPONSOR_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."SPONSOR"
    ADD CONSTRAINT "SPONSOR_pkey" PRIMARY KEY (id_sponsor);


--
-- TOC entry 4903 (class 2606 OID 16428)
-- Name: TORNEO TORNEO_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."TORNEO"
    ADD CONSTRAINT "TORNEO_pkey" PRIMARY KEY (id_torneo);


--
-- TOC entry 4928 (class 2606 OID 32776)
-- Name: Capitanes Capitanes_id_equipo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Capitanes"
    ADD CONSTRAINT "Capitanes_id_equipo_fkey" FOREIGN KEY (id_equipo) REFERENCES public."EQUIPO"(id_equipo);


--
-- TOC entry 4929 (class 2606 OID 32781)
-- Name: Capitanes Capitanes_id_jugador_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Capitanes"
    ADD CONSTRAINT "Capitanes_id_jugador_fkey" FOREIGN KEY (id_jugador) REFERENCES public."JUGADOR"(id_jugador) NOT VALID;


--
-- TOC entry 4924 (class 2606 OID 16496)
-- Name: ESTADISTICA ESTADISTICA_id_jugador_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."ESTADISTICA"
    ADD CONSTRAINT "ESTADISTICA_id_jugador_fkey" FOREIGN KEY (id_jugador) REFERENCES public."JUGADOR"(id_jugador) NOT VALID;


--
-- TOC entry 4925 (class 2606 OID 16491)
-- Name: ESTADISTICA ESTADISTICA_id_partida_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."ESTADISTICA"
    ADD CONSTRAINT "ESTADISTICA_id_partida_fkey" FOREIGN KEY (id_partida) REFERENCES public."PARTIDA"(id_partida) NOT VALID;


--
-- TOC entry 4919 (class 2606 OID 16457)
-- Name: INSCRIPCION INSCRIPCION_id_equipo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."INSCRIPCION"
    ADD CONSTRAINT "INSCRIPCION_id_equipo_fkey" FOREIGN KEY (id_equipo) REFERENCES public."EQUIPO"(id_equipo) NOT VALID;


--
-- TOC entry 4920 (class 2606 OID 16452)
-- Name: INSCRIPCION INSCRIPCION_id_torneo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."INSCRIPCION"
    ADD CONSTRAINT "INSCRIPCION_id_torneo_fkey" FOREIGN KEY (id_torneo) REFERENCES public."TORNEO"(id_torneo) NOT VALID;


--
-- TOC entry 4918 (class 2606 OID 16412)
-- Name: JUGADOR JUGADOR_id_equipo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."JUGADOR"
    ADD CONSTRAINT "JUGADOR_id_equipo_fkey" FOREIGN KEY (id_equipo) REFERENCES public."EQUIPO"(id_equipo) NOT VALID;


--
-- TOC entry 4921 (class 2606 OID 16475)
-- Name: PARTIDA PARTIDA_id_equipo_A_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PARTIDA"
    ADD CONSTRAINT "PARTIDA_id_equipo_A_fkey" FOREIGN KEY ("id_equipo_A") REFERENCES public."EQUIPO"(id_equipo) NOT VALID;


--
-- TOC entry 4922 (class 2606 OID 16480)
-- Name: PARTIDA PARTIDA_id_equipo_B_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PARTIDA"
    ADD CONSTRAINT "PARTIDA_id_equipo_B_fkey" FOREIGN KEY ("id_equipo_B") REFERENCES public."EQUIPO"(id_equipo) NOT VALID;


--
-- TOC entry 4923 (class 2606 OID 16470)
-- Name: PARTIDA PARTIDA_id_torneo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PARTIDA"
    ADD CONSTRAINT "PARTIDA_id_torneo_fkey" FOREIGN KEY (id_torneo) REFERENCES public."TORNEO"(id_torneo) NOT VALID;


--
-- TOC entry 4926 (class 2606 OID 16522)
-- Name: PATROCINIO PATROCINIO_id_sponsor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PATROCINIO"
    ADD CONSTRAINT "PATROCINIO_id_sponsor_fkey" FOREIGN KEY (id_sponsor) REFERENCES public."SPONSOR"(id_sponsor) NOT VALID;


--
-- TOC entry 4927 (class 2606 OID 16509)
-- Name: PATROCINIO PATROCINIO_id_torneo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PATROCINIO"
    ADD CONSTRAINT "PATROCINIO_id_torneo_fkey" FOREIGN KEY (id_torneo) REFERENCES public."TORNEO"(id_torneo) NOT VALID;


-- Completed on 2026-04-12 23:19:26

--
-- PostgreSQL database dump complete
--

