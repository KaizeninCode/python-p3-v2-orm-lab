from __init__ import CONN, CURSOR


class Review:
    def __init__(self, year, summary, employee_id, id=None):
        self.id = id
        self.year = year
        self.summary = summary
        self.employee_id = employee_id

    def save(self):
        """Insert a new row with the year, summary, and employee_id values of the current Review object.
        Update object id attribute using the primary key value of new row."""
        sql = """
            INSERT INTO reviews (id, year, summary, employee_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """
        CURSOR.execute(sql, (self.id, self.year, self.summary, self.employee_id))
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Review instances """
        sql = """
            DROP TABLE IF EXISTS reviews;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Review instances """
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY Key,
                year INT,
                summary TEXT,
                employee_id INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, year, summary, employee_id):
        """ Initialize a new Review instance and save the object to the database.
        Return the new instance."""
        sql = '''
            INSERT INTO reviews (year, summary, employee_id)
            VALUES (?, ?, ?);
            '''
        CURSOR.execute(sql, (year, summary, employee_id))
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        """Return a Review instance having the attribute values from the table row."""
        # Check the dictionary for existing instance using the row's primary key
        pass

        # Create a new Review instance
        review = Review(id=row[0], year=row[1], summary=row[2], employee_id=row[3])

        # Save the object in local dictionary using table row's PK as dictionary key
        pass

        # Return the new instance
        return review

    @classmethod
    def find_by_id(cls, id):
        """Return a Review instance having the attribute values from the table row."""
        # Check the dictionary for existing instance using the id
        pass

        # Create a new Review instance
        review = Review(id=id, year=None, summary=None, employee_id=None)

        # Save the object in local dictionary using table row's PK as dictionary key
        pass

        # Return the new instance
        return review

    @classmethod
    def update(self):
        """Update the table row corresponding to the current Review instance."""
        sql = """
            UPDATE reviews
            SET year = %s, summary = %s, employee_id = %s
            WHERE id = %s;
        """
        CURSOR.execute(sql, (self.year, self.summary, self.employee_id, self.id))
        CONN.commit()

    @classmethod
    def delete(self):
        """Delete the table row corresponding to the current Review instance,
        delete the dictionary entry, and reassign id attribute"""

        # Delete the table row corresponding to the current Review instance
        sql = """
            DELETE FROM reviews
            WHERE id = %s;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Reassign id attribute
        self.id = None

        # Return the updated instance
        return self
    
    def reviews(self):
        """Return a list of Review instances for the current Employee instance."""
        if self.id is None:
            return []

        sql = """
            SELECT *
            FROM reviews
            WHERE employee_id = %s;
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        reviews = [Review.instance_from_db(row) for row in rows]
        return reviews