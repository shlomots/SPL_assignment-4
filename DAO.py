from DTOs import *
import sqlite3


class Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, hat):
        self._conn.execute("""
            INSERT INTO hats (id, topping, supplier, quantity) VALUES (?, ?, ?, ?)
            """, [hat.id, hat.topping, hat.supplier, hat.quantity])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, topping, supplier, quantity FROM hats WHERE id = ?
            """, [id])
        return Hat(*c.fetchone())

    def find_a_supplier(self, topping):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, supplier, quantity FROM hats WHERE topping = ?
            """, [topping])
        all = c.fetchall()
        supplier_id = all[0][1]
        relevant_row = all[0]
        for i in range(len(all)):
            if all[i][1] < supplier_id:
                relevant_row = all[i]
        return relevant_row

    def update_quantity(self, id, quantity_update):
        self._conn.execute("""
            UPDATE hats
            SET quantity = quantity-1 WHERE id = ?
            """, [id])

    def delete_row(self, id):
        self._conn.execute("""
            DELETE FROM hats WHERE id = ?
            """, [id])


class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
            INSERT INTO suppliers (id, name) VALUES (?, ?)
            """, [supplier.id, supplier.name])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name FROM suppliers WHERE id = ?
            """, [id])
        return Supplier(*c.fetchone())


class Orders:
    id_counter = 1

    def __init__(self, conn):
        self._conn = conn

    def insert(self, order):
        self._conn.execute("""
            INSERT INTO orders (id, location, hat) VALUES (?, ?, ?)
            """, [self.id_counter, order.location, order.hat])
        self.id_counter += 1

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, location, hat FROM orders WHERE id = ?
            """, [id])
        return Order(*c.fetchone())
