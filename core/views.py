from django.shortcuts import render

SKILL_GROUPS = [
    {
        "title": "IT automation & data",
        "items": [
            "Python Development", "Automation Scripting", "Process Automation",
            "Data Analytics (Pandas/NumPy)", "Data Visualization & Reporting",
            "SQL / MS SQL Server", "Relational Database Modeling",
        ],
    },
    {
        "title": "Software, web & AI",
        "items": [
            "Django", "Next.js", "React", "Node.js", "REST APIs",
            "Object-Oriented Programming", "Generative AI & Prompt Engineering",
        ],
    },
    {
        "title": "Tools & DevOps",
        "items": [
            "Git & GitHub", "Power BI", "Excel (Data Modeling & Charts)",
            "AWS Cloud Architecture", "OS Administration", "Project Management",
        ],
    },
]

PROJECT_GROUPS = [
    {
        "label": "IT Automation & ERP",
        "color": "var(--accent)",
        "soft": "var(--accent-soft)",
        "projects": [
            {
                "name": "Automated Attendance System with WhatsApp",
                "tags": ["Django", "MS SQL Server", "WhatsApp API"],
                "description": (
                    "An ERP-style enterprise attendance platform backed by Microsoft SQL Server. "
                    "Automates check-in/out logging through WhatsApp, and runs complete workflows for "
                    "leave requests, absences, half-days, and scheduled summary reports."
                ),
            },
            {
                "name": "School Management & Ledger System",
                "tags": ["React", "Firebase", "Financial Modeling"],
                "description": (
                    "A responsive institutional management platform automating student enrollment and "
                    "record-tracking, with data-modeling logic behind real-time cash-flow charts and "
                    "budget tracking."
                ),
            },
        ],
    },
    {
        "label": "Data Science — Power BI",
        "color": "var(--accent-2)",
        "soft": "rgba(53,87,166,0.10)",
        "projects": [
            {
                "name": "Credit Card Customer Report Dashboard",
                "tags": ["Power BI", "Data Modeling", "DAX"],
                "description": (
                    "A Power BI dashboard summarizing credit card customer profiles — segmentation, "
                    "credit limit distribution, and demographic breakdowns for portfolio-level review."
                ),
            },
            {
                "name": "Credit Card Transactions Report Dashboard",
                "tags": ["Power BI", "Data Visualization"],
                "description": (
                    "A companion dashboard tracking transaction volume, spend by category, and trend "
                    "lines over time, built for quick pattern-spotting rather than raw table review."
                ),
            },
        ],
    },
    {
        "label": "Machine Learning",
        "color": "var(--accent-3)",
        "soft": "rgba(168,103,30,0.12)",
        "projects": [
            {
                "name": "Spam Email Detection",
                "tags": ["Python", "scikit-learn", "NLP"],
                "description": (
                    "A text-classification model that flags spam email using standard NLP preprocessing "
                    "and a trained classifier, evaluated on precision/recall rather than accuracy alone."
                ),
            },
            {
                "name": "House Price Prediction",
                "tags": ["Python", "scikit-learn", "Regression"],
                "description": (
                    "A regression model estimating house prices from property features, with feature "
                    "engineering and comparison across a few regression algorithms."
                ),
            },
            {
                "name": "CRUD Chatbot",
                "tags": ["Python", "Chatbot", "Database"],
                "description": (
                    "A conversational interface that performs create, read, update, and delete operations "
                    "on a database through natural-language chat instead of a traditional form-based UI."
                ),
            },
        ],
    },
]

CERTIFICATIONS = [
    {
        "title": "Generative AI: Introduction & Applications",
        "issuer": "IBM / Coursera",
        "url": "https://www.coursera.org/account/accomplishments/verify/GBA8V50RBT95"
    },
    {
        "title": "AWS Certified DevOps Engineer – Professional",
        "issuer": "AWS / Coursera",
        "url": "https://www.coursera.org/account/accomplishments/verify/ZILDSMAT9859"
    },
    {
        "title": "Using Python to Interact with the Operating System",
        "issuer": "Google / Coursera",
        "url": "https://www.coursera.org/account/accomplishments/verify/519FYLLET6R5"
    },
    {
        "title": "Google Crash Course on Python",
        "issuer": "Google / Coursera",
        "url": "https://www.coursera.org/account/accomplishments/verify/3VJYOT44WU71"
    },
]


def home_view(request):
    return render(request, "home.html", {"skill_groups": SKILL_GROUPS})


def projects_view(request):
    return render(request, "projects.html", {"project_groups": PROJECT_GROUPS})


def experience_view(request):
    return render(request, "experience.html", {"certifications": CERTIFICATIONS})



def contact_view(request):
    return render(request, "contact.html")