favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
for name,language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")

candidates = ["jen", "sarah", "shubham", "edward", "phil", "stu", "doug", "alan"]

for candidate in candidates:
    if candidate in favourite_languages.keys():
        print("\nThank you " + candidate.title() + "! Your response has been recorded.")
    else:
        print("\n" + candidate.title() + " please take the poll, "
        "your response has been not recorded yet.")