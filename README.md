Project Description

This project implements a Bloom Filter using Python, demonstrating a space-efficient probabilistic data structure used to test whether an element belongs to a set.

Bloom Filters provide:

Fast insertion and lookup

No false negatives

A small chance of false positives

This project is ideal for Data Structures & Algorithms coursework, Python practice, and understanding real-world systems like caching and databases.

🛠️ Technologies Used

Python

Data Structures

Hash Functions

Bit Array / Boolean Array

⚙️ Working Principle

Initialize a fixed-size bit array with all bits set to 0

Apply multiple hash functions to each element

Set bits at calculated indices during insertion

For lookup:

If any bit is 0 → element is definitely not present

If all bits are 1 → element may be present

✨ Features

Efficient insert operation

Fast membership checking

Configurable bit array size

Configurable number of hash functions

Zero false negatives

Memory-efficient design

📂 Project Structure
BloomFilter/
│
├── bloom_filter.py
├── main.py
└── README.md

🚀 How to Run the Project

Clone the repository

Navigate to the project directory

cd BloomFilter


Run the program

python main.py

🧪 Example Usage

Add elements to the Bloom Filter

Check if an element exists

Observe probabilistic behavior (possible false positives)

📚 Applications of Bloom Filters

Web caching systems

Database query optimization

Duplicate detection

Network packet filtering

Spell checkers

Password breach detection

🎯 Learning Outcomes

Understanding probabilistic data structures

Implementing hash-based algorithms in Python

Analyzing space vs accuracy trade-offs

Applying theory to practical use cases

🔮 Future Enhancements

False positive probability calculation

Counting Bloom Filter

Dynamic Bloom Filter

Visualization of bit array

Performance comparison with Python set
