import webapp2
import random

#html boilerplate

page_header = """
<!DOCTYPE html>
<html>
    <head>
    <title>Flicklist</title>
    </head>
    <body>
    <h1>Flicllist</h1>
    </body>
<html>"""

class Index(webapp2.RequestHandler):


    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movie_list = ['Pulp Fiction', 'Serenity', 'Moonrise Kingdom', 'Starwars: Rogue Force One', 'Your Name']

        # TODO: randomly choose one of the movies, and return it


        return random.choice(movie_list)

    def get(self):

        edit_header = "<h3>Edit My Watchlist</h3>"

        add_form - """
        <form attribute="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to mywatchlist
            </lable>
            <input type="submit" name="Add It"/>
        </form>"""

        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content2 = "<h1>Movie of the Day</h1>"
        content2 += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        movie2 = self.getRandomMovie()

        content = "<h1>Tomorrow's Movie</h1>"
        content += "<p>" + movie2 + "</p>"

        self.response.write(content2 + content)



app = webapp2.WSGIApplication([
    ('/', Index)
    ('/add', AddMovie)
], debug=True)
