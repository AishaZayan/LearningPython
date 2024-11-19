class Profile:
  def __init__(self, name, email, language):
    self.name = name
    self.email = email
    self.language = language


profile_1 = Profile("Aisha", "aisha.mzayan@gmail.com", "French")
profile_2 = Profile("Ahmed", "ahmed.mzayan@gmail.com", "English")
profile_3 = Profile("Slam", "salam.abdaalah@gmail.come", "Chinies")

print(f"The first user's name is {profile_1.name}")
print(f"The second user's email is {profile_2.email}")
print(f"The third user's learning language is {profile_3.language}")
   