import math


class PhotoAlbum:
    PAGE_SIZE: int = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list[list] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, count: int):
        return cls(math.ceil(count/4))

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos):
            if len(page) < self.PAGE_SIZE:
                page.append(label)
                return f"{label} photo added successfully on page {1+i} slot {len(page)}"

        return "No more free slots"

    def display(self):
        result = ["-----------"]
        for line in self.photos:
            result.append(" ".join("[]" for p in line))
            result.append("-----------")
        return "\n".join(result)

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())




