"""
Visual Generation Script for Programming Fundamentals Portfolio
===============================================================
Generates high-resolution diagrams:
  1. Entry Test System Architecture Flowchart
  2. C++ Programming Fundamentals Curriculum Roadmap
  3. Python Plagiarism Detector Architecture
  4. Lab Task Execution Composite Grid

Author: Muhammad Umer Basit (Civil Engineering Student)
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media_dir = os.path.join(repo_root, "media")
os.makedirs(media_dir, exist_ok=True)


def generate_entry_test_flowchart():
    print("Generating Entry Test System Flowchart...")
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)

    # Box styles
    box_blue = dict(boxstyle="round,pad=0.5", facecolor="#e3f2fd", edgecolor="#1565c0", lw=2)
    box_green = dict(boxstyle="round,pad=0.5", facecolor="#e8f5e9", edgecolor="#2e7d32", lw=2)
    box_orange = dict(boxstyle="round,pad=0.5", facecolor="#fff3e0", edgecolor="#e65100", lw=2)
    box_purple = dict(boxstyle="round,pad=0.5", facecolor="#f3e5f5", edgecolor="#7b1fa2", lw=2)
    box_red = dict(boxstyle="round,pad=0.5", facecolor="#ffebee", edgecolor="#c62828", lw=2)

    # Title
    ax.text(7, 7.5, "University Admission & Entry Test System (CS-114 Capstone Project)", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#0d47a1')

    # Nodes
    ax.text(2, 6.0, "1. Candidate Registration\n• ID: UG-19-[n]\n• Roll: 11601 to 11625\n• 13-Digit CNIC Verification\n• Dept Preferences (1, 2, 3)", 
            ha='center', va='center', bbox=box_blue, fontsize=9.5)

    ax.text(6, 6.0, "2. Authentication\n• Roll No Verification\n• Password Hash Match\n• Session Initialization\n• Test Eligibility Gate", 
            ha='center', va='center', bbox=box_green, fontsize=9.5)

    ax.text(10, 6.0, "3. Computer-Based Exam\n• Timed Multi-Choice\n• Math, Physics, English\n• Real-Time Answer Capture\n• Anti-Skipping Validation", 
            ha='center', va='center', bbox=box_orange, fontsize=9.5)

    ax.text(10, 3.2, "4. Automated Evaluation\n• Instant Score Tallying\n• Percentage Calculation\n• Threshold Check (>=40%)\n• Database Record Update", 
            ha='center', va='center', bbox=box_purple, fontsize=9.5)

    ax.text(6, 3.2, "5. Merit List & Allocation\n• Percentage Sorting\n• Preference Priority Matching\n• Cutoff Threshold Gate\n• Dept Seat Allotment", 
            ha='center', va='center', bbox=box_red, fontsize=9.5)

    ax.text(2, 3.2, "6. Public Reporting\n• Consolidated Merit List\n• Individual Roll No Lookup\n• Department Quota Status\n• Admission Call Letters", 
            ha='center', va='center', bbox=box_blue, fontsize=9.5)

    # Arrows
    arrow_props = dict(arrowstyle="->", lw=2, color="#37474f")
    ax.annotate("", xy=(3.8, 6.0), xytext=(4.2, 6.0), arrowprops=arrow_props)
    ax.annotate("", xy=(7.8, 6.0), xytext=(8.2, 6.0), arrowprops=arrow_props)
    ax.annotate("", xy=(10, 4.8), xytext=(10, 4.4), arrowprops=arrow_props)
    ax.annotate("", xy=(8.2, 3.2), xytext=(7.8, 3.2), arrowprops=arrow_props)
    ax.annotate("", xy=(4.2, 3.2), xytext=(3.8, 3.2), arrowprops=arrow_props)

    # Footer note
    ax.text(7, 1.2, "Developed in C++ (1,009 Lines) with Windows Console Animations (Sleep, system cls) & Modular Functions\nAuthored by Muhammad Umer Basit (Civil Engineering Student) | NUST NICE",
            ha='center', va='center', fontsize=9.5, style='italic', color='#455a64')

    plt.tight_layout()
    plt.savefig(os.path.join(media_dir, "entry_test_workflow.png"), dpi=300)
    plt.close()
    print("Entry Test flowchart generated.")


def generate_curriculum_roadmap():
    print("Generating C++ Curriculum Roadmap...")
    fig, ax = plt.subplots(figsize=(15, 7), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 7)

    ax.text(7.5, 6.5, "CS-114 Fundamentals of Programming (C++ Curriculum Taxonomy)", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#1b5e20')

    stages = [
        ("Phase 1: Foundations", "• Dev-C++ IDE Setup\n• Variables & Data Types\n• Stream I/O (cin/cout)\n• Escape Sequences", "#e8f5e9", "#2e7d32", 1.8),
        ("Phase 2: Operators", "• Arithmetic (+, -, *, /)\n• Relational (==, !=, <)\n• Logical (&&, ||, !)\n• Operator Precedence", "#e0f2fe", "#0284c7", 4.6),
        ("Phase 3: Control Flow", "• if / else if / else\n• Nested Conditionals\n• switch-case logic\n• Decision Trees", "#fef3c7", "#d97706", 7.4),
        ("Phase 4: Loops & Iteration", "• for / while / do-while\n• Nested Loops\n• Star Pattern Printing\n• break & continue", "#fce7f3", "#db2777", 10.2),
        ("Phase 5: Functions & Scope", "• Prototypes & Calls\n• Pass-by-Value/Ref\n• Local vs Global Scope\n• Recursion", "#f3e8ff", "#7e22ce", 13.0)
    ]

    for title, desc, bg, border, x_pos in stages:
        box = dict(boxstyle="round,pad=0.5", facecolor=bg, edgecolor=border, lw=2)
        ax.text(x_pos, 4.0, f"{title}\n\n{desc}", ha='center', va='center', bbox=box, fontsize=9.5)

    arrow_props = dict(arrowstyle="->", lw=2.5, color="#1e293b")
    for x_arr in [3.2, 6.0, 8.8, 11.6]:
        ax.annotate("", xy=(x_arr + 0.3, 4.0), xytext=(x_arr - 0.3, 4.0), arrowprops=arrow_props)

    # Advanced tier
    adv_box = dict(boxstyle="round,pad=0.6", facecolor="#f8fafc", edgecolor="#475569", lw=2)
    ax.text(7.5, 1.8, "Capstone Integration Tier:\n1D & 2D Arrays • Struct Data Collections • Dynamic Search & Sorting • Interactive Console Systems\nApplied in 1,009-line University Entry Test System & Tkinter Plagiarism Checker", 
            ha='center', va='center', bbox=adv_box, fontsize=10, fontweight='bold', color='#1e293b')

    plt.tight_layout()
    plt.savefig(os.path.join(media_dir, "cpp_programming_curriculum_roadmap.png"), dpi=300)
    plt.close()
    print("Curriculum roadmap generated.")


def generate_plagiarism_architecture():
    print("Generating Plagiarism Checker Architecture...")
    fig, ax = plt.subplots(figsize=(13, 7), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 7)

    ax.text(6.5, 6.4, "Python Tkinter Plagiarism Checker Architecture", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#7c2d12')

    box_style1 = dict(boxstyle="round,pad=0.5", facecolor="#ffedd5", edgecolor="#ea580c", lw=2)
    box_style2 = dict(boxstyle="round,pad=0.5", facecolor="#fef9c3", edgecolor="#ca8a04", lw=2)
    box_style3 = dict(boxstyle="round,pad=0.5", facecolor="#fee2e2", edgecolor="#dc2626", lw=2)
    box_style4 = dict(boxstyle="round,pad=0.5", facecolor="#dbeafe", edgecolor="#2563eb", lw=2)

    ax.text(2.2, 4.2, "Input Documents\n• Database Corpus\n• Search Query Text\n• File I/O Loader", ha='center', va='center', bbox=box_style1, fontsize=10)
    ax.text(6.5, 4.2, "Text Preprocessing & NLP\n• Regex Cleaning\n• Punctuation Stripping\n• Word Tokenization\n• n-Gram Frequency Matching", ha='center', va='center', bbox=box_style2, fontsize=10)
    ax.text(10.8, 4.2, "Similarity Engine\n• Overlap Ratio (%)\n• Plagiarism Score\n• Color-Coded Verdict", ha='center', va='center', bbox=box_style3, fontsize=10)

    ax.text(6.5, 1.8, "Multi-Tier Audio Alerts (winsound):\n• Safe Level (<25%): safe_level.wav\n• Moderate Risk (25-50%): risky_level.wav\n• High Plagiarism (50-75%): hard_level.wav\n• Critical Match (>75%): full_level.wav", ha='center', va='center', bbox=box_style4, fontsize=9.5)

    arrow_props = dict(arrowstyle="->", lw=2, color="#334155")
    ax.annotate("", xy=(4.2, 4.2), xytext=(3.4, 4.2), arrowprops=arrow_props)
    ax.annotate("", xy=(8.7, 4.2), xytext=(8.0, 4.2), arrowprops=arrow_props)
    ax.annotate("", xy=(6.5, 2.9), xytext=(6.5, 3.4), arrowprops=arrow_props)

    plt.tight_layout()
    plt.savefig(os.path.join(media_dir, "plagiarism_checker_architecture.png"), dpi=300)
    plt.close()
    print("Plagiarism architecture generated.")


def generate_composite_lab_grid():
    print("Generating Composite Lab Grid...")
    # Grab 4 sample screenshots from lab 5, lab 8, lab 9, lab 10
    sc_paths = [
        os.path.join(repo_root, "lab-tasks-and-exercises", "lab-05-devcpp-basics", "screenshots", "image1.PNG"),
        os.path.join(repo_root, "lab-tasks-and-exercises", "lab-08-control-structures", "screenshots", "image1.PNG"),
        os.path.join(repo_root, "lab-tasks-and-exercises", "lab-09-functions-part-1", "screenshots", "Task 01.PNG"),
        os.path.join(repo_root, "lab-tasks-and-exercises", "lab-10-functions-part-2", "screenshots", "Task 01.JPG")
    ]

    valid_imgs = [p for p in sc_paths if os.path.exists(p)]
    if len(valid_imgs) >= 4:
        fig, axes = plt.subplots(2, 2, figsize=(12, 8), dpi=250)
        titles = [
            "Lab 05: Dev-C++ Basic Operators & Streams",
            "Lab 08: Nested Control Statements & Loops",
            "Lab 09: User-Defined Functions & Parameters",
            "Lab 10: Scope Resolution & Variable Lifetime"
        ]
        for idx, ax in enumerate(axes.flat):
            img = Image.open(valid_imgs[idx])
            ax.imshow(img)
            ax.set_title(titles[idx], fontsize=11, fontweight='bold', pad=8)
            ax.axis('off')

        plt.suptitle("Laboratory Practical Exercises: Dev-C++ Source Code & Console Execution Outputs", 
                     fontsize=13, fontweight='bold', y=0.98)
        plt.tight_layout()
        plt.savefig(os.path.join(media_dir, "lab_execution_grid.png"), dpi=250)
        plt.close()
        print("Composite lab grid generated.")


if __name__ == "__main__":
    generate_entry_test_flowchart()
    generate_curriculum_roadmap()
    generate_plagiarism_architecture()
    generate_composite_lab_grid()
    print("All media visuals generated successfully.")
