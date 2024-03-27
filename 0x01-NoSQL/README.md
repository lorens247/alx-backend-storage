#0x01 -  NoSQL

## Table of Contents

- [1. Introduction](#1-introduction)
- [2. Difference Between SQL and NoSQL](#2-difference-between-sql-and-nosql)
- [3. ACID](#3-acid)
- [4. Document Storage](#4-document-storage)
- [5. Types of NoSQL Databases](#5-types-of-nosql-databases)
- [6. Benefits of NoSQL Databases](#6-benefits-of-nosql-databases)
- [7. Querying NoSQL Databases](#7-querying-nosql-databases)
- [8. Manipulating Data in NoSQL Databases](#8-manipulating-data-in-nosql-databases)
- [9. Using MongoDB](#9-using-mongodb)

## 1. Introduction

NoSQL, or "Not Only SQL," is a term used to describe databases that are designed to handle large volumes of unstructured, semi-structured, or structured data. Unlike traditional relational databases (SQL), which use a predefined schema and tables, NoSQL databases offer more flexibility and scalability for handling diverse data types and distributed architectures.

## 2. Difference Between SQL and NoSQL

SQL databases are based on a structured schema, typically using tables to store data, while NoSQL databases are schema-less or have a flexible schema, allowing for easier handling of dynamic and evolving data structures.

## 3. ACID

ACID stands for Atomicity, Consistency, Isolation, and Durability. It is a set of properties that ensures database transactions are processed reliably. While traditional SQL databases generally adhere strictly to ACID principles, NoSQL databases may sacrifice some of these properties in favor of performance and scalability.

## 4. Document Storage

Document storage is a method used by many NoSQL databases, where data is stored in a semi-structured format, such as JSON or XML documents. These documents can vary in structure, allowing for more flexibility compared to the rigid structure of tables in SQL databases.

## 5. Types of NoSQL Databases

NoSQL databases can be categorized into several types, including:

- Document Stores (e.g., MongoDB)
- Key-Value Stores (e.g., Redis)
- Column-Family Stores (e.g., Cassandra)
- Graph Databases (e.g., Neo4j)

Each type has its own strengths and use cases, catering to different data storage and retrieval needs.

## 6. Benefits of NoSQL Databases

Some benefits of using NoSQL databases include:

- Scalability: NoSQL databases are designed to scale horizontally, allowing for efficient distribution of data across multiple servers.
- Flexibility: NoSQL databases can handle various data types and structures, making them suitable for dynamic and evolving applications.
- Performance: NoSQL databases often offer high performance for read and write operations, especially in distributed environments.

## 7. Querying NoSQL Databases

Querying data in NoSQL databases typically involves using specialized query languages or APIs provided by the database system. Each NoSQL database may have its own query syntax and capabilities tailored to its data model.

## 8. Manipulating Data in NoSQL Databases

To insert, update, or delete data in a NoSQL database, developers typically interact with the database using specific commands or APIs provided by the database system. These operations may vary depending on the type of NoSQL database being used and its associated data model.

## 9. Using MongoDB

MongoDB is one of the most popular document-oriented NoSQL databases. It stores data in flexible, JSON-like documents, making it suitable for a wide range of use cases. To use MongoDB, you can follow the official documentation and guides provided by MongoDB Inc., which cover installation, configuration, querying, and data manipulation tasks.
