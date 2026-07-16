const express = require('express');
const { Pool } = require('pg');
const path = require('path');
 
const app = express();
app.use(express.json());
app.use(express.static('public'));
 
const pool = new Pool({
  user: process.env.PGUSER || 'postgres',
  host: process.env.PGHOST || 'localhost',
  database: process.env.PGDATABASE || 'tarea1',
  password: process.env.PGPASSWORD || 'postgres',
  port: Number(process.env.PGPORT || 5432),
});
 
// ─────────────────────────────────────────────
// PÁGINA 1: TORNEOS
// ─────────────────────────────────────────────
 
app.get('/api/torneos', async (req, res) => {
  try {
    const result = await pool.query(`
      SELECT id_torneo, nombre, videojuego, fecha_inicio, fecha_fin, price_pool_usd, max_equipos
      FROM "TORNEO"
      ORDER BY fecha_inicio DESC
    `);
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
 
app.get('/api/torneos/:id/posiciones', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await pool.query(`
      SELECT
        e.nombre AS equipo,
        COUNT(p.id_partida) AS jugadas,
        SUM(CASE
          WHEN (p."id_equipo_A" = e.id_equipo AND p."puntaje_equipo_A" > p.puntaje_equipo_b)
            OR (p."id_equipo_B" = e.id_equipo AND p.puntaje_equipo_b > p."puntaje_equipo_A") THEN 1 ELSE 0 END) AS ganadas,
        SUM(CASE
          WHEN p."puntaje_equipo_A" = p.puntaje_equipo_b THEN 1 ELSE 0 END) AS empatadas,
        SUM(CASE
          WHEN (p."id_equipo_A" = e.id_equipo AND p."puntaje_equipo_A" < p.puntaje_equipo_b)
            OR (p."id_equipo_B" = e.id_equipo AND p.puntaje_equipo_b < p."puntaje_equipo_A") THEN 1 ELSE 0 END) AS perdidas,
        SUM(CASE
          WHEN (p."id_equipo_A" = e.id_equipo AND p."puntaje_equipo_A" > p.puntaje_equipo_b)
            OR (p."id_equipo_B" = e.id_equipo AND p.puntaje_equipo_b > p."puntaje_equipo_A") THEN 3
          WHEN p."puntaje_equipo_A" = p.puntaje_equipo_b THEN 1
          ELSE 0 END) AS puntos
      FROM "EQUIPO" e
      JOIN "INSCRIPCION" i ON i.id_equipo = e.id_equipo
      JOIN "PARTIDA" p ON (p."id_equipo_A" = e.id_equipo OR p."id_equipo_B" = e.id_equipo)
        AND p.id_torneo = i.id_torneo
      WHERE i.id_torneo = $1 AND p.fase = 'fase de grupos'
      GROUP BY e.id_equipo, e.nombre
      ORDER BY puntos DESC, ganadas DESC
    `, [id]);
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
 
app.get('/api/torneos/:id/partidas', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await pool.query(`
      SELECT
        p.id_partida,
        ea.nombre AS equipo_a,
        eb.nombre AS equipo_b,
        p."puntaje_equipo_A" AS puntaje_equipo_a,
        p.puntaje_equipo_b,
        p.fecha_hora,
        p.fase
      FROM "PARTIDA" p
      JOIN "EQUIPO" ea ON p."id_equipo_A" = ea.id_equipo
      JOIN "EQUIPO" eb ON p."id_equipo_B" = eb.id_equipo
      WHERE p.id_torneo = $1
      ORDER BY p.fecha_hora
    `, [id]);
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
 
app.get('/api/torneos/:id/equipos-sponsors', async (req, res) => {
  try {
    const { id } = req.params;
    const equipos = await pool.query(`
      SELECT e.nombre
      FROM "EQUIPO" e
      JOIN "INSCRIPCION" i ON i.id_equipo = e.id_equipo
      WHERE i.id_torneo = $1
      ORDER BY e.nombre
    `, [id]);
    const sponsors = await pool.query(`
      SELECT s.nombre, s.industria, pa.monto_usd
      FROM "SPONSOR" s
      JOIN "PATROCINIO" pa ON pa.id_sponsor = s.id_sponsor
      WHERE pa.id_torneo = $1
      ORDER BY pa.monto_usd DESC
    `, [id]);
    res.json({ equipos: equipos.rows, sponsors: sponsors.rows });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
 
// ─────────────────────────────────────────────
// PÁGINA 2: ESTADÍSTICAS
// ─────────────────────────────────────────────
 
app.get('/api/estadisticas/:id/ranking', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await pool.query(`
      SELECT
        j.gamertag,
        e.nombre AS equipo,
        SUM(est.kos) AS total_kos,
        SUM(est.restarts) AS total_restarts,
        SUM(est.assists) AS total_assists,
        ROUND(
          CASE WHEN SUM(est.restarts) = 0 THEN SUM(est.kos)
               ELSE SUM(est.kos)::numeric / SUM(est.restarts)
          END, 2
        ) AS ratio
      FROM "ESTADISTICA" est
      JOIN "JUGADOR" j ON est.id_jugador = j.id_jugador
      JOIN "EQUIPO" e ON j.id_equipo = e.id_equipo
      JOIN "PARTIDA" p ON est.id_partida = p.id_partida
      WHERE p.id_torneo = $1
      GROUP BY j.id_jugador, j.gamertag, e.nombre
      HAVING COUNT(DISTINCT est.id_partida) >= 2
      ORDER BY ratio DESC
    `, [id]);
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
 
app.get('/api/estadisticas/:id/evolucion', async (req, res) => {
  try {
    const { id } = req.params;
    const { equipo } = req.query;
    const result = await pool.query(`
      SELECT
        CASE WHEN p.fase = 'fase de grupos' THEN 'Fase de Grupos'
             ELSE 'Eliminatorias' END AS fase,
        ROUND(AVG(est.kos), 2) AS avg_kos,
        ROUND(AVG(est.restarts), 2) AS avg_restarts,
        ROUND(AVG(est.assists), 2) AS avg_assists
      FROM "ESTADISTICA" est
      JOIN "PARTIDA" p ON est.id_partida = p.id_partida
      JOIN "JUGADOR" j ON est.id_jugador = j.id_jugador
      JOIN "EQUIPO" e ON j.id_equipo = e.id_equipo
      WHERE p.id_torneo = $1
        AND e.id_equipo = $2
        AND p.fase IN ('fase de grupos', 'semifinal', 'final')
      GROUP BY
        CASE WHEN p.fase = 'fase de grupos' THEN 'Fase de Grupos' ELSE 'Eliminatorias' END
    `, [id, equipo]);
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
 
app.get('/api/estadisticas/:id/equipos', async (req, res) => {
  try {
    const { id } = req.params;
    const result = await pool.query(`
      SELECT e.id_equipo, e.nombre
      FROM "EQUIPO" e
      JOIN "INSCRIPCION" i ON i.id_equipo = e.id_equipo
      WHERE i.id_torneo = $1
      ORDER BY e.nombre
    `, [id]);
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
 
// ─────────────────────────────────────────────
// PÁGINA 3: BÚSQUEDA
// ─────────────────────────────────────────────
 
app.get('/api/buscar', async (req, res) => {
  try {
    const { q } = req.query;
    const jugadores = await pool.query(`
      SELECT j.gamertag, j.nombre_real, j.pais, e.nombre AS equipo
      FROM "JUGADOR" j
      LEFT JOIN "EQUIPO" e ON j.id_equipo = e.id_equipo
      WHERE j.gamertag ILIKE $1 OR j.pais ILIKE $1
      ORDER BY j.gamertag
    `, [`%${q}%`]);
    const equipos = await pool.query(`
      SELECT
        e.nombre,
        COUNT(j.id_jugador) AS num_jugadores,
        COALESCE(
          ARRAY_AGG(
            CASE
              WHEN c.id_jugador IS NOT NULL THEN j.gamertag || ' (c)'
              ELSE j.gamertag
            END
            ORDER BY CASE WHEN c.id_jugador IS NOT NULL THEN 0 ELSE 1 END, j.gamertag
          ) FILTER (WHERE j.id_jugador IS NOT NULL),
          '{}'
        ) AS jugadores
      FROM "EQUIPO" e
      LEFT JOIN "JUGADOR" j ON j.id_equipo = e.id_equipo
      LEFT JOIN "Capitanes" c ON c.id_equipo = e.id_equipo AND c.id_jugador = j.id_jugador
      WHERE e.nombre ILIKE $1
      GROUP BY e.id_equipo, e.nombre
      ORDER BY e.nombre
    `, [`%${q}%`]);
    res.json({ jugadores: jugadores.rows, equipos: equipos.rows });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
 
// ─────────────────────────────────────────────
// PÁGINA 4: SPONSORS
// ─────────────────────────────────────────────
 
app.get('/api/videojuegos', async (req, res) => {
  try {
    const result = await pool.query(`
      SELECT DISTINCT videojuego FROM "TORNEO" ORDER BY videojuego
    `);
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
 
app.get('/api/sponsors', async (req, res) => {
  try {
    const { videojuego } = req.query;
    const result = await pool.query(`
      SELECT s.nombre, s.industria, SUM(pa.monto_usd) AS monto_total
      FROM "SPONSOR" s
      JOIN "PATROCINIO" pa ON pa.id_sponsor = s.id_sponsor
      JOIN "TORNEO" t ON pa.id_torneo = t.id_torneo
      WHERE t.videojuego = $1
      GROUP BY s.id_sponsor, s.nombre, s.industria
      HAVING COUNT(DISTINCT t.id_torneo) = (
        SELECT COUNT(*) FROM "TORNEO" WHERE videojuego = $1
      )
      ORDER BY monto_total DESC
    `, [videojuego]);
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
 
// ─────────────────────────────────────────────
// PÁGINA 5: FORMULARIO DE INSCRIPCIÓN
// ─────────────────────────────────────────────
 
app.get('/api/equipos', async (req, res) => {
  try {
    const result = await pool.query(`SELECT id_equipo, nombre FROM "EQUIPO" ORDER BY nombre`);
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
 
app.post('/api/inscribir', async (req, res) => {
  try {
    const { id_equipo, id_torneo } = req.body;

    if (!id_equipo || !id_torneo) {
      return res.status(400).json({ error: 'Debes enviar id_equipo e id_torneo.' });
    }
 
    const yaInscrito = await pool.query(`
      SELECT 1 FROM "INSCRIPCION" WHERE id_equipo = $1 AND id_torneo = $2
    `, [id_equipo, id_torneo]);
    if (yaInscrito.rows.length > 0) {
      return res.status(400).json({ error: 'Este equipo ya está inscrito en el torneo.' });
    }
 
    const torneo = await pool.query(`SELECT max_equipos FROM "TORNEO" WHERE id_torneo = $1`, [id_torneo]);
    if (torneo.rows.length === 0) {
      return res.status(404).json({ error: 'El torneo seleccionado no existe.' });
    }

    const inscritos = await pool.query(`SELECT COUNT(*) FROM "INSCRIPCION" WHERE id_torneo = $1`, [id_torneo]);
    if (parseInt(inscritos.rows[0].count) >= torneo.rows[0].max_equipos) {
      return res.status(400).json({ error: 'El torneo ya alcanzó su número máximo de equipos.' });
    }
 
    await pool.query(`
      INSERT INTO "INSCRIPCION" (id_inscripcion, id_equipo, id_torneo, fecha_inscripcion)
      SELECT COALESCE(MAX(id_inscripcion), 0) + 1, $1, $2, CURRENT_DATE
      FROM "INSCRIPCION"
    `, [id_equipo, id_torneo]);
 
    res.json({ mensaje: '¡Equipo inscrito exitosamente!' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});
 
// ─────────────────────────────────────────────
app.listen(3000, () => {
  console.log('Servidor corriendo en http://localhost:3000');
});

