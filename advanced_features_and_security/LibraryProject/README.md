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

# Security Measures Implemented

## Security Settings
- **DEBUG**: Set to `False` in production.
- **SECURE_BROWSER_XSS_FILTER**: Enabled to protect against XSS.
- **X_FRAME_OPTIONS**: Set to `DENY` to prevent clickjacking.
- **SECURE_CONTENT_TYPE_NOSNIFF**: Enabled to prevent MIME type sniffing.
- **CSRF_COOKIE_SECURE** and **SESSION_COOKIE_SECURE**: Set to `True` to enforce HTTPS for cookies.
- **SECURE_SSL_REDIRECT**: Redirects HTTP to HTTPS.

## CSRF Protection
- All forms include `{% csrf_token %}` to protect against CSRF attacks.

## SQL Injection Protection
- Used Django ORM for database queries.
- Validated and sanitized user inputs using Django forms.

## Content Security Policy
- Implemented CSP with `django-csp` middleware to mitigate XSS risks.
