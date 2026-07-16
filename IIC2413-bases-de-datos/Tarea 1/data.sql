--
-- PostgreSQL database dump
--


-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

-- Started on 2026-04-12 23:16:48

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
-- TOC entry 5076 (class 0 OID 16399)
-- Dependencies: 220
-- Data for Name: EQUIPO; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."EQUIPO" VALUES (10, 'Puente Alto', '2026-04-05');
INSERT INTO public."EQUIPO" VALUES (9, 'Argentina', '2026-04-05');
INSERT INTO public."EQUIPO" VALUES (8, 'Chile', '2026-04-05');
INSERT INTO public."EQUIPO" VALUES (7, 'Perú', '2026-04-05');
INSERT INTO public."EQUIPO" VALUES (6, 'Union Española', '2026-04-05');
INSERT INTO public."EQUIPO" VALUES (5, 'Deportes Iquique', '2026-04-05');
INSERT INTO public."EQUIPO" VALUES (4, 'Santiago Wanders', '2026-04-05');
INSERT INTO public."EQUIPO" VALUES (3, 'Cobreloa', '2026-04-05');
INSERT INTO public."EQUIPO" VALUES (2, 'Colo Colo', '2026-04-05');
INSERT INTO public."EQUIPO" VALUES (1, 'U de Chile', '2026-04-05');


--
-- TOC entry 5075 (class 0 OID 16391)
-- Dependencies: 219
-- Data for Name: JUGADOR; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."JUGADOR" VALUES (5, 'alexdestroyer', 'alex', 'alex@email.com', '2026-04-05', 'chile', 1);
INSERT INTO public."JUGADOR" VALUES (4, 'angelesdestroyer', 'angeles', 'angeles@email.com', '2026-04-05', 'bolivia', 1);
INSERT INTO public."JUGADOR" VALUES (3, 'andredestroyer', 'andre', 'andre@email.com', '2026-04-05', 'alemania', 1);
INSERT INTO public."JUGADOR" VALUES (2, 'catadestroyer', 'cata', 'cata@email.com', '2026-04-05', 'peru', 1);
INSERT INTO public."JUGADOR" VALUES (1, 'fernandadestroyer', 'fernanda', 'fernanda@email.com', '2026-04-05', 'Peru', 1);
INSERT INTO public."JUGADOR" VALUES (6, 'andresitokawai1', 'alex', 'alex1@email.com', '2026-04-05', 'chile', 2);
INSERT INTO public."JUGADOR" VALUES (7, 'andresitokawai2', 'alex', 'alex2@email.com', '2026-04-05', 'chile', 2);
INSERT INTO public."JUGADOR" VALUES (8, 'andresitokawai3', 'alex', 'alex3@email.com', '2026-04-05', 'chile', 2);
INSERT INTO public."JUGADOR" VALUES (9, 'andresitokawai4', 'alex', 'alex4@email.com', '2026-04-05', 'chile', 2);
INSERT INTO public."JUGADOR" VALUES (10, 'andresitokawai5', 'alex', 'ale5x@email.com', '2026-04-05', 'chile', 2);
INSERT INTO public."JUGADOR" VALUES (11, 'andresitokawai6', 'alex', 'ale32x@email.com', '2026-04-05', 'chile', 3);
INSERT INTO public."JUGADOR" VALUES (12, 'andresitokawai7', 'alex', 'ale3233x@email.com', '2026-04-05', 'chile', 3);
INSERT INTO public."JUGADOR" VALUES (13, 'andresitokawai8', 'alex', 'ale313131x@email.com', '2026-04-05', 'chile', 3);
INSERT INTO public."JUGADOR" VALUES (14, 'andresitokawai9', 'alex', 'al313131ex@email.com', '2026-04-05', 'chile', 3);
INSERT INTO public."JUGADOR" VALUES (15, 'andresitokawai10', 'alex', 'alex321313@email.com', '2026-04-05', 'chile', 3);
INSERT INTO public."JUGADOR" VALUES (16, 'andresitokawai11', 'alex', 'a31313lex@email.com', '2026-04-05', 'chile', 4);
INSERT INTO public."JUGADOR" VALUES (17, 'andresitokawai12', 'alex', 'ale3131x@email.com', '2026-04-05', 'chile', 4);
INSERT INTO public."JUGADOR" VALUES (18, 'andresitokawai13', 'alex', 'alex3131@email.com', '2026-04-05', 'chile', 4);
INSERT INTO public."JUGADOR" VALUES (19, 'andresitokawai14', 'alex', 'ale313131313131x@email.com', '2026-04-05', 'chile', 4);
INSERT INTO public."JUGADOR" VALUES (20, 'andresitokawai15', 'alex', 'a442424lex@email.com', '2026-04-05', 'chile', 4);
INSERT INTO public."JUGADOR" VALUES (21, 'andresitokawai16', 'alex', 'alex323555@email.com', '2026-04-05', 'chile', 5);
INSERT INTO public."JUGADOR" VALUES (22, 'andresitokawai17', 'alex', 'ale313j1x@email.com', '2026-04-05', 'chile', 5);
INSERT INTO public."JUGADOR" VALUES (23, 'andresitokawai18', 'alex', 'alexdadad@email.com', '2026-04-05', 'chile', 5);
INSERT INTO public."JUGADOR" VALUES (24, 'andresitokawai19', 'alex', 'aledadadx@email.com', '2026-04-05', 'chile', 5);
INSERT INTO public."JUGADOR" VALUES (25, 'andresitokawai20', 'alex', 'aledadaddddddxdadada@email.com', '2026-04-05', 'chile', 5);
INSERT INTO public."JUGADOR" VALUES (26, 'andresitokawai21', 'alex', 'aledadadax@email.com', '2026-04-05', 'chile', 6);
INSERT INTO public."JUGADOR" VALUES (27, 'andresitokawai22', 'alex', 'fffffadadx@email.com', '2026-04-05', 'chile', 6);
INSERT INTO public."JUGADOR" VALUES (28, 'andresitokawai23', 'alex', 'aleadadax@email.com', '2026-04-05', 'chile', 6);
INSERT INTO public."JUGADOR" VALUES (29, 'andresitokawai24', 'alex', 'aledad313131adax@email.com', '2026-04-05', 'chile', 6);
INSERT INTO public."JUGADOR" VALUES (30, 'andresitokawai25', 'alex', 'alexdadadad@email.com', '2026-04-05', 'chile', 6);
INSERT INTO public."JUGADOR" VALUES (31, 'andresitokawai26', 'alex', 'aledadaddadadaax@email.com', '2026-04-05', 'chile', 7);
INSERT INTO public."JUGADOR" VALUES (32, 'andresitokawai27', 'alex', 'aledadaffsffdax@email.com', '2026-04-05', 'chile', 7);
INSERT INTO public."JUGADOR" VALUES (33, 'andresitokawai28', 'alex', 'aledadr3r32radax@email.com', '2026-04-05', 'chile', 7);
INSERT INTO public."JUGADOR" VALUES (34, 'andresitokawai29', 'alex', 'aledadadax@email.com', '2026-04-05', 'chile', 7);
INSERT INTO public."JUGADOR" VALUES (35, 'andresitokawai30', 'alex', 'alexdadada@email.com', '2026-04-05', 'chile', 7);
INSERT INTO public."JUGADOR" VALUES (36, 'andresitokawai31', 'alex', 'alexdadada@email.com', '2026-04-05', 'chile', 8);
INSERT INTO public."JUGADOR" VALUES (37, 'andresitokawai32', 'alex', 'alexdadadddda@email.com', '2026-04-05', 'chile', 8);
INSERT INTO public."JUGADOR" VALUES (38, 'nosoyalex', 'alex', 'alexd1d1d1@email.com', '2026-04-05', 'chile', 8);
INSERT INTO public."JUGADOR" VALUES (39, 'andresitokawai33', 'alex', 'alexxxxxxx@email.com', '2026-04-05', 'chile', 8);
INSERT INTO public."JUGADOR" VALUES (40, 'alexdestroye34', 'alex', 'alexxxx@email.com', '2026-04-05', 'chile', 8);
INSERT INTO public."JUGADOR" VALUES (41, 'andresitokawai35', 'alex', '13131@gmail.com', '2026-04-05', 'chile', 9);
INSERT INTO public."JUGADOR" VALUES (42, 'andresitokawai36', 'alex', 'aledddddddddx@email.com', '2026-04-05', 'chile', 9);
INSERT INTO public."JUGADOR" VALUES (43, 'andresitokawai37', 'alex', 'aleeeeee@email.com', '2026-04-05', 'chile', 9);
INSERT INTO public."JUGADOR" VALUES (44, 'andresitokawai38', 'alex', 'ax@email.com', '2026-04-05', 'chile', 9);
INSERT INTO public."JUGADOR" VALUES (45, 'andresitokawai39', 'alex', 'alexxxxxxxxxxxxxxx@email.com', '2026-04-05', 'chile', 9);
INSERT INTO public."JUGADOR" VALUES (46, 'andresitokawai40', 'alex', 'alelllx@email.com', '2026-04-05', 'chile', 10);
INSERT INTO public."JUGADOR" VALUES (47, 'andresitokawai41', 'alex', 'alexxxxxx@email.com', '2026-04-05', 'chile', 10);
INSERT INTO public."JUGADOR" VALUES (48, 'andresitokawai42', 'alex', 'alexxxxxxxadada@email.com', '2026-04-05', 'chile', 10);
INSERT INTO public."JUGADOR" VALUES (49, 'xdlol', 'alex', 'alexddadd@email.com', '2026-04-05', 'chile', 10);
INSERT INTO public."JUGADOR" VALUES (50, 'holasoygerman', 'alex', 'alexxxxxaxdadadada@email.com', '2026-04-05', 'chile', 10);


