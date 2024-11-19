
# Epic_Events

## Overview

This project is a comprehensive CRM (Customer Relationship Management) platform designed to manage users, clients, contracts, and events efficiently. The system ensures that each collaborator has unique credentials to access the platform, with roles assigned based on their department.

### General Requirements
- Each collaborator must have their own credentials to use the platform.
- Each collaborator is associated with a specific role (based on their department).
- The platform must allow for the storage and updating of information regarding clients, contracts, and events.
- All collaborators should have read-only access to all clients, contracts, and events.

### Individual Requirements

#### Management Team
- Create, update, and delete users within the CRM system.
- Create and modify all contracts.
- Filter event displays, for example, to show all events that do not have an associated support representative.
- Modify events to associate a support representative with the event.

#### Commercial Team
- Create clients (clients will be automatically associated with them).
- Update clients for whom they are responsible.
- Modify/update contracts for clients they manage.
- Filter contract displays: show all contracts that are not yet signed or are not fully paid.
- Create an event for a client who has signed a contract.

#### Support Team
- Filter event displays: show only events assigned to them.
- Update events for which they are responsible.

## Features

- User management (create, update, delete users)
- Contract management (create, update, contracts)
- Event management (update , view events associated with clients)
- Role-based access control (commercial, support, management)
- Password hashing using Argon2 for secure user authentication
- Filtering contracts based on their status (unsigned, unpaid)

## Technologies Used

- Python
- SQLAlchemy
- Argon2 for password hashing
- SQLite (or any other database of your choice)
- FastAPI (or any other web framework if applicable)

### Database Management
- The project includes a robust database management system using SQLAlchemy to handle database interactions.
- The `database.py` file contains functions to create the database and tables, initialize the database, and reset it if necessary.
- The database connection details are managed through environment variables in the `config.py` file, ensuring secure handling of sensitive information such as database credentials.
- The `creation_admin.py` script allows for the creation of an initial admin user with predefined credentials, facilitating the setup of the system.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alinacharon/Epic_Events.git
   cd Epic_Events
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```bash
   python main.py
   ```

2. To create the admin user, run: 
   ```bash
   python creation_admin.py
   ```

3. Follow the on-screen instructions to navigate through the menus for managing users, contracts, and events.