# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")
book

# Expected Output
# <Book: 1984>