--
-- TOC entry 5083 (class 0 OID 32768)
-- Dependencies: 227
-- Data for Name: Capitanes; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Capitanes" VALUES (26, 6);
INSERT INTO public."Capitanes" VALUES (24, 5);
INSERT INTO public."Capitanes" VALUES (16, 4);
INSERT INTO public."Capitanes" VALUES (15, 3);
INSERT INTO public."Capitanes" VALUES (1, 1);
INSERT INTO public."Capitanes" VALUES (42, 9);
INSERT INTO public."Capitanes" VALUES (37, 8);
INSERT INTO public."Capitanes" VALUES (33, 7);
INSERT INTO public."Capitanes" VALUES (48, 10);


--
-- TOC entry 5077 (class 0 OID 16421)
-- Dependencies: 221
-- Data for Name: TORNEO; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."TORNEO" VALUES (1, 'fernandagamerlol123', 'League of Leagends', '2026-04-05', '2026-04-06', 500, 8);
INSERT INTO public."TORNEO" VALUES (2, 'cata the game: bebe 8 cervezas al hilo', 'Drink the game', '2026-04-05', '2026-04-06', 10000000, 3);
INSERT INTO public."TORNEO" VALUES (3, 'andré escape from tarkov', 'Call of duty: ', '2026-04-05', '2026-04-06', 10, 10);


