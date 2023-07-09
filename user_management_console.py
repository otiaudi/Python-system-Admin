import cmd
import json

class UserManagementConsole(cmd.Cmd):
    prompt = 'user> '
    intro = 'Welcome to the User Management Console. Type "help" to see available commands.'

    def __init__(self):
        super().__init__()
        self.users = {}

    def do_create(self, arg):
        """Create a new user. Syntax: create <username> <email>"""
        args = arg.split()
        if len(args) != 2:
            print('Invalid syntax. Please provide username and email.')
            return
        username, email = args
        if username in self.users:
            print('User already exists.')
            return
        self.users[username] = {'email': email}
        print('User created successfully.')

    def do_update(self, arg):
        """Update user information. Syntax: update <username> <email>"""
        args = arg.split()
        if len(args) != 2:
            print('Invalid syntax. Please provide username and new email.')
            return
        username, new_email = args
        if username not in self.users:
            print('User does not exist.')
            return
        self.users[username]['email'] = new_email
        print('User information updated successfully.')

    def do_delete(self, arg):
        """Delete a user. Syntax: delete <username>"""
        username = arg.strip()
        if username not in self.users:
            print('User does not exist.')
            return
        del self.users[username]
        print('User deleted successfully.')

    def do_list(self, arg):
        """List all users."""
        if not self.users:
            print('No users found.')
            return
        for username, data in self.users.items():
            email = data['email']
            print(f'Username: {username}\tEmail: {email}')

    def do_save(self, arg):
        """Save user data to a file. Syntax: save <filename>"""
        filename = arg.strip()
        if not filename:
            print('Please provide a filename.')
            return
        with open(filename, 'w') as f:
            json.dump(self.users, f)
        print(f'User data saved to {filename}.')

    def do_load(self, arg):
        """Load user data from a file. Syntax: load <filename>"""
        filename = arg.strip()
        if not filename:
            print('Please provide a filename.')
            return
        try:
            with open(filename, 'r') as f:
                self.users = json.load(f)
            print(f'User data loaded from {filename}.')
        except FileNotFoundError:
            print(f'File {filename} not found.')

    def do_quit(self, arg):
        """Exit the program."""
        print('Exiting...')
        return True

if __name__ == '__main__':
    UserManagementConsole().cmdloop()

