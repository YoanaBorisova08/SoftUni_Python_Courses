from project.product import Product


class ProductRepository:
    products: list[Product] = []
    def add(self, p: Product):
        self.products.append(p)

    def find(self, p_name: str):
        for p in self.products:
            if p.name == p_name:
                return p

    def remove(self, p_name: str):
        for p in self.products:
            if p.name == p_name:
                self.products.remove(p)

    def __repr__(self):
        return "\n".join(f"{p.name}: {p.quantity}" for p in self.products)