# **Better Ships that Battle Better**

![Hit ship](assets/images/battleship-hit.webp)

A Django-powered pirate-themed naval battleship game featuring user authentication, battle statistics, and immersive pirate captain gameplay.

## **Live Deployment**

- **[Play the Game](https://better-ships-battle-better.herokuapp.com/)** - Main deployment on Heroku
- **[Alternative Link](https://pirate-queens-sea-battles-a92eba2c9a74.herokuapp.com/)** - Secondary deployment
- **[GitHub Repository](https://github.com/SamOBrienOlinger/Better-Ships-that-Battle-Better)** - View the source code

## **Summary**

This interactive web-based battleship game transforms the classic naval warfare experience into an immersive pirate adventure. Players create pirate captain profiles, engage in tactical 8x8 grid battles against computer opponents, and track their naval conquest statistics. Built with Django and deployed on Heroku, the game features a complete user authentication system, historical battle tracking, and a beautiful pirate-themed interface.

## **[Contents](#contents)**

1. **[How to Play](#how-to-play)**
2. **[Features](#features)**
3. **[Technology Stack](#technology-stack)**
4. **[Game Mechanics](#game-mechanics)**
5. **[User System](#user-system)**
6. **[Deployment](#deployment)**
7. **[Installation](#installation)**
8. **[Credits](#credits)**
9. **[Acknowledgements](#acknowledgements)**

## **[How to Play](#how-to-play)**

### Getting Started
1. **Visit the Game**: Navigate to the [live deployment](https://better-ships-battle-better.herokuapp.com/)
2. **Choose Your Path**: 
   - **Guest Play**: Jump straight into battle without registration
   - **Create Account**: Register for full pirate captain experience with statistics tracking

### Pirate Captain Setup (Registered Users)
1. **Create Your Profile**: Choose your pirate captain name and write your naval biography
2. **Select Your Avatar**: Pick from historical Pirate Queen avatars
3. **Set Difficulty**: Choose your challenge level:
   - **Easy**: 20 cannonballs
   - **Normal**: 15 cannonballs  
   - **Hard**: 10 cannonballs

### Naval Combat
1. **Battle Grid**: Face an 8x8 tactical grid with 5 hidden enemy ships
2. **Fleet Composition**: Hunt down the enemy fleet:
   - Carrier (5 spaces)
   - Battleship (4 spaces)
   - Cruiser (3 spaces)
   - Submarine (3 spaces)
   - Destroyer (2 spaces)
3. **Fire Cannonballs**: Click grid coordinates to launch attacks
4. **Track Results**: 
   - 💥 Direct hits on enemy ships
   - 🌊 Misses in open water
   - 🚢 Sunken ships
5. **Victory Conditions**: Sink all enemy ships before running out of ammunition

## **[Features](#features)**

### 🏴‍☠️ **Pirate-Themed Naval Combat**
- Interactive 8x8 battleship grid with tactical gameplay
- 5 strategically placed ships with realistic naval vessel sizes
- Real-time battle feedback with naval emojis and animations
- Strategic ammunition management system based on difficulty

### 👤 **Complete User Authentication System**
- User registration with automatic pirate profile creation
- Secure login/logout with Django session management
- Guest play option for immediate access
- Protected routes for authenticated features

### 🏴‍☠️ **Pirate Captain Profile System**
- Custom pirate captain names and biographical stories
- Historical Pirate Queen avatar selection system
- Difficulty preference settings with ammunition scaling
- Profile editing and management interface

### 📊 **Battle Statistics & History Tracking**
- Comprehensive battle history with timestamps
- Win/loss statistics and win rate calculations
- Average shots fired and total ships sunk metrics
- Game duration recording and performance analytics
- AJAX-powered real-time game result saving

### 🎯 **Dashboard & Analytics**
- Personal captain dashboard with recent battles
- Detailed game history viewing system
- Performance analytics and achievement tracking
- Quick access to profile management tools

### 🎨 **Modern Naval-Themed Interface**
- Immersive pirate/naval aesthetic with authentic color schemes
- Responsive grid-based layouts for all devices
- Interactive hover effects and smooth animations
- Hero images featuring pirate ships and naval warfare
- Professional game instructions and feature descriptions

## **[Technology Stack](#technology-stack)**

### **Backend**
- **Django 4.2.9**: Web framework with MVC architecture
- **Python 3.11**: Core programming language
- **Gunicorn**: WSGI HTTP Server for production
- **WhiteNoise**: Static file serving middleware

### **Database & Models**
- **SQLite**: Development database
- **PostgreSQL**: Production database (Heroku)
- **Custom Models**: PirateQueen, UserProfile, Game tracking

### **Frontend**
- **HTML5**: Semantic markup structure
- **CSS3**: Naval-themed styling and responsive design
- **JavaScript**: Interactive gameplay and AJAX functionality
- **Bootstrap**: Responsive grid system and components

### **Deployment & DevOps**
- **Heroku**: Cloud platform deployment
- **Git**: Version control system
- **GitHub**: Repository hosting and collaboration
- **Environment Variables**: Secure configuration management

## **[Game Mechanics](#game-mechanics)**

### **Ship Placement Algorithm**
- Randomized ship positioning using Python's `randint()` method
- Collision detection prevents ship overlap
- Strategic placement ensures balanced gameplay difficulty

### **Battle System**
- Click-based coordinate targeting system
- Real-time hit/miss validation and feedback
- Ammunition tracking with difficulty-based limits
- Victory/defeat condition checking

### **Scoring System**
- Battle completion tracking with timestamps
- Shot accuracy calculations and statistics
- Win rate percentages and performance metrics
- Historical battle data persistence

## **[User System](#user-system)**

### **Authentication Flow**
- Django's built-in authentication system
- Automatic profile creation upon registration
- Session-based login state management
- Secure password handling and validation

### **Profile Management**
- Pirate captain customization interface
- Avatar selection from historical figures
- Biographical information and preferences
- Game difficulty and display settings

## **[Deployment](#deployment)**

### **Live Production Environment**
The game is deployed on Heroku with the following configuration:

**Primary Deployment**: https://better-ships-battle-better.herokuapp.com/
**Secondary Deployment**: https://pirate-queens-sea-battles-a92eba2c9a74.herokuapp.com/

### **Deployment Process**
1. **Heroku Setup**: Create new Heroku application
2. **Environment Configuration**: Set production environment variables
3. **Database Migration**: Configure PostgreSQL database
4. **Static Files**: WhiteNoise middleware for static file serving
5. **Process Configuration**: Gunicorn WSGI server setup

### **Key Configuration Files**
- `Procfile`: Heroku process configuration
- `requirements.txt`: Python dependencies
- `settings.py`: Django production settings
- `.python-version`: Python version specification

## **[Installation](#installation)**

### **Local Development Setup**

1. **Clone Repository**
   ```bash
   git clone https://github.com/SamOBrienOlinger/Better-Ships-that-Battle-Better.git
   cd Better-Ships-that-Battle-Better
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser** (Optional)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver 8080
   ```

7. **Access Game**: Navigate to `http://localhost:8080`

### **Environment Variables**
Create a `.env` file in the project root:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
```

## **[Credits](#credits)**

### **Development Resources**
- **[Code Institute LMS](https://learn.codeinstitute.net/)**: Portfolio project guidance and Django tutorials
- **[Django Documentation](https://docs.djangoproject.com/)**: Framework reference and best practices
- **[W3Schools](https://www.w3schools.com/)**: HTML, CSS, and JavaScript tutorials
- **[Stack Overflow](https://stackoverflow.com/)**: Community support and problem-solving
- **[MDN Web Docs](https://developer.mozilla.org/)**: Web development standards and references
- **[Geeks for Geeks](https://www.geeksforgeeks.org/)**: Python programming tutorials

### **Original Battleship Logic**
Core game board logic adapted from [Garrett Broughton's Battleship](https://github.com/gbrough/battleship):

```python
def get_letters_to_numbers():
    letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    return letters_to_numbers

def print_board(self):
    print("  1 2 3 4 5 6 7 8")
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in self.board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
```

### **Historical References**
- Pirate Queen avatars based on historical female pirates
- Naval terminology and theming from maritime history
- Ship classifications from real naval vessel types

## **[Acknowledgements](#acknowledgements)**

### **Educational Support**
- **YouTube Tutorials**: Various Python game development and Django deployment guides
- **[Sandeep Aggarwal](https://code-institute-room.slack.com/archives/D02TFLJRZTR)**: Mentor guidance and project feedback
- **Code Institute Community**: Tutors and students providing support via Slack

### **Technical Contributors**
- **[jo_ci](https://github.com/wings30306)**: Django authentication guidance
- **[AlexaHendry_5P](https://code-institute-room.slack.com/team/U02FQKWTXGT)**: Frontend design feedback
- **[oisin_ci](https://code-institute-room.slack.com/archives/D03NCBKR8BB)**: Deployment troubleshooting
- **[gemma_ci](https://code-institute-room.slack.com/archives/D03MT4GMGG6)**: Database modeling assistance
- **[alexandru_ci](https://code-institute-room.slack.com/archives/D03MK4WD9NK)**: Heroku deployment support

### **Special Recognition**
- **Windsurf AI**: Advanced development assistance and code optimization
- **Heroku Platform**: Reliable cloud deployment infrastructure
- **Django Community**: Excellent framework documentation and community support

---

**[⬆️ Back to Top](#better-ships-that-battle-better)** | **[🎮 Play Now](https://better-ships-battle-better.herokuapp.com/)** | **[📁 View Code](https://github.com/SamOBrienOlinger/Better-Ships-that-Battle-Better)**