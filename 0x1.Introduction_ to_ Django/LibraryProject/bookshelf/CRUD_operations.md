# CRUD_operations

#Create_Operation

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output
# Book instance created: <Book: 1984>

#Retrieve_Operation

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")
book

# Expected Output
# <Book: 1984>

#Update_Operation

```python
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output
# Book instance updated: <Book: Nineteen Eighty-Four>

#Delete_Operation

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