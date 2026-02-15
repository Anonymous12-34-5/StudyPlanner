# CBSE Study Planner

A desktop application for Windows that generates personalized CBSE study timetables based on user inputs.

## Features

- **Smart Scheduling Algorithm**: Prioritizes difficult and weak chapters
- **Spaced Repetition**: Automatic revision sessions (1, 3, and 7 days after initial study)
- **Buffer Days**: Rest days every 7th day
- **Mock Tests**: Scheduled automatically when exam is within 30 days
- **Progress Tracking**: Mark tasks as completed and track overall progress
- **Save/Load**: Save study plans to JSON and load them later
- **Export**: Export timetables to TXT or CSV format

## Requirements

- Python 3.11 or higher
- Tkinter (included with Python on Windows)

## Installation

1. Clone or download this project
2. No additional packages required - Tkinter is built-in!

## How to Run

Simply run the main.py file:

```bash
python main.py
```

## Usage

### 1. Enter Basic Information
- Select your class (9/10/11/12)
- Enter exam date (DD/MM/YYYY format) OR days left until exam
- Set daily study hours for weekdays and weekends

### 2. Add Subjects and Chapters
- Click "Add Subject" to add each subject
- Enter subject name
- Select weakness level (Low/Medium/High)
- Enter chapters (one per line)
- Select default difficulty (Easy/Medium/Hard)

### 3. Generate Timetable
- Click "Generate Timetable" button
- View your personalized study schedule

### 4. Track Progress
- Click on checkboxes to mark tasks as completed
- Progress bar shows overall completion percentage

### 5. Save and Export
- **Save Plan**: Save to JSON for later use
- **Load Plan**: Load previously saved plan
- **Export TXT**: Export readable text file
- **Export CSV**: Export to spreadsheet format

## How the Algorithm Works

### Priority Calculation
Each chapter gets a priority score based on:
- **Difficulty**: Hard (3.0) > Medium (2.0) > Easy (1.0)
- **Weakness**: High (2.0) > Medium (1.5) > Low (1.0)
- **Time Factor**: Urgency increases as exam approaches

Priority = Difficulty × Weakness × Time Factor

### Time Allocation
- 60% for initial study
- 20% for practice (NCERT/PYQ/Exemplar)
- 20% for revision

### Scheduling Strategy
1. Chapters sorted by priority (highest first)
2. Study hours distributed based on subject priorities
3. Revision sessions added using spaced repetition (1, 3, 7 days)
4. Buffer days inserted every 7th day
5. Mock tests scheduled if exam is within 30 days

### Session Types
- **Study**: Initial learning of chapter
- **Practice**: NCERT exercises, PYQs, or Exemplar problems
- **Revision**: Spaced repetition review
- **Mock Test**: Full syllabus practice test
- **Buffer Day**: Rest and light review

## Building an Executable (EXE)



## Tips for Best Results

1. **Be Realistic**: Set achievable daily study hours
2. **Prioritize Correctly**: Mark weak subjects/chapters accurately
3. **Update Progress**: Regularly mark completed tasks
4. **Follow the Plan**: Stick to the generated schedule
5. **Use Revisions**: Don't skip revision sessions - they're crucial!
6. **Take Breaks**: Buffer days are important for rest

## Troubleshooting

### "Exam date cannot be in the past"
- Check your date format (DD/MM/YYYY)
- Ensure exam date is in the future

### "No chapters specified"
- Make sure to enter at least one chapter per subject
- Each chapter should be on a new line

### Window too small
- Resize the window or maximize it
- All sections are scrollable

## License

Free to use for educational purposes.

## Author

Built with ❤️ for CBSE students

