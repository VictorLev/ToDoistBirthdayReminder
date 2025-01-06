# Birthday Reminder Workflow

This repository contains a GitHub Actions workflow that sends a birthday reminder to Todoist. The birthdays are stored in the `BIRTHDAY_DATA` variable in the repository's settings. This document explains how to change the birthday of a person in the `BIRTHDAY_DATA` variable.

## Changing a Birthday in the `BIRTHDAY_DATA` Variable

Follow these steps to update the birthday for someone in the `BIRTHDAY_DATA` variable:

### 1. Open Your GitHub Repository

Navigate to the GitHub repository where the workflow is stored.

### 2. Access Repository Settings

1. Go to the **Settings** tab at the top of your repository.
2. In the left sidebar, click on **Secrets and Variables**.
3. Under **Secrets and Variables**, select **Actions**.

### 3. Edit the `BIRTHDAY_DATA` Variable

1. In the **Variables** section, locate the variable named `BIRTHDAY_DATA`.
2. Click on the **Edit** button next to the variable name.

### 4. Update the Birthday Information

The `BIRTHDAY_DATA` variable contains a JSON object with names as keys and their birthdays (in `MM-DD` format) as values. For example:

```json
{
    "Lily": "11-25",
    "Constance Levesque": "05-16",
    "Justine Levesque": "09-19",
    "Marc-Andre": "08-17"
}
