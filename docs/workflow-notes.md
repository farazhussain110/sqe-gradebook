# Workflow Notes

## Change Workflow

A change in the SQE Gradebook project follows this workflow:

```text
Idea
  ↓
Issue
  ↓
Branch
  ↓
Pull Request (PR)
  ↓
Review
  ↓
Merge
  ↓
CI
  ↓
Release
```

## QA Engineer Intervention

### 1. Idea

The team identifies a new feature, improvement, or possible problem.

**QA Intervention:** QA considers testability, quality risks, and acceptance criteria for the proposed change.

### 2. Issue

The idea is documented as a GitHub Issue with clear requirements and expected behavior.

**QA Intervention:** QA reviews the issue to make sure the requirements are clear, complete, and testable.

### 3. Branch

A separate branch is created to implement the change.

**QA Intervention:** QA can review the planned change and identify the test cases that will be needed.

### 4. Pull Request

The completed change is submitted through a Pull Request.

**QA Intervention:** QA checks the changes and verifies that appropriate tests have been added or updated.

### 5. Review

Team members review the Pull Request before merging.

**QA Intervention:** QA participates in the review and checks functionality, test coverage, risks, and possible defects.

### 6. Merge

After approval and successful checks, the Pull Request is merged into the `main` branch.

**QA Intervention:** QA confirms that required quality conditions have been satisfied before the change is merged.

### 7. CI

Continuous Integration automatically builds and runs automated tests and quality checks.

**QA Intervention:** QA monitors CI results and investigates any failed tests or quality checks.

### 8. Release

The validated change is included in a released version of the software.

**QA Intervention:** QA performs or verifies final validation/regression testing and confirms that the release meets the requirements.

## Summary

The QA engineer can contribute throughout the complete workflow, not only after development is finished. Early QA involvement helps identify unclear requirements and risks, while testing and CI checks help prevent defective changes from reaching the released software.
