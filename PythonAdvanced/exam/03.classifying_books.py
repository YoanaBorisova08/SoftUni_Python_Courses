

def classify_books(*book_genres, **isbns):

    fiction_books = {}
    non_fiction_books = {}

    for genre, title in book_genres:
        book_isbn = 0
        for isbn, book in isbns.items():
            if book == title:
                book_isbn = isbn
                del isbns[isbn]
                break

        if genre == "fiction":
            fiction_books[title] = book_isbn
        else:
            non_fiction_books[title] = book_isbn

    sorted_fiction_books = sorted(fiction_books.items(), key=lambda x: x[1])
    sorted_non_fiction_books = sorted(non_fiction_books.items(), key=lambda x: x[1], reverse=True)

    result = []
    if fiction_books:
        result.append("Fiction Books:")
        for title, isbn in sorted_fiction_books:
            result.append(f"~~~{isbn}#{title}")
    if non_fiction_books:
        result.append("Non-Fiction Books:")
        for title, isbn in sorted_non_fiction_books:
            result.append(f"***{isbn}#{title}")
    return "\n".join(result)


