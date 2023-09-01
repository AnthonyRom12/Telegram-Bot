def get_topics_for_language(language):
    if language == "language_python":
        return ["topic_str", "topic_numbers", "topic_bool", "topic_for", "topic_while"]
    elif language == "language_java":
        return ["topic_str", "topic_numbers", "topic_bool", "topic_for", "topic_while"]
    elif language == "language_cpp":
        return ["topic_str", "topic_numbers", "topic_bool", "topic_for", "topic_while"]
    else:
        return []