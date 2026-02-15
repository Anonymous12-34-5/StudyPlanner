"""
CBSE Study Planner - Main Entry Point
A desktop application for generating personalized CBSE study timetables
"""

import tkinter as tk
from ui.app import StudyPlannerApp

def main():
    """Main entry point for the application"""
    root = tk.Tk()
    app = StudyPlannerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
