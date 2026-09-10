

__name__  -->  is a special built‑in variable that tells whether a file is being run directly or imported as a module

<!-- --------------------------------------------------------------------------->
Route = A rule that defines how an app responds to a request.

Router = The mechanism that matches requests to routes.

Routing = The overall process of directing requests to the right handler.



<!-- ------------------------------------------------------------------ -->


Static data is fixed content that does not change with user requests. It includes files like CSS, JavaScript, and images stored in the static/ folder. These files are served directly by Flask and remain the same for all users.


Dynamic data is content generated at runtime based on user input or database queries. It is rendered using Jinja2 templates inside the templates/ folder. This data can be different for each user, such as showing their name or personalized content.
<!-- ------------------------------------------------------------------------- -->

In Flask, URL converters are used inside route definitions to capture parts of the URL and pass them as variables to your view functions. They help you define what type of data you expect in the URL.

🔑 Common URL Converters

<string:variable> → Default, captures text (no slashes).

<int:variable> → Captures integers only.

<float:variable> → Captures floating-point numbers.

<path:variable> → Captures text including slashes (like file paths).

<uuid:variable> → Captures UUID strings.


<!-- ------------------------------------------------------------------------------------ -->

QUERY PARAMETER 

In Flask, query parameters are the values you pass in the URL after a ? symbol. They are often used to filter, search, or customize the response without changing the route itself.

🔑 Key Points
Query parameters come after ? in the URL.

Multiple parameters are separated by &.

You access them in Flask using request.args.