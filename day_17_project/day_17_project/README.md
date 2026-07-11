"""
1. What is template inheritance? What problem does it solve?

Template inheritance is a Django feature that allows one template to inherit
the layout and structure of another template, such as base.html, using the
{% extends %} tag. It solves the problem of repeating the same HTML code
(header, navigation bar, footer, etc.) on multiple pages. Any change made to
base.html is automatically reflected in all child templates.

2. What is the difference between {{ variable }} and {% tag %}?

{{ variable }} is used to display the value of a variable in a template.

{% tag %} is used for template logic such as loops, conditions, template
inheritance, and loading templates.

Example:
{{ username }}          -> Displays the value of username.
{% for post in posts %} -> Loops through the posts list.

3. What is the purpose of {% url 'view_name' %} instead of hardcoding the path?

The {% url %} tag generates URLs dynamically using the view name defined in
urls.py. This makes templates easier to maintain because if a URL changes,
only urls.py needs to be updated instead of every template. It also helps
prevent broken links.

4. What is a template filter? Give an example not used before.

A template filter modifies the value of a variable before displaying it.
Filters are applied using the | (pipe) symbol.

Example:
{{ "HELLO DJANGO"|lower }}

Output:
hello django

The 'lower' filter converts all text to lowercase.
"""
<img width="1600" height="632" alt="image" src="https://github.com/user-attachments/assets/f464a742-4fbf-4141-b415-db824b7f97d4" />
<img width="1600" height="531" alt="image" src="https://github.com/user-attachments/assets/6c5ab699-e54f-47fe-a058-48ba0e54fe65" />
<img width="1600" height="561" alt="image" src="https://github.com/user-attachments/assets/21dc1f06-9c0c-46b2-af9d-430639416aeb" />
<img width="1600" height="508" alt="image" src="https://github.com/user-attachments/assets/1ee0fd58-2f5a-44b5-b69d-fe1a1393e846" />




