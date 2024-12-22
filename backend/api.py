from flask import Flask, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix
import pymysql
from dotenv import load_dotenv
import os
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)


def get_db_connection():
    return pymysql.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        user=os.getenv('MYSQL_USERNAME', 'root'),
        password=os.getenv('MYSQL_PASSWORD', ''),
        database=os.getenv('MYSQL_DATABASE', 'test_db'),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.get('/donations')
def get_donations():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM donation"
            cursor.execute(sql)
            results = cursor.fetchall()
        connection.close()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.get('/donations/<int:donation_id>')
def get_donation(donation_id):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM donation WHERE id = %s"
            cursor.execute(sql, (donation_id,))
            result = cursor.fetchone()
        connection.close()
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Donation not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.post('/donations')
def create_donation():
    data = request.json
    donator = data.get('donator')
    organ = data.get('organ')
    availability = data.get('availability', 0)

    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "INSERT INTO donation (donator, organ, availability) VALUES (%s, %s, %s)"
            cursor.execute(sql, (donator, organ, availability))
            connection.commit()
        connection.close()
        return jsonify({"message": "Donation created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.put('/donations/<int:donation_id>')
def update_donation(donation_id):
    data = request.json
    donator = data.get('donator')
    organ = data.get('organ')
    availability = data.get('availability')

    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = """
            UPDATE donation
            SET donator = %s, organ = %s, availability = %s
            WHERE id = %s
            """
            rows_updated = cursor.execute(sql, (donator, organ, availability, donation_id))
            connection.commit()
        connection.close()
        if rows_updated:
            return jsonify({"message": "Donation updated successfully"}), 200
        else:
            return jsonify({"error": "Donation not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.delete('/donations/<int:donation_id>')
def delete_donation(donation_id):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            sql = "DELETE FROM donation WHERE id = %s"
            rows_deleted = cursor.execute(sql, (donation_id,))
            connection.commit()
        connection.close()
        if rows_deleted:
            return jsonify({"message": "Donation deleted successfully"}), 200
        else:
            return jsonify({"error": "Donation not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(
        host=os.getenv('FLASK_HOST', '127.0.0.1'),
        port=int(os.getenv('FLASK_PORT', 5000))
    )