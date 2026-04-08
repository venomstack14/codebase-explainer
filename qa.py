def search_codebase(query, parsed_data):
    query = query.lower()
    results = []

    for file, details in parsed_data.items():
        score = 0

        for func in details["functions"]:
            if query in func.lower():
                score += 2

        for cls in details["classes"]:
            if query in cls.lower():
                score += 2

        for imp in details["imports"]:
            if imp and query in imp.lower():
                score += 3

        if score > 0:
            results.append((file, score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results


def answer_question(query, parsed_data):
    results = search_codebase(query, parsed_data)

    if not results:
        return "❌ No relevant files found."

    best_file = results[0][0]
    details = parsed_data[best_file]

    answer = f"📄 Best match: {best_file}\n"

    if details["functions"]:
        answer += f"\nFunctions: {', '.join(details['functions'])}"

    if details["classes"]:
        answer += f"\nClasses: {', '.join(details['classes'])}"

    if details["imports"]:
        answer += f"\nImports: {', '.join(details['imports'])}"

    return answer