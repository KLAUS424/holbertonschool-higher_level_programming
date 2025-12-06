#!/usr/bin/env python3
"""
Task 00: Introduction to Templating
A simple templating program that generates personalized invitations.
"""

import os


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and list of attendees.
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee data
    Returns:
        None: Creates output files or logs errors
    """
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    # Check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    # Check if all items in attendees are dictionaries
    for i, attendee in enumerate(attendees):
        if not isinstance(attendee, dict):
            print(f"Error: Attendee at index {i} is not a dictionary.")
            return
    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Start with the template
        invitation = template
        # Define the placeholder keys we're looking for
        placeholders = ['name', 'event_title', 'event_date', 'event_location']
        # Replace each placeholder with the value or "N/A"
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            if value is None or value == "":
                value = "N/A"
            # Replace the placeholder in the template
            invitation = invitation.replace(f"{{{placeholder}}}", str(value))
        # Create the output filename
        filename = f"output_{i}.txt"
        # Write the invitation to file
        try:
            with open(filename, 'w') as file:
                file.write(invitation)
            print(f"Created {filename}")
        except Exception as e:
            print(f"Error writing file {filename}: {e}")


# Test the function (if run directly)
if __name__ == "__main__":
    # Read the template from file if template.txt exists
    try:
        with open('template.txt', 'r') as file:
            template_content = file.read()
    except FileNotFoundError:
        # Use the template from the problem description
        template_content = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""
    # Test data
    test_attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]
    # Generate invitations
    generate_invitations(template_content, test_attendees)
