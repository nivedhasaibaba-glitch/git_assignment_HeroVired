# 🧮 CalculatorPlus - Git Assignment (Hero Vired)

## 📌 Overview
This repository (`git_assignment_HeroVired`) contains solutions for the Git assignment.  
The project demonstrates:
- Git branching, merging, and release management
- Collaboration and code review
- Feature implementation in Python
- Git LFS integration for large files
- Use of Git stash for managing multiple features

---

## 🚀 Assignment Workflow

### Q1: CalculatorPlus Application
**Task:** Extend a Python calculator with a square root feature and fix a bug in division.

#### Steps Performed:
1. **Repository Creation**
   - Created repository: `git_assignment_HeroVired` (private).
   - Added collaborators (classmates).

2. **Branching**
   - Created `dev` branch.
   - Added initial calculator code.

3. **Feature Implementation**
   - Implemented `square_root()` function in `feature/sqrt` branch.
   - Fixed division bug in `dev` branch:
     ```python
     def divide(self, a, b):
         if b == 0:
             raise ValueError("Cannot divide by zero.")
         return a / b
     ```

4. **Merging & Releases**
   - Merged `feature/sqrt` → `dev`.
   - Tested in `dev` branch.
   - Merged `dev` → `main`.
   - Created **Version 1 release** (basic calculator).
   - Created **Version 2 release** (with square root + bug fix).

5. **Collaboration**
   - Requested code review from a classmate.
   - Incorporated feedback before merging.

---

### Q2: Git LFS Integration
**Task:** Handle large binary files (>200 MB).

#### Steps Performed:
1. Installed Git LFS:
   ```bash
   git lfs install
Created branch lfs.

Tracked large files:

bash
git lfs track "*.zip"
Added and pushed a file >200 MB.

Verified by cloning repository on another machine:

Large file downloaded correctly via Git LFS.

Q3: Geometry Calculator with Git Stash
Task: Implement circle and rectangle area features using Git stash.

Steps Performed:
Created branch geometry-calculator.

Created sub-branches:

feature/circle-area

feature/rectangle-area

Used Git stash:

Stashed incomplete circle area code.

Switched to rectangle branch.

Stashed incomplete rectangle code.

Retrieved stashes when resuming work.

Completed implementations:

python
def calculate_circle_area(self, radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(self, length, width):
    return length * width
Committed & pushed both features.

Created pull requests → dev branch.

Requested review, merged after approval.

Final merge into main.

Repository Structure:
git_assignment_HeroVired/
│── calculator.py
│── geometry_calculator.py
│── large_file.zip (tracked via Git LFS)
│── README.md
