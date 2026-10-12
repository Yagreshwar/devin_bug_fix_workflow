# Order Service — Devin Bug-to-PR POC

A small Python order-processing service designed to demonstrate Devin's ability to investigate a bug, identify its root cause, implement a fix, run regression tests, and open a GitHub pull request.

## Features

- Order subtotal calculation
- Percentage-based discounts
- Tax calculation
- Final order total calculation
- Automated tests using pytest

## Setup

Create a virtual environment:

    python3 -m venv devin_poc_env

Activate the virtual environment:

    source devin_poc_env/bin/activate

Install the test dependency:

    python -m pip install pytest

## Run Tests

Run the automated test suite using pytest:

    python -m pytest -v

## POC Objective

Introduce an intentional defect in the percentage-discount calculation, push the code to GitHub, and ask Devin to investigate the issue, reproduce the bug, identify the root cause, implement a fix, add regression tests, and submit a GitHub pull request for human review.

## Expected Workflow

1. Investigate the reported issue.
2. Reproduce the percentage-discount bug.
3. Identify the root cause.
4. Implement the fix.
5. Add regression tests to prevent the bug from recurring.
6. Run the test suite to verify the fix.
7. Submit a GitHub pull request for human review.

## Expected Outcome

Demonstrate an end-to-end bug-fixing workflow in which Devin identifies and fixes the percentage-discount defect, validates the solution using automated tests, and submits a pull request for human review.