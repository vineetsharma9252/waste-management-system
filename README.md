# waste-management-system

Here’s the updated README file content based on your requirements, including the use of the `start_server.py` file:

---

# Waste Management System

## Description
The **Waste Management System** is a web-based platform designed to streamline waste segregation, disposal, and sanitation efforts. It helps users manage waste effectively, track collection schedules, and visualize waste data through interactive dashboards. The platform is built to address the challenges faced in waste management, especially in urban areas in India.

## Features
- **User Registration & Login**: Secure user authentication system.
- **Waste Data Visualization**: Visualize waste management data trends and insights.
- **Waste Collection Scheduling**: Users can track and manage their waste collection dates.
- **FAQ Section**: Interactive and animated FAQs.
- **Customer Information Management**: Manage customer details for waste collection services.

## Technologies Used
- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Django Framework
- **Database**: MySQL
- **Visualization**: Streamlit for data visualization dashboards

## Installation

### Prerequisites
- Python 3.x
- MySQL
- Pip

### Steps to run locally:
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/waste-management.git
    ```
2. Navigate to the project directory:
    ```bash
    cd waste-management
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Use the `start_servers.py` script to run both the Django website and the Streamlit app:
    ```bash
    python start_servers.py
    ```
   This script will:
   - Launch the Django server and open the website at `http://127.0.0.1:8000/`.
   - Start the Streamlit server in the background without opening the Streamlit interface in the browser.

## Usage
- **Website**: Users can register, log in, and manage waste disposal and collection schedules. Admins can manage customer details and monitor waste data.
- **Streamlit Dashboard**: Provides interactive visualizations of waste trends and data insights. It runs in the background to support visualizations on the website.

## Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or suggestions, feel free to reach out via:
- Email: Mastergenos228@gmail.com
- GitHub: https://github.com/vineet9252)

---

# This README reflects your requirement for running both the Django and Streamlit servers through the `start_servers.py` file. 
