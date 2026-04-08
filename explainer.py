def explain_file(file, details):
    summary = f"\n📄 File: {file}\n"

    if details["classes"]:
        summary += f"- Classes: {', '.join(details['classes'])}\n"

    if details["functions"]:
        summary += f"- Functions: {', '.join(details['functions'])}\n"

    if details["imports"]:
        summary += f"- Imports: {', '.join(details['imports'])}\n"

    # Simple logic-based insights
    imports_text = " ".join(details["imports"]).lower()

    if "flask" in imports_text:
        summary += "- 🔥 This looks like a Flask web app\n"

    if "sql" in summary.lower():
        summary += "- 🗄️ Contains database-related logic\n"

    return summary


def explain_project(parsed_data):
    total_files = len(parsed_data)
    total_functions = sum(len(d["functions"]) for d in parsed_data.values())

    result = "📊 Project Summary:\n"
    result += f"- Total files: {total_files}\n"
    result += f"- Total functions: {total_functions}\n"

    return result