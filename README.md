# AirBnB Clone Console

This is the command-line interface (CLI) for the AirBnB Clone project. The purpose of this project is to create a simple command interpreter to manage AirBnB objects. This CLI will allow you to create, retrieve, update, and delete objects related to AirBnB.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/OlabiyiTolu/AirBnB_clone.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AirBnB_clone
   ```

3. Run the console:
   ```bash
   ./console.py
   ```

## Commands

The following commands are available in the console:

- `create`: Create a new object.
- `show`: Display information about a specific object.
- `destroy`: Delete an object.
- `all`: Display information about all objects or all objects of a specific class.
- `update`: Update the attributes of an object.

## Examples

```bash
$ ./console.py
(hbnb) create User
96f1f017-5f7b-46b1-8daa-57927bc7e4e4
(hbnb) show User 96f1f017-5f7b-46b1-8daa-57927bc7e4e4
[User] (96f1f017-5f7b-46b1-8daa-57927bc7e4e4) {'id': '96f1f017-5f7b-46b1-8daa-57927bc7e4e4', 'created_at': '2024-02-05T06:00:00', 'updated_at': '2024-02-05T06:00:00'}
(hbnb) all
["[User] (96f1f017-5f7b-46b1-8daa-57927bc7e4e4) {'id': '96f1f017-5f7b-46b1-8daa-57927bc7e4e4', 'created_at': '2024-02-05T06:00:00', 'updated_at': '2024-02-05T06:00:00'}"]
(hbnb) update User 96f1f017-5f7b-46b1-8daa-57927bc7e4e4 first_name "John"
(hbnb) show User 96f1f017-5f7b-46b1-8daa-57927bc7e4e4
[User] (96f1f017-5f7b-46b1-8daa-57927bc7e4e4) {'id': '96f1f017-5f7b-46b1-8daa-57927bc7e4e4', 'created_at': '2024-02-05T06:00:00', 'updated_at': '2024-02-05T06:00:00', 'first_name': 'John'}
(hbnb) quit
$
```

## Authors

- Tolu Olabiyi

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.