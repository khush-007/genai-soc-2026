import json


def format_code_review(response):

    try:
        data = json.loads(response)

        issues = "\n".join(
            f"- {item}" for item in data.get("issues", [])
        )

        suggestions = "\n".join(
            f"- {item}" for item in data.get("suggestions", [])
        )

        markdown = f"""
# 📋 Code Review

## Summary
{data.get("summary", "N/A")}

## ⚠️ Issues
{issues}

## 💡 Suggestions
{suggestions}

## 🔥 Severity
{data.get("severity", "N/A")}

## ⏱ Complexity
{data.get("complexity", "N/A")}
"""

        return markdown

    except Exception:

        return (
            "⚠️ JSON Parsing Failed\n\n"
            "Raw Response:\n\n"
            f"{response}"
        )