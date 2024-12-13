# ToDo-s App 📅
<img align="left" src="https://github.com/debugfinder/Todo-s-App/blob/main/mytodo-images/My-Todo-s-Homepage.png?raw=true"/>

## Introduction
The ToDo-s App is a simple web application built using Python and the Flask framework. It allows users to organize and manage their tasks efficiently. It provides features to add, delete, mark as complete, and filter tasks. Tasks are stored in a MongoDB database.

## Objective of the ToDo-s App 🎯
The primary objective of the ToDo-s App is to offer users a simple and intuitive platform for managing their tasks effectively, thereby enhancing productivity.

---

## Features 🔗
1. **Add Todo**: Allows users to add new tasks to their todo list. 🖋️
2. **Complete Todo**: Users can mark tasks as completed. ✔️
3. **Delete Todo**: Users can delete individual tasks or clear their entire todo list. 🗑️
4. **Filter Todo**: Provides options to filter todos based on completion status and creation date. 🔍
5. **View Completed and Not Completed Todos**: Separate endpoints are available to view completed and not completed todos. 🔄
6. **API Access**: Offers an API endpoint to retrieve todos in JSON format. 🔢
7. **App Information**: Displays information about installed packages used in the application. 📘️
8. **Additional Information**: The app offers links to app information, documentation, API usage, and developer profiles. 🔗

---

## Installation 🛠️
1. Clone or download the ToDo App source code from the repository.
   ```bash
   git clone <repository_url>
   ```
2. Install the required Python packages listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```

---

## Usage 🌐
1. Access the ToDo App through a web browser by navigating to `http://localhost:5000`.
2. Use the provided interface to add, complete, and delete todos. 📝
3. Navigate to different endpoints (e.g., `/completed`, `/notcompleted`) to view specific sets of todos. 🔄
4. Filter todos by status and creation date using the filter option (`/filter/todo`). 🔍
5. Access the API endpoint at `/api/todos` to retrieve todos in JSON format. 🔢
6. Additional information about the app and the developer can be accessed through the provided links. 🔗

---

## Dependencies 📊
The ToDo App relies on the following dependencies:
1. **Flask**: A Python web framework used for building the web application. 📊
2. **PyMongo**: A MongoDB driver for Python used to interact with the database. 🏛
3. **Datetime**: A module in Python's standard library used for working with dates and times. ⏳
4. **bson.objectid**: Module providing ObjectId data type for MongoDB. 🔢
5. **pkg_resources**: Part of the setuptools package, used for querying information about installed packages. 📘️

---

## File Structure 🌐
1. **app.py**: Contains the Flask application code. 🔢
2. **index.html**: HTML template for rendering the user interface. 🔄
3. **static/**: Contains static files such as CSS stylesheets. 🌀
4. **templates/**: Contains HTML templates. 🛠️

---

## Testing Process 🎮
The testing process involves:
- **Unit Testing**: For individual functionalities. 🎯
- **Integration Testing**: For the entire application. 🛠️

Testing ensures the reliability and correctness of the application. 🚀

---

## Tools/Platforms 🛠️
1. Flask: Python web framework 🔧
2. MongoDB: NoSQL database for data storage 🏛
3. HTML/CSS: Frontend development 🌐
4. JavaScript: Scripting language for frontend interactions ⚛
5. Git: Version control system 📐

---

## Future Scope of the ToDo-s App 🌐
1. User authentication and authorization ⛓️
2. Task prioritization and categorization 🔘
3. Reminders and notifications 🕒
4. Collaboration features for shared task management 🛠️

---

## Limitations of the ToDo-s App ⚠️
1. Lack of user authentication 🔐
2. Basic filtering options 🔍
3. Limited customization features 🌀

---

## Bibliography 📖
1. [Flask Documentation](https://flask.palletsprojects.com/)
2. [MongoDB Documentation](https://www.mongodb.com/docs/)
3. [Python Documentation](https://docs.python.org/3/)

---

## Support 📢
For any issues or inquiries related to the ToDo App, please contact the developer at:

**Email**: debugfinder@gmail.com

---

## Related Links 🔗
- **[Introducing - My Sparta Coding Club Final Project Plan](https://debugfinder.medium.com/introducing-my-sparta-coding-club-final-project-plan-c14763b07fb6)**
- **[My Todo-s App: A Productivity Tool for Task Management](https://debugfinder.medium.com/my-todo-s-app-a-productivity-tool-for-task-management-2aa0bf6cadf3)**
- **[Demo Video: Curious to see the app in action? Watch our Demo Video.](https://youtu.be/H9i3nVAtEmg)**
- **[Project PPT: For an in-depth look, check out our Project PPT.](https://www.linkedin.com/posts/debugfinder_my-todo-s-app-sparta-coding-club-final-activity-7181275392735948800-NL7J?utm_source=share&utm_medium=member_android)**
