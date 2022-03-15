import sqlite3

from DAO import *


class _Repository:
    def __init__(self, path):
        self._conn = sqlite3.connect(path)
        self.hats = Hats(self._conn)
        self.suppliers = Suppliers(self._conn)
        self.orders = Orders(self._conn)
        self.list_of_orders = []

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
            CREATE TABLE IF NOT EXISTS hats(
            id INTEGER PRIMARY KEY,
            topping STRING NOT NULL, 
            supplier INTEGER REFERENCES suppliers(id),
            quantity INTEGER NOT NULL 
            );

            CREATE TABLE IF NOT EXISTS suppliers(
            id INTEGER PRIMARY KEY,
            name STRING NOT NULL
            );

            CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY,
            location STRING NOT NULL,
            hat INTEGER REFERENCES hats(id)
            );
        """)
        self._conn.commit()

    def parse_orders(self, path):
        file = open(path, 'r')
        content = file.read()
        orders_file = content.split("\n")
        for line in orders_file:
            line = line.split(",")
            relevant_row = self.hats.find_a_supplier(line[1])
            # [0] = hat_id, [1] = supp_id, [2] = quantity
            order = Order(line[0], int(relevant_row[0]))
            self.orders.insert(order)
            if relevant_row[2] > 1:
                self.hats.update_quantity(relevant_row[0], relevant_row[2] - 1)
            else:
                self.hats.delete_row(relevant_row[0])
            self._conn.commit()
            supplier_name = self.suppliers.find(relevant_row[1]).name
            order_sent = (line[1], supplier_name, line[0])
            self.list_of_orders.append(order_sent)

    def create_output(self, path):
        file = open(path, 'w')
        for order_sent in self.list_of_orders:
            to_write = str(order_sent[0]) + "," + str(order_sent[1]) + "," + str(order_sent[2])
            file.write(to_write + "\n")
        file.close()

    def commit(self):
        self._conn.commit()



