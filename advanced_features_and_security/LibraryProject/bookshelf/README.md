# Permissions and Groups Setup

This Django application uses custom permissions and groups to control access to certain actions on the Book model.

## Custom Permissions
The `Book` model includes the following custom permissions:
- `can_view`: Allows users to view book details.
- `can_create`: Allows users to create new book entries.
- `can_edit`: Allows users to edit existing book entries.
- `can_delete`: Allows users to delete book entries.

## Groups
- `Editors`: Can create and edit books.
- `Viewers`: Can view book details.
- `Admins`: Full access, including delete permissions.

## Implementation
Permissions are enforced in views using the `@permission_required` decorator.
