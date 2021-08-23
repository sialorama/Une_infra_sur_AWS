import psycopg2


class Data:

    @classmethod
    def open_db(cls):
        cls.conn = psycopg2.connect(
            host="postgres-db.cs0pdb25dfum.us-east-1.rds.amazonaws.com",
            database="exercises",
            user="postgres",
            password="rtyfghrtyfgh",
            port='5432')
        cls.cur = cls.conn.cursor()

    @classmethod
    def close_db(cls):
        cls.cur.close()
        cls.conn.close()

    @classmethod
    def name(cls):
        cls.open_db()
        cls.cur.execute("SELECT name, membercost FROM cd.facilities")
        query_results = cls.cur.fetchall()
        cls.close_db()
        return query_results

    @classmethod
    def member(cls):
        cls.open_db()
        cls.cur.execute("SELECT surname, firstname, address, zipcode FROM cd.members")
        query_results = cls.cur.fetchall()
        cls.close_db()
        return query_results
