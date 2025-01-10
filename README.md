# Social Media Performance Analysis

## Overview
This project was developed as part of the *Pre-Hackathon Assignment: Social Media Performance Analysis* for the Level Supermind Hackathon. It demonstrates a basic analytics module leveraging *Langflow* and *DataStax Astra DB* to analyze social media engagement data and provide actionable insights.

---

## Features
1. *Data Fetching:*
   - Simulated a dataset containing mock social media engagement data (e.g., likes, shares, comments, post types).
   - Stored the dataset in *DataStax Astra DB* for robust database operations.

2. *Performance Analysis:*
   - Constructed a workflow in *Langflow* to:
     - Accept post types (e.g., carousel, reels, static images) as input.
     - Query the dataset in Astra DB to calculate average engagement metrics for each post type.

3. *Insights Generation:*
   - Leveraged *GPT integration* in Langflow to produce simple, actionable insights, such as:
     - Carousel posts have 20% higher engagement than static posts.
     - Reels generate 2x more comments compared to other formats.

---

## Tech Stack
- *Langflow*: For workflow creation and GPT integration.
- *DataStax Astra DB*: For storing and querying engagement data.
- *GPT Integration*: To generate automated insights.

---

## Repository Structure
---

## Setup Instructions

### Prerequisites
1. *Langflow*: Install Langflow using the official guide from [Langflow.org](https://www.langflow.org/).
2. *DataStax Astra DB*: Set up an account and create a database. Learn more [here](https://www.datastax.com/).

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/social-media-performance.git
   cd social-media-performance
