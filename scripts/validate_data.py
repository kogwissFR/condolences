#!/usr/bin/env python3
"""
Validate stories.yml data integrity.
Run before committing changes or as part of CI/CD.
"""

import yaml
import sys
from datetime import datetime
from pathlib import Path


def validate_stories():
    """Validate all stories in the YAML file."""
    print("=" * 60)
    print("Kogni Memorial - Story Validation Script")
    print("=" * 60)
    
    errors = []
    warnings = []
    
    # Check if file exists
    stories_file = Path('_data/stories.yml')
    if not stories_file.exists():
        print("\n✓ No stories.yml yet (acceptable for new project)")
        return True
    
    # Load YAML
    try:
        with open(stories_file, 'r', encoding='utf-8') as f:
            stories = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"\n✗ YAML parsing error: {e}")
        return False
    except Exception as e:
        print(f"\n✗ Error reading file: {e}")
        return False
    
    # Handle empty file
    if not stories:
        print("\n✓ Empty stories list (acceptable)")
        return True
    
    if not isinstance(stories, list):
        print(f"\n✗ Stories data must be a list, got {type(stories).__name__}")
        return False
    
    print(f"\n[1/3] Validating {len(stories)} stories...")
    
    # Validate each story
    for i, story in enumerate(stories, 1):
        story_errors = validate_story(story, i)
        errors.extend(story_errors)
    
    print(f"\n[2/3] Checking for duplicate IDs...")
    ids = [s.get('id') for s in stories if 'id' in s]
    duplicates = [id for id in ids if ids.count(id) > 1]
    if duplicates:
        errors.append(f"Duplicate story IDs found: {set(duplicates)}")
    else:
        print(f"✓ All {len(ids)} story IDs are unique")
    
    print(f"\n[3/3] Checking chronological order...")
    dates = [s.get('publication_date') for s in stories if 'publication_date' in s]
    if dates and dates != sorted(dates, reverse=True):
        warnings.append("Stories are not sorted by publication date (newest first)")
    else:
        print("✓ Stories are properly sorted")
    
    # Print results
    print("\n" + "=" * 60)
    print("VALIDATION RESULTS")
    print("=" * 60)
    
    if errors:
        print(f"\n✗ Found {len(errors)} error(s):\n")
        for error in errors:
            print(f"  - {error}")
    else:
        print(f"\n✓ All {len(stories)} stories validated successfully!")
    
    if warnings:
        print(f"\n⚠ {len(warnings)} warning(s):\n")
        for warning in warnings:
            print(f"  - {warning}")
    
    print("\n" + "=" * 60)
    
    return len(errors) == 0


def validate_story(story, story_num):
    """Validate a single story entry."""
    errors = []
    
    if not isinstance(story, dict):
        errors.append(f"Story {story_num}: Must be a dictionary")
        return errors
    
    # Required fields
    required_fields = ['id', 'author_name', 'title', 'content', 'publication_date']
    for field in required_fields:
        if field not in story:
            errors.append(f"Story {story_num}: Missing required field '{field}'")
        elif not story[field]:
            errors.append(f"Story {story_num}: Field '{field}' is empty")
    
    # ID format
    story_id = story.get('id', '')
    if story_id and not (isinstance(story_id, str) and len(story_id) == 3 and story_id.isdigit()):
        errors.append(f"Story {story_num}: ID must be 3-digit string (e.g., '001'), got '{story_id}'")
    
    # Content length validation
    content = story.get('content', '')
    if isinstance(content, str):
        if len(content) < 50:
            errors.append(f"Story {story_num}: Content too short ({len(content)} chars, min 50)")
        if len(content) > 5000:
            errors.append(f"Story {story_num}: Content too long ({len(content)} chars, max 5000)")
    
    # Title length validation
    title = story.get('title', '')
    if isinstance(title, str):
        if len(title) < 5:
            errors.append(f"Story {story_num}: Title too short ({len(title)} chars, min 5)")
        if len(title) > 200:
            errors.append(f"Story {story_num}: Title too long ({len(title)} chars, max 200)")
    
    # Date format validation
    pub_date = story.get('publication_date', '')
    if pub_date:
        try:
            datetime.strptime(str(pub_date), '%Y-%m-%d')
        except ValueError:
            errors.append(f"Story {story_num}: Invalid publication_date format (expected YYYY-MM-DD), got '{pub_date}'")
    
    submission_date = story.get('submission_date')
    if submission_date:
        try:
            datetime.strptime(str(submission_date), '%Y-%m-%d')
        except ValueError:
            errors.append(f"Story {story_num}: Invalid submission_date format (expected YYYY-MM-DD), got '{submission_date}'")
    
    # Graduation year validation (optional field)
    grad_year = story.get('graduation_year')
    if grad_year is not None:
        if not isinstance(grad_year, int):
            errors.append(f"Story {story_num}: graduation_year must be an integer, got {type(grad_year).__name__}")
        elif not (1990 <= grad_year <= 2029):
            errors.append(f"Story {story_num}: graduation_year must be between 1990-2029, got {grad_year}")
    
    # Author name validation
    author = story.get('author_name', '')
    if isinstance(author, str) and (len(author) < 2 or len(author) > 100):
        errors.append(f"Story {story_num}: author_name length must be 2-100 chars, got {len(author)}")
    
    return errors


def main():
    """Main entry point."""
    success = validate_stories()
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
