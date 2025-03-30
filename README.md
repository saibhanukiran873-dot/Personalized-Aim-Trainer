# Personalized Aim Trainer

Welcome to **Personalized Aim Trainer**—a fast-paced, interactive game designed to help improve your mouse control and reaction time. This project is a fun way to practice your aiming skills and can be run on any computer using Python and Pygame.

## Overview

The Aim Trainer game creates targets that grow and shrink on the screen. Your goal is to click on these targets as quickly and accurately as possible. The game tracks your performance by recording your hits, misses, and overall speed. Additionally, it provides real-time statistics like elapsed time, hit speed (targets per second), and remaining lives.

## Motivation

-  As an avid fan of combat games like Valorant, I wanted to sharpen my aiming skills to gain a competitive edge.
-  However, premium aim training platforms like AimLabs can cost more than $9 per month—making them less accessible for some gamers.
-  This inspired me to create a local aim training session that's both innovative and cost-effective.
-  With this project, I aimed to develop a tool that not only improves your aim but is also readily available to anyone without recurring fees.

## Key Features

- **Dynamic Target Behavior:**  
  Targets continuously grow and shrink, making each click a challenge!
  
- **Real-Time Performance Metrics:**  
  Displays time elapsed, hit speed, number of hits, and lives remaining.
  
- **Interactive Gameplay:**  
  The game updates live as you click on targets, providing immediate feedback on your accuracy.
  
- **End Game Summary:**  
  When you run out of lives, the game shows your final statistics including accuracy and overall performance.

## File Structure

The project includes two main Python files:
- **`main.py`:** Contains the full implementation of the aim trainer game.
- **`tutorial.py`:** A similar implementation meant to serve as a tutorial or learning aid. (Both files currently share similar logic.)

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Aim-Trainer.git
   cd Aim-Trainer
2. **Install Dependencies: This project uses Pygame. Install it via pip:**
   pip install pygame
   
3. Run the Game: To start the game, simply run:
   python main.py
   Alternatively, you can run tutorial.py to see a version of the game with additional comments or variations.

## Tech Stack :
-  Python: The core language for the game logic.

-  Pygame: Used for rendering graphics, handling events, and creating the interactive game environment.

-  Math & Time Modules: For calculating distances, handling game timing, and scoring.

## My Learnings :
-  In this project, I developed and fine-tuned the gameplay mechanics and performance tracking. I explored various algorithms to optimize responsiveness and user experience, ultimately choosing a lightweight approach that balances visual appeal and computational efficiency. My work involved:

-  Designing the dynamic behavior of targets.

-  Implementing real-time scoring and performance metrics.

-  Testing and optimizing game performance to ensure smooth gameplay on systems with lower specifications.

-  Creating clear and engaging documentation to help others understand and build upon this project.

## Future Enhancements :
-  Advanced Scoring System: Introducing leaderboards or difficulty levels.

-  Enhanced Visuals: Adding more animations, sound effects, and interactive tutorials.

-  User Customization: Allowing players to adjust game settings like target speed, size, and frequency.
