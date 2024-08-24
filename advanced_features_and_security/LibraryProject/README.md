# LibraryProject
This is a Django project named LibraryProject.
## Custom Permissions and Groups Setup

### Custom Permissions

The following custom permissions have been added to the `Book` model:
- `can_view`: Allows viewing Book.
- `can_create`: Allows creating new Book.
- `can_edit`: Allows editing existing Book.
- `can_delete`: Allows deleting Book.

### Groups and Permissions

Groups and their associated permissions:
- **Editors**: `can_edit`, `can_create`
- **Viewers**: `can_view`
- **Admins**: All permissions (`can_view`, `can_create`, `can_edit`, `can_delete`)

### Enforcing Permissions

Permissions are enforced in views using the `@permission_required` decorator. Ensure users have the necessary permissions to access or modify resources.
