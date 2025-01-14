from collections.abc import MutableSequence, Sequence


class HashTable:
    # Create empty bucket list of given size
    def __init__(self, size) -> None:
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, val) -> None:
        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        found_index = 0
        for i, record in enumerate(bucket):
            record_key, _ = record

            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                found_index = i
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[found_index] = (key, val)
        else:
            bucket.append((key, val))

    def get_val(self, key):
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for _, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        return "No record found"

    # Remove a value with specific key
    def delete_val(self, key) -> None:
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)

    # To print the items of hash map
    def __str__(self) -> str:
        return "".join(str(item) for item in self.hash_table)


class Bar:
    def __init__(self, size) -> None:
        self.size = size
        self.buckets = self.create_buckets(size)

    @staticmethod
    def create_buckets(size) -> MutableSequence[Sequence[int]]:
        return [() for _ in range(size)]

    def set_value(self, key, value) -> None:
        key_hash = hash(key) % self.size

        for index, item in enumerate(self.buckets):
            item_key, item_value = item

            if item_key == key_hash:
                self.buckets[index] = (item_key, value)
                return

        self.buckets.append([key_hash, value])

    def get_value(self, key) -> int:
        key_hash = hash(key) % self.size

        for index, item in enumerate(self.buckets):
            item_key, item_value = item

            if item_key == key_hash:
                return self.buckets[index][1]

        return 0

    def delete_value(self, key) -> None:
        key_hash = hash(key) % self.size

        for index, item in enumerate(self.buckets):
            item_key, item_value = item

            if item_key == key_hash:
                self.buckets.pop(index)

    def __str__(self) -> str:
        return "".join((str(value) for key, value in self.buckets))


if __name__ == "__main__":
    hash_table = HashTable(50)

    # insert some values
    hash_table.set_val("gfg@example.com", "some value")

    hash_table.set_val("portal@example.com", "some other value")

    # search/access a record with key

    # delete or remove a value
    hash_table.delete_val("portal@example.com")
