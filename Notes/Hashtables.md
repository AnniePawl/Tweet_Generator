# Hash Table Notes
A Hash Table is a data structure that is used to store key/value pairs. It uses a **hash function** to compute an *index* into an array of buckets, from which an element can be inserted or search.

## Implementation
1. An element is converted into an integer by using a hash function. This element can be used as an index to store original element, which falls into hash table.
2. The element is stored in the hash table where it can be quickly retrieved using hashed key

```
hash = hashfunc(key)
index = hash % array_size
```

### The Hash Function
Any function that can be used to map a data set of an arbitrary size to a data set of a fixed size, which falls into the hash table. The values returned by a hash function are called **hash values, hash codes, hash sums** or just **hashes**.

#### Basic Requirements
1. **Easy to Compute**
2. **Uniform Distribution** across hash table, shouldn't result in clustering
3. **Less Collisions**, which occur when pairs of elements are mapped to the same hash value

### When to Use
- **Associative Arrays:** Hash tables are commonly used to implement many types of in-memory tables. Used to implement associative arrays (arrays whose indices are arbitrary strings or other complicated objects)
- **Database Indexing:** Hash tables can be used as disk-based data structures and database indices
- **Caches:** HT can be used to implement caches that speed up access to data
- **Object Representation:** 
