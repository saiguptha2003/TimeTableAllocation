# Timetable Scheduler

Timetable Scheduler is a Flask web application for generating class schedules based on specified parameters such as classes, sections, and available time slots.

## Features

- Generates class schedules for different sections based on specified parameters.
- Ensures that classes are scheduled without conflicts and optimally utilizes available classrooms.

## Setup

To set up the Timetable Scheduler locally, follow these steps:

1. Clone the repository:

    ```bash
    
            https://github.com/saiguptha2003/TimeTableAllocation.git

    ```

2. Navigate to the project directory:

    ```bash
    cd TimeTableAllocation
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python main.py
    ```

5. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Usage

1. Enter the desired number of classes, sections, and time slots on the homepage.
2. Click on the "Generate Schedule" button.
3. View the generated class schedule, which will display class sections along with their respective timings and classrooms.

## Sample Code Explanation

- `app.py`: Contains the Flask web application code, including routes for handling user requests and rendering HTML templates.
- `utility.py`: Implements the scheduling algorithm to generate class schedules based on specified parameters.
- `templates/index.html`: HTML template for the homepage, where users can input parameters.
- `templates/createtable.html`: HTML template for displaying the generated class schedule.

## Contributing

Contributions to the Timetable Scheduler are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