--
-- TOC entry 5079 (class 0 OID 16462)
-- Dependencies: 223
-- Data for Name: PARTIDA; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."PARTIDA" VALUES (29, 1, 1, 4, '15:00:00-04', 1, 0, 'semifinal');
INSERT INTO public."PARTIDA" VALUES (30, 1, 2, 3, '15:00:00-04', 0, 1, 'semifinal');
INSERT INTO public."PARTIDA" VALUES (31, 1, 1, 3, '15:00:00-04', 1, 0, 'final');
INSERT INTO public."PARTIDA" VALUES (1, 1, 7, 8, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (2, 1, 6, 8, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (3, 1, 6, 7, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (4, 1, 5, 8, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (5, 1, 5, 7, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (6, 1, 5, 6, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (7, 1, 4, 8, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (8, 1, 4, 7, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (9, 1, 4, 6, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (10, 1, 4, 5, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (11, 1, 3, 8, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (12, 1, 3, 7, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (13, 1, 3, 6, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (14, 1, 3, 5, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (15, 1, 3, 4, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (16, 1, 2, 8, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (17, 1, 2, 7, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (18, 1, 2, 6, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (19, 1, 2, 5, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (20, 1, 2, 4, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (21, 1, 2, 3, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (22, 1, 1, 8, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (23, 1, 1, 7, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (24, 1, 1, 6, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (25, 1, 1, 5, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (26, 1, 1, 4, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (27, 1, 1, 3, '15:00:00-04', 1, 0, 'fase de grupos');
INSERT INTO public."PARTIDA" VALUES (28, 1, 1, 2, '15:00:00-04', 1, 0, 'fase de grupos');


--
-- TOC entry 5080 (class 0 OID 16485)
-- Dependencies: 224
-- Data for Name: ESTADISTICA; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."ESTADISTICA" VALUES (1, 29, 5, 14, 0, 5);
INSERT INTO public."ESTADISTICA" VALUES (2, 31, 5, 14, 7, 8);
INSERT INTO public."ESTADISTICA" VALUES (3, 22, 5, 18, 7, 0);
INSERT INTO public."ESTADISTICA" VALUES (4, 23, 5, 7, 4, 7);
INSERT INTO public."ESTADISTICA" VALUES (5, 24, 5, 13, 3, 11);
INSERT INTO public."ESTADISTICA" VALUES (6, 25, 5, 4, 2, 8);
INSERT INTO public."ESTADISTICA" VALUES (7, 26, 5, 4, 6, 2);
INSERT INTO public."ESTADISTICA" VALUES (8, 27, 5, 6, 0, 4);
INSERT INTO public."ESTADISTICA" VALUES (9, 28, 5, 15, 5, 0);
INSERT INTO public."ESTADISTICA" VALUES (10, 29, 4, 4, 3, 11);
INSERT INTO public."ESTADISTICA" VALUES (11, 31, 4, 9, 0, 1);
INSERT INTO public."ESTADISTICA" VALUES (12, 22, 4, 5, 9, 5);
INSERT INTO public."ESTADISTICA" VALUES (13, 23, 4, 14, 9, 13);
INSERT INTO public."ESTADISTICA" VALUES (14, 24, 4, 1, 7, 0);
INSERT INTO public."ESTADISTICA" VALUES (15, 25, 4, 14, 3, 14);
INSERT INTO public."ESTADISTICA" VALUES (16, 26, 4, 15, 0, 13);
INSERT INTO public."ESTADISTICA" VALUES (17, 27, 4, 5, 0, 10);
INSERT INTO public."ESTADISTICA" VALUES (18, 28, 4, 18, 7, 5);
INSERT INTO public."ESTADISTICA" VALUES (19, 29, 3, 8, 4, 1);
INSERT INTO public."ESTADISTICA" VALUES (20, 31, 3, 19, 3, 4);
INSERT INTO public."ESTADISTICA" VALUES (21, 22, 3, 12, 1, 13);
INSERT INTO public."ESTADISTICA" VALUES (22, 23, 3, 7, 8, 6);
INSERT INTO public."ESTADISTICA" VALUES (23, 24, 3, 6, 5, 5);
INSERT INTO public."ESTADISTICA" VALUES (24, 25, 3, 6, 1, 9);
INSERT INTO public."ESTADISTICA" VALUES (25, 26, 3, 8, 5, 10);
INSERT INTO public."ESTADISTICA" VALUES (26, 27, 3, 17, 7, 11);
INSERT INTO public."ESTADISTICA" VALUES (27, 28, 3, 18, 1, 1);
INSERT INTO public."ESTADISTICA" VALUES (28, 29, 2, 6, 0, 3);
INSERT INTO public."ESTADISTICA" VALUES (29, 31, 2, 1, 5, 6);
INSERT INTO public."ESTADISTICA" VALUES (30, 22, 2, 14, 3, 7);
INSERT INTO public."ESTADISTICA" VALUES (31, 23, 2, 14, 7, 3);
INSERT INTO public."ESTADISTICA" VALUES (32, 24, 2, 7, 2, 5);
INSERT INTO public."ESTADISTICA" VALUES (33, 25, 2, 3, 1, 4);
INSERT INTO public."ESTADISTICA" VALUES (34, 26, 2, 14, 4, 3);
INSERT INTO public."ESTADISTICA" VALUES (35, 27, 2, 19, 3, 12);
INSERT INTO public."ESTADISTICA" VALUES (36, 28, 2, 18, 3, 4);
INSERT INTO public."ESTADISTICA" VALUES (37, 29, 1, 2, 4, 12);
INSERT INTO public."ESTADISTICA" VALUES (38, 31, 1, 19, 2, 0);
INSERT INTO public."ESTADISTICA" VALUES (39, 22, 1, 15, 5, 14);
INSERT INTO public."ESTADISTICA" VALUES (40, 23, 1, 15, 6, 5);
INSERT INTO public."ESTADISTICA" VALUES (41, 24, 1, 1, 7, 2);
INSERT INTO public."ESTADISTICA" VALUES (42, 25, 1, 12, 4, 7);
INSERT INTO public."ESTADISTICA" VALUES (43, 26, 1, 13, 4, 13);
INSERT INTO public."ESTADISTICA" VALUES (44, 27, 1, 14, 5, 13);
INSERT INTO public."ESTADISTICA" VALUES (45, 28, 1, 18, 7, 14);
INSERT INTO public."ESTADISTICA" VALUES (46, 30, 6, 7, 9, 9);
INSERT INTO public."ESTADISTICA" VALUES (47, 16, 6, 13, 8, 6);
INSERT INTO public."ESTADISTICA" VALUES (48, 17, 6, 16, 3, 8);
INSERT INTO public."ESTADISTICA" VALUES (49, 18, 6, 4, 4, 2);
INSERT INTO public."ESTADISTICA" VALUES (50, 19, 6, 7, 0, 12);
INSERT INTO public."ESTADISTICA" VALUES (51, 20, 6, 2, 5, 7);
INSERT INTO public."ESTADISTICA" VALUES (52, 21, 6, 14, 1, 4);
INSERT INTO public."ESTADISTICA" VALUES (53, 28, 6, 18, 7, 8);
INSERT INTO public."ESTADISTICA" VALUES (54, 30, 7, 16, 9, 13);
INSERT INTO public."ESTADISTICA" VALUES (55, 16, 7, 0, 5, 6);
INSERT INTO public."ESTADISTICA" VALUES (56, 17, 7, 7, 8, 11);
INSERT INTO public."ESTADISTICA" VALUES (57, 18, 7, 16, 8, 10);
INSERT INTO public."ESTADISTICA" VALUES (58, 19, 7, 2, 6, 14);
INSERT INTO public."ESTADISTICA" VALUES (59, 20, 7, 6, 5, 3);
INSERT INTO public."ESTADISTICA" VALUES (60, 21, 7, 18, 4, 8);
INSERT INTO public."ESTADISTICA" VALUES (61, 28, 7, 0, 2, 12);
INSERT INTO public."ESTADISTICA" VALUES (62, 30, 8, 11, 1, 10);
INSERT INTO public."ESTADISTICA" VALUES (63, 16, 8, 8, 2, 4);
INSERT INTO public."ESTADISTICA" VALUES (64, 17, 8, 9, 0, 4);
INSERT INTO public."ESTADISTICA" VALUES (65, 18, 8, 11, 5, 9);
INSERT INTO public."ESTADISTICA" VALUES (66, 19, 8, 6, 6, 5);
INSERT INTO public."ESTADISTICA" VALUES (67, 20, 8, 11, 1, 0);
INSERT INTO public."ESTADISTICA" VALUES (68, 21, 8, 5, 8, 9);
INSERT INTO public."ESTADISTICA" VALUES (69, 28, 8, 8, 3, 6);
INSERT INTO public."ESTADISTICA" VALUES (70, 30, 9, 1, 4, 4);
INSERT INTO public."ESTADISTICA" VALUES (71, 16, 9, 0, 6, 10);
INSERT INTO public."ESTADISTICA" VALUES (72, 17, 9, 11, 3, 0);
INSERT INTO public."ESTADISTICA" VALUES (73, 18, 9, 16, 0, 7);
INSERT INTO public."ESTADISTICA" VALUES (74, 19, 9, 6, 3, 10);
INSERT INTO public."ESTADISTICA" VALUES (75, 20, 9, 15, 6, 7);
INSERT INTO public."ESTADISTICA" VALUES (76, 21, 9, 10, 1, 12);
INSERT INTO public."ESTADISTICA" VALUES (77, 28, 9, 3, 3, 12);
INSERT INTO public."ESTADISTICA" VALUES (78, 30, 10, 2, 7, 1);
INSERT INTO public."ESTADISTICA" VALUES (79, 16, 10, 8, 5, 5);
INSERT INTO public."ESTADISTICA" VALUES (80, 17, 10, 3, 7, 13);
INSERT INTO public."ESTADISTICA" VALUES (81, 18, 10, 5, 6, 12);
INSERT INTO public."ESTADISTICA" VALUES (82, 19, 10, 13, 4, 7);
INSERT INTO public."ESTADISTICA" VALUES (83, 20, 10, 3, 4, 7);
INSERT INTO public."ESTADISTICA" VALUES (84, 21, 10, 5, 5, 2);
INSERT INTO public."ESTADISTICA" VALUES (85, 28, 10, 7, 3, 6);
INSERT INTO public."ESTADISTICA" VALUES (86, 30, 11, 1, 6, 1);
INSERT INTO public."ESTADISTICA" VALUES (87, 31, 11, 16, 6, 5);
INSERT INTO public."ESTADISTICA" VALUES (88, 11, 11, 16, 9, 10);
INSERT INTO public."ESTADISTICA" VALUES (89, 12, 11, 17, 3, 6);
INSERT INTO public."ESTADISTICA" VALUES (90, 13, 11, 5, 7, 11);
INSERT INTO public."ESTADISTICA" VALUES (91, 14, 11, 7, 2, 0);
INSERT INTO public."ESTADISTICA" VALUES (92, 15, 11, 18, 9, 14);
INSERT INTO public."ESTADISTICA" VALUES (93, 21, 11, 17, 9, 11);
INSERT INTO public."ESTADISTICA" VALUES (94, 27, 11, 2, 8, 12);
INSERT INTO public."ESTADISTICA" VALUES (95, 30, 12, 6, 1, 11);
INSERT INTO public."ESTADISTICA" VALUES (96, 31, 12, 6, 3, 11);
INSERT INTO public."ESTADISTICA" VALUES (97, 11, 12, 13, 3, 7);
INSERT INTO public."ESTADISTICA" VALUES (98, 12, 12, 15, 6, 8);
INSERT INTO public."ESTADISTICA" VALUES (99, 13, 12, 1, 1, 12);
INSERT INTO public."ESTADISTICA" VALUES (100, 14, 12, 19, 8, 11);
INSERT INTO public."ESTADISTICA" VALUES (101, 15, 12, 5, 3, 6);
INSERT INTO public."ESTADISTICA" VALUES (102, 21, 12, 11, 8, 4);
INSERT INTO public."ESTADISTICA" VALUES (103, 27, 12, 7, 5, 10);
INSERT INTO public."ESTADISTICA" VALUES (104, 30, 13, 16, 9, 12);
INSERT INTO public."ESTADISTICA" VALUES (105, 31, 13, 6, 8, 10);
INSERT INTO public."ESTADISTICA" VALUES (106, 11, 13, 3, 6, 0);
INSERT INTO public."ESTADISTICA" VALUES (107, 12, 13, 1, 5, 13);
INSERT INTO public."ESTADISTICA" VALUES (108, 13, 13, 19, 4, 7);
INSERT INTO public."ESTADISTICA" VALUES (109, 14, 13, 12, 6, 7);
INSERT INTO public."ESTADISTICA" VALUES (110, 15, 13, 8, 4, 11);
INSERT INTO public."ESTADISTICA" VALUES (111, 21, 13, 11, 6, 8);
INSERT INTO public."ESTADISTICA" VALUES (112, 27, 13, 9, 0, 9);
INSERT INTO public."ESTADISTICA" VALUES (113, 30, 14, 11, 7, 12);
INSERT INTO public."ESTADISTICA" VALUES (114, 31, 14, 12, 8, 0);
INSERT INTO public."ESTADISTICA" VALUES (115, 11, 14, 16, 0, 13);
INSERT INTO public."ESTADISTICA" VALUES (116, 12, 14, 7, 7, 0);
INSERT INTO public."ESTADISTICA" VALUES (117, 13, 14, 8, 6, 1);
INSERT INTO public."ESTADISTICA" VALUES (118, 14, 14, 0, 8, 0);
INSERT INTO public."ESTADISTICA" VALUES (119, 15, 14, 6, 1, 3);
INSERT INTO public."ESTADISTICA" VALUES (120, 21, 14, 12, 4, 12);
INSERT INTO public."ESTADISTICA" VALUES (121, 27, 14, 6, 7, 7);
INSERT INTO public."ESTADISTICA" VALUES (122, 30, 15, 18, 7, 13);
INSERT INTO public."ESTADISTICA" VALUES (123, 31, 15, 11, 6, 4);
INSERT INTO public."ESTADISTICA" VALUES (124, 11, 15, 19, 1, 11);
INSERT INTO public."ESTADISTICA" VALUES (125, 12, 15, 3, 8, 12);
INSERT INTO public."ESTADISTICA" VALUES (126, 13, 15, 12, 9, 2);
INSERT INTO public."ESTADISTICA" VALUES (127, 14, 15, 18, 4, 4);
INSERT INTO public."ESTADISTICA" VALUES (128, 15, 15, 13, 1, 14);
INSERT INTO public."ESTADISTICA" VALUES (129, 21, 15, 2, 7, 10);
INSERT INTO public."ESTADISTICA" VALUES (130, 27, 15, 17, 9, 7);
INSERT INTO public."ESTADISTICA" VALUES (131, 29, 16, 18, 8, 3);
INSERT INTO public."ESTADISTICA" VALUES (132, 7, 16, 0, 7, 7);
INSERT INTO public."ESTADISTICA" VALUES (133, 8, 16, 2, 5, 6);
INSERT INTO public."ESTADISTICA" VALUES (134, 9, 16, 3, 2, 11);
INSERT INTO public."ESTADISTICA" VALUES (135, 10, 16, 8, 6, 13);
INSERT INTO public."ESTADISTICA" VALUES (136, 15, 16, 18, 6, 8);
INSERT INTO public."ESTADISTICA" VALUES (137, 20, 16, 7, 1, 9);
INSERT INTO public."ESTADISTICA" VALUES (138, 26, 16, 14, 0, 9);
INSERT INTO public."ESTADISTICA" VALUES (139, 29, 17, 10, 3, 12);
INSERT INTO public."ESTADISTICA" VALUES (140, 7, 17, 11, 8, 9);
INSERT INTO public."ESTADISTICA" VALUES (141, 8, 17, 19, 1, 6);
INSERT INTO public."ESTADISTICA" VALUES (142, 9, 17, 19, 6, 6);
INSERT INTO public."ESTADISTICA" VALUES (143, 10, 17, 8, 8, 6);
INSERT INTO public."ESTADISTICA" VALUES (144, 15, 17, 5, 7, 10);
INSERT INTO public."ESTADISTICA" VALUES (145, 20, 17, 8, 1, 2);
INSERT INTO public."ESTADISTICA" VALUES (146, 26, 17, 1, 1, 9);
INSERT INTO public."ESTADISTICA" VALUES (147, 29, 18, 18, 4, 14);
INSERT INTO public."ESTADISTICA" VALUES (148, 7, 18, 4, 8, 11);
INSERT INTO public."ESTADISTICA" VALUES (149, 8, 18, 5, 9, 5);
INSERT INTO public."ESTADISTICA" VALUES (150, 9, 18, 10, 9, 14);
INSERT INTO public."ESTADISTICA" VALUES (151, 10, 18, 11, 9, 14);
INSERT INTO public."ESTADISTICA" VALUES (152, 15, 18, 1, 7, 11);
INSERT INTO public."ESTADISTICA" VALUES (153, 20, 18, 0, 6, 12);
INSERT INTO public."ESTADISTICA" VALUES (154, 26, 18, 7, 2, 9);
INSERT INTO public."ESTADISTICA" VALUES (155, 29, 19, 6, 1, 7);
INSERT INTO public."ESTADISTICA" VALUES (156, 7, 19, 7, 4, 7);
INSERT INTO public."ESTADISTICA" VALUES (157, 8, 19, 4, 1, 8);
INSERT INTO public."ESTADISTICA" VALUES (158, 9, 19, 18, 5, 13);
INSERT INTO public."ESTADISTICA" VALUES (159, 10, 19, 9, 4, 9);
INSERT INTO public."ESTADISTICA" VALUES (160, 15, 19, 15, 1, 2);
INSERT INTO public."ESTADISTICA" VALUES (161, 20, 19, 13, 9, 8);
INSERT INTO public."ESTADISTICA" VALUES (162, 26, 19, 9, 9, 11);
INSERT INTO public."ESTADISTICA" VALUES (163, 29, 20, 6, 8, 9);
INSERT INTO public."ESTADISTICA" VALUES (164, 7, 20, 13, 1, 6);
INSERT INTO public."ESTADISTICA" VALUES (165, 8, 20, 17, 3, 4);
INSERT INTO public."ESTADISTICA" VALUES (166, 9, 20, 12, 5, 13);
INSERT INTO public."ESTADISTICA" VALUES (167, 10, 20, 7, 1, 4);
INSERT INTO public."ESTADISTICA" VALUES (168, 15, 20, 19, 1, 4);
INSERT INTO public."ESTADISTICA" VALUES (169, 20, 20, 15, 2, 14);
INSERT INTO public."ESTADISTICA" VALUES (170, 26, 20, 17, 0, 6);
INSERT INTO public."ESTADISTICA" VALUES (171, 4, 21, 15, 4, 2);
INSERT INTO public."ESTADISTICA" VALUES (172, 5, 21, 10, 3, 9);
INSERT INTO public."ESTADISTICA" VALUES (173, 6, 21, 19, 9, 11);
INSERT INTO public."ESTADISTICA" VALUES (174, 10, 21, 4, 6, 0);
INSERT INTO public."ESTADISTICA" VALUES (175, 14, 21, 2, 0, 12);
INSERT INTO public."ESTADISTICA" VALUES (176, 19, 21, 3, 7, 14);
INSERT INTO public."ESTADISTICA" VALUES (177, 25, 21, 10, 7, 7);
INSERT INTO public."ESTADISTICA" VALUES (178, 4, 22, 8, 7, 8);
INSERT INTO public."ESTADISTICA" VALUES (179, 5, 22, 2, 0, 4);
INSERT INTO public."ESTADISTICA" VALUES (180, 6, 22, 0, 1, 13);
INSERT INTO public."ESTADISTICA" VALUES (181, 10, 22, 3, 9, 3);
INSERT INTO public."ESTADISTICA" VALUES (182, 14, 22, 13, 5, 11);
INSERT INTO public."ESTADISTICA" VALUES (183, 19, 22, 2, 3, 0);
INSERT INTO public."ESTADISTICA" VALUES (184, 25, 22, 8, 5, 11);
INSERT INTO public."ESTADISTICA" VALUES (185, 4, 23, 13, 9, 13);
INSERT INTO public."ESTADISTICA" VALUES (186, 5, 23, 14, 7, 1);
INSERT INTO public."ESTADISTICA" VALUES (187, 6, 23, 9, 0, 12);
INSERT INTO public."ESTADISTICA" VALUES (188, 10, 23, 4, 9, 8);
INSERT INTO public."ESTADISTICA" VALUES (189, 14, 23, 16, 5, 3);
INSERT INTO public."ESTADISTICA" VALUES (190, 19, 23, 1, 8, 2);
INSERT INTO public."ESTADISTICA" VALUES (191, 25, 23, 5, 2, 2);
INSERT INTO public."ESTADISTICA" VALUES (192, 4, 24, 13, 3, 14);
INSERT INTO public."ESTADISTICA" VALUES (193, 5, 24, 7, 9, 1);
INSERT INTO public."ESTADISTICA" VALUES (194, 6, 24, 8, 8, 10);
INSERT INTO public."ESTADISTICA" VALUES (195, 10, 24, 15, 9, 12);
INSERT INTO public."ESTADISTICA" VALUES (196, 14, 24, 2, 8, 2);
INSERT INTO public."ESTADISTICA" VALUES (197, 19, 24, 17, 9, 12);
INSERT INTO public."ESTADISTICA" VALUES (198, 25, 24, 8, 3, 12);
INSERT INTO public."ESTADISTICA" VALUES (199, 4, 25, 5, 1, 3);
INSERT INTO public."ESTADISTICA" VALUES (200, 5, 25, 10, 7, 0);
INSERT INTO public."ESTADISTICA" VALUES (201, 6, 25, 3, 7, 6);
INSERT INTO public."ESTADISTICA" VALUES (202, 10, 25, 2, 5, 11);
INSERT INTO public."ESTADISTICA" VALUES (203, 14, 25, 2, 4, 0);
INSERT INTO public."ESTADISTICA" VALUES (204, 19, 25, 10, 7, 10);
INSERT INTO public."ESTADISTICA" VALUES (205, 25, 25, 15, 3, 2);
INSERT INTO public."ESTADISTICA" VALUES (206, 2, 26, 16, 6, 2);
INSERT INTO public."ESTADISTICA" VALUES (207, 3, 26, 15, 8, 13);
INSERT INTO public."ESTADISTICA" VALUES (208, 6, 26, 13, 0, 14);
INSERT INTO public."ESTADISTICA" VALUES (209, 9, 26, 10, 1, 5);
INSERT INTO public."ESTADISTICA" VALUES (210, 13, 26, 11, 0, 2);
INSERT INTO public."ESTADISTICA" VALUES (211, 18, 26, 7, 8, 13);
INSERT INTO public."ESTADISTICA" VALUES (212, 24, 26, 3, 4, 14);
INSERT INTO public."ESTADISTICA" VALUES (213, 2, 27, 0, 6, 13);
INSERT INTO public."ESTADISTICA" VALUES (214, 3, 27, 9, 9, 1);
INSERT INTO public."ESTADISTICA" VALUES (215, 6, 27, 17, 8, 7);
INSERT INTO public."ESTADISTICA" VALUES (216, 9, 27, 15, 2, 10);
INSERT INTO public."ESTADISTICA" VALUES (217, 13, 27, 10, 6, 0);
INSERT INTO public."ESTADISTICA" VALUES (218, 18, 27, 8, 9, 13);
INSERT INTO public."ESTADISTICA" VALUES (219, 24, 27, 18, 9, 2);
INSERT INTO public."ESTADISTICA" VALUES (220, 2, 28, 6, 3, 7);
INSERT INTO public."ESTADISTICA" VALUES (221, 3, 28, 5, 0, 7);
INSERT INTO public."ESTADISTICA" VALUES (222, 6, 28, 15, 5, 5);
INSERT INTO public."ESTADISTICA" VALUES (223, 9, 28, 4, 7, 7);
INSERT INTO public."ESTADISTICA" VALUES (224, 13, 28, 9, 6, 4);
INSERT INTO public."ESTADISTICA" VALUES (225, 18, 28, 16, 3, 5);
INSERT INTO public."ESTADISTICA" VALUES (226, 24, 28, 1, 5, 5);
INSERT INTO public."ESTADISTICA" VALUES (227, 2, 29, 8, 8, 14);
INSERT INTO public."ESTADISTICA" VALUES (228, 3, 29, 11, 0, 12);
INSERT INTO public."ESTADISTICA" VALUES (229, 6, 29, 13, 8, 0);
INSERT INTO public."ESTADISTICA" VALUES (230, 9, 29, 16, 6, 6);
INSERT INTO public."ESTADISTICA" VALUES (231, 13, 29, 5, 0, 12);
INSERT INTO public."ESTADISTICA" VALUES (232, 18, 29, 3, 7, 4);
INSERT INTO public."ESTADISTICA" VALUES (233, 24, 29, 17, 7, 1);
INSERT INTO public."ESTADISTICA" VALUES (234, 2, 30, 9, 2, 12);
INSERT INTO public."ESTADISTICA" VALUES (235, 3, 30, 16, 6, 6);
INSERT INTO public."ESTADISTICA" VALUES (236, 6, 30, 8, 6, 6);
INSERT INTO public."ESTADISTICA" VALUES (237, 9, 30, 6, 6, 14);
INSERT INTO public."ESTADISTICA" VALUES (238, 13, 30, 5, 3, 10);
INSERT INTO public."ESTADISTICA" VALUES (239, 18, 30, 10, 7, 0);
INSERT INTO public."ESTADISTICA" VALUES (240, 24, 30, 15, 0, 13);
INSERT INTO public."ESTADISTICA" VALUES (241, 1, 31, 13, 2, 6);
INSERT INTO public."ESTADISTICA" VALUES (242, 3, 31, 6, 9, 9);
INSERT INTO public."ESTADISTICA" VALUES (243, 5, 31, 19, 2, 13);
INSERT INTO public."ESTADISTICA" VALUES (244, 8, 31, 7, 1, 13);
INSERT INTO public."ESTADISTICA" VALUES (245, 12, 31, 12, 3, 5);
INSERT INTO public."ESTADISTICA" VALUES (246, 17, 31, 9, 8, 12);
INSERT INTO public."ESTADISTICA" VALUES (247, 23, 31, 13, 4, 6);
INSERT INTO public."ESTADISTICA" VALUES (248, 1, 32, 0, 4, 6);
INSERT INTO public."ESTADISTICA" VALUES (249, 3, 32, 5, 5, 10);
INSERT INTO public."ESTADISTICA" VALUES (250, 5, 32, 7, 1, 6);
INSERT INTO public."ESTADISTICA" VALUES (251, 8, 32, 11, 7, 13);
INSERT INTO public."ESTADISTICA" VALUES (252, 12, 32, 4, 9, 3);
INSERT INTO public."ESTADISTICA" VALUES (253, 17, 32, 6, 3, 5);
INSERT INTO public."ESTADISTICA" VALUES (254, 23, 32, 0, 7, 11);
INSERT INTO public."ESTADISTICA" VALUES (255, 1, 33, 18, 2, 13);
INSERT INTO public."ESTADISTICA" VALUES (256, 3, 33, 15, 9, 3);
INSERT INTO public."ESTADISTICA" VALUES (257, 5, 33, 18, 3, 3);
INSERT INTO public."ESTADISTICA" VALUES (258, 8, 33, 3, 5, 10);
INSERT INTO public."ESTADISTICA" VALUES (259, 12, 33, 9, 3, 4);
INSERT INTO public."ESTADISTICA" VALUES (260, 17, 33, 15, 2, 12);
INSERT INTO public."ESTADISTICA" VALUES (261, 23, 33, 1, 1, 1);
INSERT INTO public."ESTADISTICA" VALUES (262, 1, 34, 7, 2, 3);
INSERT INTO public."ESTADISTICA" VALUES (263, 3, 34, 7, 0, 7);
INSERT INTO public."ESTADISTICA" VALUES (264, 5, 34, 4, 3, 2);
INSERT INTO public."ESTADISTICA" VALUES (265, 8, 34, 19, 6, 2);
INSERT INTO public."ESTADISTICA" VALUES (266, 12, 34, 7, 5, 9);
INSERT INTO public."ESTADISTICA" VALUES (267, 17, 34, 7, 2, 10);
INSERT INTO public."ESTADISTICA" VALUES (268, 23, 34, 3, 0, 0);
INSERT INTO public."ESTADISTICA" VALUES (269, 1, 35, 7, 2, 13);
INSERT INTO public."ESTADISTICA" VALUES (270, 3, 35, 1, 3, 7);
INSERT INTO public."ESTADISTICA" VALUES (271, 5, 35, 14, 1, 10);
INSERT INTO public."ESTADISTICA" VALUES (272, 8, 35, 16, 9, 12);
INSERT INTO public."ESTADISTICA" VALUES (273, 12, 35, 5, 5, 1);
INSERT INTO public."ESTADISTICA" VALUES (274, 17, 35, 19, 3, 13);
INSERT INTO public."ESTADISTICA" VALUES (275, 23, 35, 2, 9, 10);
INSERT INTO public."ESTADISTICA" VALUES (276, 1, 36, 17, 3, 8);
INSERT INTO public."ESTADISTICA" VALUES (277, 2, 36, 12, 2, 3);
INSERT INTO public."ESTADISTICA" VALUES (278, 4, 36, 12, 1, 9);
INSERT INTO public."ESTADISTICA" VALUES (279, 7, 36, 3, 9, 2);
INSERT INTO public."ESTADISTICA" VALUES (280, 11, 36, 3, 4, 1);
INSERT INTO public."ESTADISTICA" VALUES (281, 16, 36, 12, 0, 9);
INSERT INTO public."ESTADISTICA" VALUES (282, 22, 36, 16, 1, 6);
INSERT INTO public."ESTADISTICA" VALUES (283, 1, 37, 5, 4, 8);
INSERT INTO public."ESTADISTICA" VALUES (284, 2, 37, 9, 2, 6);
INSERT INTO public."ESTADISTICA" VALUES (285, 4, 37, 15, 6, 12);
INSERT INTO public."ESTADISTICA" VALUES (286, 7, 37, 18, 3, 12);
INSERT INTO public."ESTADISTICA" VALUES (287, 11, 37, 19, 5, 6);
INSERT INTO public."ESTADISTICA" VALUES (288, 16, 37, 17, 7, 14);
INSERT INTO public."ESTADISTICA" VALUES (289, 22, 37, 6, 4, 1);
INSERT INTO public."ESTADISTICA" VALUES (290, 1, 38, 19, 0, 14);
INSERT INTO public."ESTADISTICA" VALUES (291, 2, 38, 10, 9, 5);
INSERT INTO public."ESTADISTICA" VALUES (292, 4, 38, 19, 5, 0);
INSERT INTO public."ESTADISTICA" VALUES (293, 7, 38, 10, 4, 0);
INSERT INTO public."ESTADISTICA" VALUES (294, 11, 38, 8, 3, 1);
INSERT INTO public."ESTADISTICA" VALUES (295, 16, 38, 7, 8, 11);
INSERT INTO public."ESTADISTICA" VALUES (296, 22, 38, 11, 8, 11);
INSERT INTO public."ESTADISTICA" VALUES (297, 1, 39, 7, 2, 14);
INSERT INTO public."ESTADISTICA" VALUES (298, 2, 39, 15, 4, 1);
INSERT INTO public."ESTADISTICA" VALUES (299, 4, 39, 19, 0, 3);
INSERT INTO public."ESTADISTICA" VALUES (300, 7, 39, 11, 7, 14);
INSERT INTO public."ESTADISTICA" VALUES (301, 11, 39, 11, 9, 4);
INSERT INTO public."ESTADISTICA" VALUES (302, 16, 39, 16, 9, 11);
INSERT INTO public."ESTADISTICA" VALUES (303, 22, 39, 16, 4, 12);
INSERT INTO public."ESTADISTICA" VALUES (304, 1, 40, 13, 8, 6);
INSERT INTO public."ESTADISTICA" VALUES (305, 2, 40, 14, 2, 7);
INSERT INTO public."ESTADISTICA" VALUES (306, 4, 40, 4, 1, 6);
INSERT INTO public."ESTADISTICA" VALUES (307, 7, 40, 17, 8, 14);
INSERT INTO public."ESTADISTICA" VALUES (308, 11, 40, 9, 5, 11);
INSERT INTO public."ESTADISTICA" VALUES (309, 16, 40, 5, 4, 7);
INSERT INTO public."ESTADISTICA" VALUES (310, 22, 40, 8, 5, 13);


--
-- TOC entry 5078 (class 0 OID 16441)
-- Dependencies: 222
-- Data for Name: INSCRIPCION; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."INSCRIPCION" VALUES (8, 8, 1, '2026-04-12');
INSERT INTO public."INSCRIPCION" VALUES (7, 7, 1, '2026-04-12');
INSERT INTO public."INSCRIPCION" VALUES (6, 6, 1, '2026-04-12');
INSERT INTO public."INSCRIPCION" VALUES (5, 5, 1, '2026-04-12');
INSERT INTO public."INSCRIPCION" VALUES (4, 4, 1, '2026-04-12');
INSERT INTO public."INSCRIPCION" VALUES (3, 3, 1, '2026-04-12');
INSERT INTO public."INSCRIPCION" VALUES (2, 2, 1, '2026-04-12');
INSERT INTO public."INSCRIPCION" VALUES (1, 1, 1, '2026-04-12');
INSERT INTO public."INSCRIPCION" VALUES (12, 4, 2, '2026-04-12');
INSERT INTO public."INSCRIPCION" VALUES (11, 3, 2, '2026-04-12');
INSERT INTO public."INSCRIPCION" VALUES (10, 2, 2, '2026-04-12');
INSERT INTO public."INSCRIPCION" VALUES (9, 1, 2, '2026-04-12');


--
-- TOC entry 5082 (class 0 OID 16514)
-- Dependencies: 226
-- Data for Name: SPONSOR; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."SPONSOR" VALUES (5, 'hp', 'tecnologia');
INSERT INTO public."SPONSOR" VALUES (4, 'lenovo', 'tecnologia');
INSERT INTO public."SPONSOR" VALUES (3, 'apple', 'tecnologia');
INSERT INTO public."SPONSOR" VALUES (2, 'samsung', 'tecnologia');
INSERT INTO public."SPONSOR" VALUES (1, 'spotify', 'musica');


--
-- TOC entry 5081 (class 0 OID 16501)
-- Dependencies: 225
-- Data for Name: PATROCINIO; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."PATROCINIO" VALUES (5, 5, 1, 100);
INSERT INTO public."PATROCINIO" VALUES (4, 4, 1, 99);
INSERT INTO public."PATROCINIO" VALUES (3, 3, 1, 100);
INSERT INTO public."PATROCINIO" VALUES (2, 2, 1, 100);
INSERT INTO public."PATROCINIO" VALUES (1, 1, 1, 100);


--
-- TOC entry 5091 (class 0 OID 0)
-- Dependencies: 229
-- Name: ESTADISTICA_id_estadistica_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."ESTADISTICA_id_estadistica_seq"', 310, true);


--
-- TOC entry 5092 (class 0 OID 0)
-- Dependencies: 228
-- Name: PARTIDA_id_partida_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."PARTIDA_id_partida_seq"', 31, true);


-- Completed on 2026-04-12 23:16:48

--
-- PostgreSQL database dump complete
--


