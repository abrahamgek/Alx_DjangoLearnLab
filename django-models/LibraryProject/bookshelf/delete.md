# Delete Operation

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book instance
book.delete()

# Verify deletion
Book.objects.all()

# Expected Output
# QuerySet should be empty
# <QuerySet []>