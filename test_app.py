# -*- coding: utf-8 -*-
"""
Test script to verify CBSE Study Planner functionality
Run this to test the core algorithm without GUI
"""

import sys
import io
from datetime import date, timedelta
from planner.models import StudyPlan, Subject, Chapter
from planner.generator import TimetableGenerator
from planner.data_manager import DataManager

# Force UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def test_basic_generation():
    """Test basic timetable generation"""
    print("=" * 60)
    print("TEST 1: Basic Timetable Generation")
    print("=" * 60)
    
    # Create a study plan
    exam_date = date.today() + timedelta(days=30)
    
    plan = StudyPlan(
        student_class=10,
        exam_date=exam_date,
        weekday_hours=4.0,
        weekend_hours=8.0
    )
    
    # Add Mathematics
    math = Subject(name="Mathematics", weakness_level="High")
    math.chapters = [
        Chapter(name="Quadratic Equations", difficulty="Hard"),
        Chapter(name="Arithmetic Progression", difficulty="Medium"),
        Chapter(name="Triangles", difficulty="Medium"),
    ]
    plan.subjects.append(math)
    
    # Add Science
    science = Subject(name="Science", weakness_level="Medium")
    science.chapters = [
        Chapter(name="Chemical Reactions", difficulty="Medium"),
        Chapter(name="Electricity", difficulty="Hard"),
    ]
    plan.subjects.append(science)
    
    # Generate timetable
    try:
        generator = TimetableGenerator(plan)
        sessions = generator.generate()
        
        print(f"[OK] Generated {len(sessions)} sessions")
        print(f"[OK] Date range: {sessions[0].date} to {sessions[-1].date}")
        
        # Count session types
        study_count = sum(1 for s in sessions if s.task_type == 'Study')
        practice_count = sum(1 for s in sessions if 'Practice' in s.task_type)
        revision_count = sum(1 for s in sessions if 'Revision' in s.task_type)
        buffer_count = sum(1 for s in sessions if 'Buffer' in s.task_type)
        mock_count = sum(1 for s in sessions if 'Mock' in s.task_type)
        
        print(f"[OK] Study sessions: {study_count}")
        print(f"[OK] Practice sessions: {practice_count}")
        print(f"[OK] Revision sessions: {revision_count}")
        print(f"[OK] Buffer days: {buffer_count}")
        print(f"[OK] Mock tests: {mock_count}")
        
        # Show first few sessions
        print("\nFirst 5 sessions:")
        for i, session in enumerate(sessions[:5]):
            print(f"  {i+1}. {session.date} | {session.subject} | {session.chapter} | {session.task_type}")
        
        print("\n[PASS] TEST PASSED\n")
        return plan
        
    except Exception as e:
        print(f"\n[FAIL] TEST FAILED: {e}\n")
        raise


def test_save_load(plan):
    """Test save and load functionality"""
    print("=" * 60)
    print("TEST 2: Save and Load Functionality")
    print("=" * 60)
    
    try:
        manager = DataManager()
        
        # Save plan
        filepath = manager.save_plan(plan, "test_plan.json")
        print(f"[OK] Saved plan to: {filepath}")
        
        # Load plan
        loaded_plan = manager.load_plan(filepath)
        print(f"[OK] Loaded plan successfully")
        print(f"[OK] Class: {loaded_plan.student_class}")
        print(f"[OK] Subjects: {len(loaded_plan.subjects)}")
        print(f"[OK] Sessions: {len(loaded_plan.sessions)}")
        
        print("\n[PASS] TEST PASSED\n")
        return loaded_plan
        
    except Exception as e:
        print(f"\n[FAIL] TEST FAILED: {e}\n")
        raise


def test_export(plan):
    """Test export functionality"""
    print("=" * 60)
    print("TEST 3: Export Functionality")
    print("=" * 60)
    
    try:
        manager = DataManager()
        
        # Export to TXT
        txt_path = "data/test_export.txt"
        manager.export_to_txt(plan, txt_path)
        print(f"[OK] Exported to TXT: {txt_path}")
        
        # Export to CSV
        csv_path = "data/test_export.csv"
        manager.export_to_csv(plan, csv_path)
        print(f"[OK] Exported to CSV: {csv_path}")
        
        print("\n[PASS] TEST PASSED\n")
        
    except Exception as e:
        print(f"\n[FAIL] TEST FAILED: {e}\n")
        raise


def test_priority_calculation():
    """Test priority calculation"""
    print("=" * 60)
    print("TEST 4: Priority Calculation")
    print("=" * 60)
    
    try:
        chapter1 = Chapter(name="Easy Chapter", difficulty="Easy")
        chapter2 = Chapter(name="Hard Chapter", difficulty="Hard")
        
        # Calculate priorities
        priority1 = chapter1.calculate_priority("Low", 30)
        priority2 = chapter2.calculate_priority("High", 30)
        
        print(f"[OK] Easy chapter (Low weakness): {priority1:.2f}")
        print(f"[OK] Hard chapter (High weakness): {priority2:.2f}")
        
        assert priority2 > priority1, "Hard chapter should have higher priority"
        print("[OK] Priority ordering correct")
        
        print("\n[PASS] TEST PASSED\n")
        
    except Exception as e:
        print(f"\n[FAIL] TEST FAILED: {e}\n")
        raise


def test_progress_tracking():
    """Test progress tracking"""
    print("=" * 60)
    print("TEST 5: Progress Tracking")
    print("=" * 60)
    
    try:
        exam_date = date.today() + timedelta(days=15)
        
        plan = StudyPlan(
            student_class=12,
            exam_date=exam_date,
            weekday_hours=3.0,
            weekend_hours=6.0
        )
        
        # Add one subject
        subject = Subject(name="English", weakness_level="Low")
        subject.chapters = [
            Chapter(name="Chapter 1", difficulty="Easy"),
            Chapter(name="Chapter 2", difficulty="Easy"),
        ]
        plan.subjects.append(subject)
        
        # Generate
        generator = TimetableGenerator(plan)
        sessions = generator.generate()
        
        # Initial progress
        progress1 = plan.get_progress_percentage()
        print(f"[OK] Initial progress: {progress1:.1f}%")
        assert progress1 == 0.0, "Initial progress should be 0%"
        
        # Mark half complete
        for i in range(len(sessions) // 2):
            sessions[i].completed = True
        
        progress2 = plan.get_progress_percentage()
        print(f"[OK] After marking half complete: {progress2:.1f}%")
        assert 40 < progress2 < 60, "Progress should be around 50%"
        
        # Mark all complete
        for session in sessions:
            session.completed = True
        
        progress3 = plan.get_progress_percentage()
        print(f"[OK] After marking all complete: {progress3:.1f}%")
        assert progress3 == 100.0, "Final progress should be 100%"
        
        print("\n[PASS] TEST PASSED\n")
        
    except Exception as e:
        print(f"\n[FAIL] TEST FAILED: {e}\n")
        raise


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("CBSE STUDY PLANNER - AUTOMATED TESTS")
    print("=" * 60 + "\n")
    
    try:
        # Run tests
        plan = test_basic_generation()
        loaded_plan = test_save_load(plan)
        test_export(loaded_plan)
        test_priority_calculation()
        test_progress_tracking()
        
        print("=" * 60)
        print("SUCCESS: ALL TESTS PASSED!")
        print("=" * 60)
        print("\nThe application is working correctly.")
        print("You can now run: py main.py")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print("\n" + "=" * 60)
        print("ERROR: TESTS FAILED")
        print("=" * 60)
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
