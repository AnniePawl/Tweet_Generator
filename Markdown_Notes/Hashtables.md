# Hash Table Notes
A Hash Table is a data structure that is used to store key/value pairs. It uses a **hash function** to compute an *index* into an array of buckets, from which an element can be inserted or search.

## Implementation
1. An element is converted into an integer by using a hash function. This element can be used as an index to store original element, which falls into hash table.
2. The element is stored in the hash table where it can be quickly retrieved using hashed key

```
hash = hashfunc(key)
index = hash % array_size
```

### Basic Requirements
1. **Easy to Compute**
2. **Uniform Distribution** across hash table, shouldn't result in clustering
3. **Less Collisions**, which occur when pairs of elements are mapped to the same hash value

### When to Use
- **Associative Arrays:** Hash tables are commonly used to implement many types of in-memory tables. Used to implement associative arrays (arrays whose indices are arbitrary strings or other complicated objects)
- **Database Indexing:** Hash tables can be used as disk-based data structures and database indices
- **Caches:** HT can be used to implement caches that speed up access to data
- **Object Representation:**

## The Hash Function
Any function that can be used to map a data set of an arbitrary size to a data set of a fixed size, which falls into the hash table. The values returned by a hash function are called **hash values, hash codes, hash sums** or just **hashes**.

### Collisions
A **Hash Collision** is where a hash function generates the same index for more than one key. Ideally, the hash function will assign each key to a unique bucket, but it's impossible to map all possible input to a fixed output space without some inputs generating the same output...

### Chaining
Chaining is a way to handle collisions. The idea is to make each cell of the hash table point to a linked list of records that have the same hash function value. All collision, retrieval and deletion functions can be handled by the list and hash function just guides to algorithms.

### Linear Probing
Linear probing is a form of open addressing that helps handle collisions. When a collision happens, Linear probing searches for the closest following key location and inserts new key there.

### Load Factor = entries / buckets
The load factor refers to the number of keys stored in a hash table, divided by the capacity. Size should be chosen to load factor is less than one. As load factor gets closer to 100%, the number of probes that may be needed to find or insert a key rises dramatically.

### Pros
- Super speedy! Especially when number of entries is large, uses constant time on average
- *Inserting and Deleting:* O(1) + Hashing and Indexing (amortized)
- *Direct access:* O(n) + Hashing and Indexing

### Cons
- A little more memory space than arrays
- Retrieval of elements doesn't guarantee specific order
- Accessing data in a sorted order is very time consuming
- Poor locality of reference, distributed seemingly randomly
- Searching for a value (without know it's key)
- Can be a little more difficult to write and use
