from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")
DB_PORT = os.getenv("DB_PORT", "5432")


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )


@app.route("/")
def home():
    return jsonify({
        "message": "DevOps Dockerized Web App is running"
    })


@app.route("/health")
def health():
    conn = None
    try:
        conn = get_connection()
        return jsonify({
            "status": "ok",
            "database": "connected"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "database": str(e)
        }), 500
    finally:
        if conn:
            conn.close()


@app.route("/users")
def users():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, email FROM users ORDER BY id;")
        rows = cur.fetchall()

        result = []
        for row in rows:
            result.append({
                "id": row[0],
                "name": row[1],
                "email": row[2]
            })

        return jsonify(result), 200
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)