# Access Control Setup

## Model Permissions
The `Book` model has the following custom permissions:
- `can_view_book`: Allows viewing books.
- `can_create_book`: Allows creating books.
- `can_edit_book`: Allows editing books.
- `can_delete_book`: Allows deleting books.

## Groups and Permissions
- **Viewers**: Has `can_view_book` permission.
- **Editors**: Has `can_view_book`, `can_create_book`, and `can_edit_book` permissions.
- **Admins**: Has `can_view_book`, `can_create_book`, `can_edit_book`, and `can_delete_book` permissions.

## Views
Permissions are enforced in views using the `@permission_required` decorator:
- `book_list`: Requires `can_view_book`.
- `book_create`: Requires `can_create_book`.
- `book_edit`: Requires `can_edit_book`.
- `book_delete`: Requires `can_delete_book`.
