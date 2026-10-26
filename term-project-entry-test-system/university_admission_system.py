"""
University Admission & Entry Test Examination System
====================================================
Python implementation and simulation of the C++ CS-114 Term Project (Project_ict.cpp).
Implements candidate registration, 13-digit CNIC validation, automated roll number
assignment, multi-subject computer-based testing, scoring, merit ranking, and
department allocation.

Author: Muhammad Umer Basit (Civil Engineering Student)
Original C++ Project Presented: December 17, 2018 at NUST NICE
"""

import sys
import time
from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Candidate:
    id_num: str
    roll_no: int
    name: str
    cnic: str
    email: str
    password: str
    pref1: str
    pref2: str
    pref3: str
    score: int = 0
    percentage: float = 0.0
    allocated_dept: str = "Pending"
    test_taken: bool = False


class UniversityAdmissionSystem:
    DEPARTMENTS = [
        "Civil Engineering",
        "Electrical Engineering",
        "Mechanical Engineering",
        "Software Engineering",
        "Chemical Engineering"
    ]

    QUESTIONS = [
        {
            "q": "What is the derivative of sin(2x) with respect to x?",
            "options": ["A) cos(2x)", "B) 2cos(2x)", "C) -2cos(2x)", "D) 2sin(x)"],
            "ans": "B"
        },
        {
            "q": "Newton's Second Law of Motion is mathematically expressed as:",
            "options": ["A) F = mv", "B) F = m/a", "C) F = ma", "D) W = Fd"],
            "ans": "C"
        },
        {
            "q": "What is the pH value of pure distilled water at 25°C?",
            "options": ["A) 5", "B) 7", "C) 9", "D) 14"],
            "ans": "B"
        },
        {
            "q": "Which data structure operates on a Last-In, First-Out (LIFO) principle?",
            "options": ["A) Queue", "B) Stack", "C) Array", "D) Tree"],
            "ans": "B"
        },
        {
            "q": "In C++, which keyword is used to allocate memory dynamically?",
            "options": ["A) malloc", "B) alloc", "C) new", "D) create"],
            "ans": "C"
        }
    ]

    def __init__(self, capacity: int = 25):
        self.capacity = capacity
        self.candidates: Dict[int, Candidate] = {}
        self.current_id = 1
        self.current_roll = 11601

    def register_candidate(self, name: str, cnic: str, email: str, password: str,
                           pref1: str, pref2: str, pref3: str) -> Optional[Candidate]:
        if len(self.candidates) >= self.capacity:
            print("Registration capacity full!")
            return None
        if len(cnic.replace("-", "").strip()) != 13 or not cnic.replace("-", "").strip().isdigit():
            print("Invalid CNIC! Must be exactly 13 digits.")
            return None

        clean_cnic = cnic.replace("-", "").strip()
        cand_id = f"UG-19-{self.current_id}"
        roll = self.current_roll

        cand = Candidate(
            id_num=cand_id,
            roll_no=roll,
            name=name.strip(),
            cnic=clean_cnic,
            email=email.strip(),
            password=password,
            pref1=pref1,
            pref2=pref2,
            pref3=pref3
        )
        self.candidates[roll] = cand
        self.current_id += 1
        self.current_roll += 1
        return cand

    def authenticate(self, roll_no: int, password: str) -> Optional[Candidate]:
        cand = self.candidates.get(roll_no)
        if cand and cand.password == password:
            return cand
        return None

    def conduct_test(self, candidate: Candidate, answers: List[str]) -> float:
        if candidate.test_taken:
            return candidate.percentage

        score = 0
        total = len(self.QUESTIONS)
        for i, q in enumerate(self.QUESTIONS):
            user_ans = answers[i].strip().upper() if i < len(answers) else ""
            if user_ans == q["ans"]:
                score += 1

        candidate.score = score
        candidate.percentage = (score / total) * 100.0
        candidate.test_taken = True
        return candidate.percentage

    def compute_merit_and_allocations(self):
        """
        Calculates merit list and allocates department seats based on test percentage.
        Thresholds:
          - >= 80%: First preference
          - >= 60%: Second preference
          - >= 40%: Third preference
          - < 40%: Not Qualified
        """
        sorted_candidates = sorted(
            [c for c in self.candidates.values() if c.test_taken],
            key=lambda x: x.percentage,
            reverse=True
        )

        for cand in sorted_candidates:
            if cand.percentage >= 80.0:
                cand.allocated_dept = cand.pref1
            elif cand.percentage >= 60.0:
                cand.allocated_dept = cand.pref2
            elif cand.percentage >= 40.0:
                cand.allocated_dept = cand.pref3
            else:
                cand.allocated_dept = "Not Qualified (Below 40% Threshold)"

        return sorted_candidates

    def display_merit_list(self):
        merit_list = self.compute_merit_and_allocations()
        print("=" * 95)
        print(f"{'Rank':<6} {'Roll No':<10} {'Candidate Name':<22} {'Score':<8} {'Percentage':<12} {'Allocated Department':<28}")
        print("=" * 95)
        for rank, cand in enumerate(merit_list, 1):
            score_str = f"{cand.score}/{len(self.QUESTIONS)}"
            pct_str = f"{cand.percentage:.1f}%"
            print(f"{rank:<6} {cand.roll_no:<10} {cand.name[:20]:<22} {score_str:<8} {pct_str:<12} {cand.allocated_dept:<28}")
        print("=" * 95)


def run_demo():
    print("Initializing University Admission & Entry Test Simulation...")
    sys_app = UniversityAdmissionSystem()

    # Pre-populate sample candidates
    c1 = sys_app.register_candidate(
        name="Muhammad Umer Basit",
        cnic="3120212345671",
        email="umer.basit@example.com",
        password="securePass123",
        pref1="Civil Engineering",
        pref2="Software Engineering",
        pref3="Electrical Engineering"
    )
    c2 = sys_app.register_candidate(
        name="Hassan Mughal",
        cnic="3120212345672",
        email="hassan.mughal@example.com",
        password="pass456",
        pref1="Software Engineering",
        pref2="Civil Engineering",
        pref3="Mechanical Engineering"
    )
    c3 = sys_app.register_candidate(
        name="Haziq Ahmad",
        cnic="3120212345673",
        email="haziq.ahmad@example.com",
        password="pass789",
        pref1="Electrical Engineering",
        pref2="Civil Engineering",
        pref3="Mechanical Engineering"
    )

    # Conduct entry test
    sys_app.conduct_test(c1, ["B", "C", "B", "B", "C"])  # 5/5 = 100%
    sys_app.conduct_test(c2, ["B", "C", "A", "B", "C"])  # 4/5 = 80%
    sys_app.conduct_test(c3, ["B", "A", "B", "B", "D"])  # 3/5 = 60%

    print("\nSimulated Entry Test Results:")
    sys_app.display_merit_list()


if __name__ == "__main__":
    run_demo()
