# Airbnb Clone Command Line Interface (CLI)

Welcome to our Airbnb clone! This is a web application that allows users to search for and book accommodations that are listed on the platform, as well as create their own listings to rent out. The goal of this project is to provide a user-friendly platform that closely emulates the features and functionality of the original Airbnb website, while also offering unique features and customizations. Whether you're a traveler looking for a place to stay or a host looking to list your property, our Airbnb clone has you covered.
This project is a command-line interface (CLI) for an Airbnb clone. The CLI allows users to interact with the Airbnb clone system through commands entered in the terminal. Users can perform various actions such as searching for listings, making reservations, and managing their account.

## Command Interpreter

The command interpreter is a Python-based CLI tool that provides a text-based interface for interacting with the Airbnb clone system. It parses user input, executes corresponding actions, and displays relevant information back to the user.

### How to Start It

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine:

    ```
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```
    cd airbnb_clone_cli
    ```

3. Run the command interpreter:

    ```
    python airbnb_cli.py
    ```

### How to Use It

Once the command interpreter is running, you can enter commands to perform various actions within the Airbnb clone system. The commands are structured in a user-friendly manner to facilitate easy interaction. Here are some basic commands:

- `search <location>`: Search for available listings in a specific location.
- `reserve <listing_id> <check-in_date> <check-out_date>`: Make a reservation for a listing with the specified ID and dates.
- `listings`: View all available listings.
- `my_reservations`: View your current reservations.
- `help`: Display a list of available commands and their usage.

### Examples

1. Search for listings in New York:

    ```
    > search New York
    ```

2. Reserve a listing with ID 123 for a stay from April 1st to April 5th:

    ```
    > reserve 123 2024-04-01 2024-04-05
    ```

3. View all available listings:

    ```
    > listings
    ```

4. View your current reservations:

    ```
    > my_reservations
    ```

These examples illustrate how to use the command interpreter to perform common tasks within the Airbnb clone system. Feel free to explore additional commands and functionalities provided by the CLI.