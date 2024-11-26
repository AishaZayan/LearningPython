print("______ Movie List _______\n \n \n")

class Movie:
  def __init__(self, title, director, release_year, genre):
    self.tilte = title
    self.director = director
    self.release_year= release_year
    self.genre = genre

  def display_movie(self):
    print(f"Title: {self.tilte}")
    print(f"Director: {self.director}")
    print(f"Release: {self.release_year}")
    print(f"Genre: {self.genre}\n \n")

  def change_movie_director(self, new_director):
    self.director = new_director


movie1 = Movie("Inception", "Christopher Nolan", 2010, "Sci_fi")
movie2 = Movie("The Godfather", "Francis Ford Coppola", 1927, "Crime")
movie3 = Movie("Parasite", "Bong Joon_ho", 2019, "Thriller")

movie1.display_movie()
movie2.display_movie()
movie3.display_movie()

print("Changing movies directors... \n \n \n")

movie1.change_movie_director("Shokry Sarhan")
movie2.change_movie_director("Ahmed Mazhar")
movie3.change_movie_director("Ismaeel Yaseen")

movie1.display_movie()
movie2.display_movie()
movie3.display_movie()