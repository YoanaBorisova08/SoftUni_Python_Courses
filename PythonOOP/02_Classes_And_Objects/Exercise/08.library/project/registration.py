from project.library import Library
from project.user import User


class Registration:

    @staticmethod
    def add_user(user: User, library: Library):
        if any(u.user_id == user.user_id for u in library.user_records):
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    @staticmethod
    def remove_user(user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
            if user.username in library.rented_books:
                del library.rented_books[user.username]
        else:
            return "We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username == new_username:
                    return "Please check again the provided username - it should be different than the username used so far!"

                old_username = user.username
                user.username = new_username

                if old_username in library.rented_books:
                    old_rentals = library.rented_books.pop(old_username)
                    if new_username in library.rented_books:
                        library.rented_books[new_username].update(old_rentals)
                    else:
                        library.rented_books[new_username] = old_rentals

                return f"Username successfully changed to: {new_username} for user id: {user_id}"
        return f"There is no user with id = {user_id}!"
